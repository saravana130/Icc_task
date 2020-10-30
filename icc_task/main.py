from typing import List
import os
# import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException ,File, UploadFile,Form,Request
import shutil
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import models, schemas, crud
from database import engine, SessionLocal
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse ,RedirectResponse

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
app = FastAPI()
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}
# app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/static", StaticFiles(directory=pkg_resources.resource_filename(__name__, 'static')), name="static")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")


# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/user", response_model=schemas.Users)
def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_roll = crud.get_roll_by_id(db, RollId=user.roll)
    if not db_roll:
        raise HTTPException(status_code=400, detail="User Roll Not registered")
    return crud.create_user(db=db, user=user)

@app.post("/recruiter/{user_id}/create",response_model=schemas.RecruitersInfo)
def create_Recruiter(user_id: int,recruiter:schemas.RecruitersInfoCreate,db:Session=Depends(get_db)):
    db_user=crud.get_user_by_id(db,UsersId=user_id)
    if db_user:
        return crud.create_RecruitersInfo(db=db,recruiter=recruiter,user_id=user_id)
    raise HTTPException(status_code=400, detail="User not registered")

@app.post("/candidate/{user_id}/create",response_model=schemas.CandidateInfo)
def create_Candidate(user_id: int,Candidate:schemas.CandidateInfoCreate,db:Session=Depends(get_db)):
    db_user=crud.get_user_by_id(db,UsersId=user_id)
    if db_user:
        return crud.create_candidatesInfo(db=db,candidate=Candidate,user_id=user_id)
    raise HTTPException(status_code=400, detail="User not registered")

@app.get("/jobs",response_model=List[schemas.Jobs])
def get_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_jobs(db, skip=skip, limit=limit)

@app.get("/job/{job_id}",response_model=schemas.Jobs)
def get_job_byID(job_id:int, db: Session = Depends(get_db)):
    recruiter = crud.get_job_by_id(db, job_id=job_id)
    if recruiter is None:
        raise HTTPException(status_code=404, detail="Job not found/job deleted")
    return recruiter

@app.post("/job/",response_model=schemas.Jobs)
def create_job(job:schemas.jobCreate,db:Session=Depends(get_db)):
    db_user=crud.get_user_by_id(db,UsersId=1)
    if db_user:
        return crud.create_jobs(db=db,jobs=job,user_id=1)
    raise HTTPException(status_code=400, detail="User not registered")

@app.delete("/job/{job_id}",response_model=schemas.Jobs)
def delete_job(job_id: int,db:Session=Depends(get_db)):
    db_job=crud.get_job_by_id(db,job_id=job_id)
    if db_job:
        return crud.del_job(db,job_id=job_id)
    raise HTTPException(status_code=400, detail="User not found")

@app.put("/job/{job_id}", response_model=schemas.Jobs)
def edit_job(job_id: int, job: schemas.jobCreate, db: Session = Depends(get_db)):
	get_job_byID(db=db, job_id=job_id)
	obj = crud.edit_jobs(db=db,job_id=job_id,jobs=job)
	return obj




# @app.post("/job/{jobId}/apply",response_model=schemas.JobApplications)
# def create_upload_file0(db:Session=Depends(get_db),file: UploadFile = File(...),user_id: str = Form(...)):
#     file_path=UPLOAD_FOLDER+"/"+file.filename
#     if file.content_type=="application/pdf":
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)  
          
#         return crud.create_JobApplications(db=db,job_id=jobId,Candidate=user_id,resume_path=file_path)
#     raise HTTPException(status_code=405, detail="Upload pdf file")

    

@app.get("/job/{jobId}/apply",response_model=schemas.JobApplications)
def create_jobapply(jobId: int,job:schemas.JobApplicationsCreate,db:Session=Depends(get_db)):
    return crud.create_JobApplications(db=db,job_id=jobId,Candidate=2)


@app.get("/")
async def read_index():
    return RedirectResponse('/templates/home.html')

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8081)
