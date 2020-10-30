from sqlalchemy.orm import Session

import models, schemas


def get_user_by_username(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()

def get_user_by_id(db: Session, UsersId:int):
    return (db.query(models.Users).get(UsersId))

def get_roll_by_id(db: Session, RollId:int):
    return (db.query(models.UserRolls).get(RollId))    


def create_user(db: Session, user: schemas.UsersCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_RecruitersInfo(db: Session, recruiter: schemas.RecruitersInfoCreate,user_id: int):
    db_user = models.RecruitersInfo(**recruiter.dict(),User_id=user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_candidatesInfo(db: Session, candidate: schemas.CandidateInfoCreate,user_id: int):
    db_user = models.CandidateInfo(**candidate.dict(),User_id=user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_jobs(db: Session, jobs: schemas.jobCreate,user_id: int):
    db_user = models.Jobs(**jobs.dict(),User_id=user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_job_by_id(db: Session, job_id: int):
    return (db.query(models.Jobs).get(job_id))

def get_jobs(db: Session,skip: int = 0, limit: int = 100):
    return (db.query(models.Jobs).offset(skip).limit(limit).all())

def del_job(db:Session,job_id:int):
    db_jobs=db.query(models.Jobs).get(job_id)
    db.delete(db_jobs)
    db.commit()

def edit_jobs(db:Session,job_id:int,jobs:schemas.jobCreate):
    print(jobs)
    job_obj=db.query(models.Jobs).get(job_id)
    job_obj.employment_type=jobs.employment_type
    job_obj.is_active=jobs.is_active
    job_obj.job_Description=jobs.job_Description
    job_obj.job_location=jobs.job_location
    job_obj.jobTitel=jobs.jobTitel
    job_obj.ShortDescription=jobs.ShortDescription
    job_obj.walkin_date=jobs.walkin_date
    db.commit()
    return job_obj

# def create_JobApplications(db: Session,job_id:int,Candidate:int,resume_path:str):
#     db_user = models.JobApplications(job_id=job_id,Candidate=Candidate,resume_path=resume_path)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def create_JobApplications(db: Session,job_id:int,Candidate:int):
    print(db)
    db_user = models.JobApplications(job_id=job_id,Candidate=Candidate)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

