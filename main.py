from fastapi import FastAPI,Response, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from query import executeQuery
from datetime import datetime,date
from dateutil import relativedelta
import pytz
from pydantic import BaseModel

class Request(BaseModel):
    dateOfBirth:datetime

IST = pytz.timezone('Asia/Kolkata')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

@app.get('/addRequest')
def addRequest(name:str,dob:str=datetime.now().strftime("%d-%m-%Y")):
    k=dob.split('-')
    print(k)
    dob_=date(int(k[2]),int(k[1]),int(k[0]))
    today=datetime.now().strftime("%d-%m-%Y")
    k2=today.split('-')
    today_=date(int(k2[2]),int(k2[1]),int(k2[0]))
    age=relativedelta.relativedelta(today_,dob_)
    age_=f"{age.years} years,{age.months} months,{age.days} days"
    data=executeQuery(f"INSERT INTO requests ('name','age','dateOfBirth','created_at') VALUES ('{name}','{age_}','{dob}','{datetime.utcnow()}')")
    return {'status': data,'years':age.years,'months':age.months,'days':age.days}
    # return f'{age.years} years,{age.months} months,{age.days} days'

@app.get('/getRequests')
def addRequest():
    data=executeQuery("select * from requests ")
    return data
