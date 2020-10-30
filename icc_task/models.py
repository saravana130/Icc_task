from sqlalchemy import Column,Boolean, Integer, String,Enum,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime

class UserRolls(Base):
    __tablename__="userrolls"
    id = Column(Integer, primary_key=True, index=True)
    user_roll=Column(String(25),unique=True)
    

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password = Column(String(10))
    fullname = Column(String(50))
    roll=Column(ForeignKey("userrolls.id"),nullable=False)
    email=Column(String,nullable=False)
    created_date=Column(DateTime,default=datetime.datetime.utcnow)
    # recruiters_info=relationship("RecruitersInfo", uselist=False,backref="users",cascade="all, delete")
    # recruiters_info=relationship("RecruitersInfo", uselist=False,backref="users",cascade="all, delete")


class RecruitersInfo(Base):
    __tablename__="recruitersinfo"
    id = Column(Integer, primary_key=True, index=True)
    User_id=Column(ForeignKey("users.id"),nullable=False)
    CompanyName=Column(String(50))
    Company_websiteurl=Column(String, index=True)
    description=Column(String(150), index=True)
    ContactNumber=Column(String(10), index=True)
    companyAddress=Column(String(150), index=True)
    # users=relationship("Users",backref="recruiters_info",)

class CandidateInfo(Base):
    __tablename__="candidateinfo"
    id = Column(Integer, primary_key=True, index=True)
    User_id=Column(ForeignKey("users.id"),nullable=False)
    first_name=Column(String(25))
    last_name=Column(String(25))
    email = Column(String,unique=True, index=True)
    experience=Column(Integer)
    ContactNumber=Column(String(10), index=True)
    current_company=Column(String,index=True)
    current_salary=Column(Integer)
    salary_is_annually_monthly=Column(String(8),nullable=False)

class Jobs(Base):
    __tablename__ = "jobs"
    id = Column(Integer,primary_key=True, index=True)
    User_id=Column(ForeignKey("users.id"))
    jobTitel=Column(String, index=True)
    ShortDescription = Column(String, index=True)
    job_Description=Column(String, index=True)
    job_location=Column(String, index=True)
    walkin_date=Column(DateTime)
    created_date=Column(DateTime,default=datetime.datetime.utcnow)
    employment_type=Column(String(25), index=True)
    is_active = Column(Boolean, default=True)

class JobApplications(Base):
    __tablename__ = "jobapplications"
    id = Column(Integer, primary_key=True, index=True)
    job_id=Column(ForeignKey("jobs.id"))
    Candidate=Column(ForeignKey("users.id"))
    # resume_path=Column(String)
    jobApplication_date=Column(DateTime,default=datetime.datetime.utcnow)
