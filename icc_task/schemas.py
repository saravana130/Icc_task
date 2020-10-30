from typing import List
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel , HttpUrl, ValidationError,FilePath,EmailStr,constr
from enum import Enum, IntEnum

contact_regex = constr(regex=r'^\d{10,10}$')

class annually_monthly_CTC(str,Enum):
    annually="annually"
    monthly="monthly"

class EmploymentTypes(str,Enum):
    fulltime="Full-Time"
    parttime="Part-Time"
    internship="Internship"


# class UserRoll(str,Enum):
#     Recruiter="Recruiter"
#     Candidate="Candidate"


class RecruitersInfoBase(BaseModel):
    CompanyName:str
    Company_websiteurl:HttpUrl
    description:constr(max_length=150)
    ContactNumber:contact_regex
    companyAddress:constr(max_length=150)

class RecruitersInfoCreate(RecruitersInfoBase):
    pass

class RecruitersInfo(RecruitersInfoBase):
    id:int
    User_id:int

   

    class Config:
        orm_mode=True


class UsersBase(BaseModel):
    username: constr(min_length=2,max_length=50)
    fullname: constr(min_length=2,max_length=50)
    roll:int
    # roll:UserRoll
    email:EmailStr 


class UsersCreate(UsersBase):   
    password:str


class Users(UsersBase):
    id: int
    
    class Config:
        orm_mode = True



class CandidateInfoBase(BaseModel):
    first_name:constr(min_length=2, max_length=25)
    last_name:constr(min_length=2, max_length=25)
    current_company:str
    email:EmailStr
    experience:int
    current_salary:int
    ContactNumber:contact_regex
    salary_is_annually_monthly:annually_monthly_CTC

class CandidateInfoCreate(CandidateInfoBase):
    pass

class CandidateInfo(CandidateInfoBase):
    id:int
    User_id:int

    class Config:
        orm_mode=True

class jobsBase(BaseModel):
    jobTitel:constr(min_length=10, max_length=50)
    ShortDescription:constr(min_length=10, max_length=100)
    job_Description:constr(min_length=100)
    job_location:constr(min_length=5, max_length=50)
    walkin_date:datetime
    employment_type:EmploymentTypes
    is_active:bool

class jobCreate(jobsBase):
    pass    

class Jobs(jobsBase):
    id:int
    User_id:int

    class Config:
        orm_mode = True

class JobApplicationsBase(BaseModel):
    # resume_path:FilePath
    pass


class JobApplicationsCreate(JobApplicationsBase):
    pass    

class JobApplications(JobApplicationsBase):
    id:int
    job_id:int
    Candidate:int

    class Config:
        orm_mode = True          