from fastapi import APIRouter, Depends, status, HTTPException
import requests
import json
from api.utills import get_token
from api.settings import Settings
from api.db import get_db
from sqlalchemy.orm import Session
from api.models import Transactions
router = APIRouter(
    tags=["Bio Transactions"],
    prefix="/transactions"
)
URL = Settings.BASE_URL

@router.get("/")
def get_transactions():
    url = URL+("/iclock/api/transactions/")
    token = get_token()
    word1 = "JWT"
    word2 = token
    auth = word1+" "+word2
    # return auth
# or use JWT tokn
    headers = {
    "Content-Type": "application/json",
    # "Authorization": token,
    "Authorization": auth
    }
    # return headers
    response = requests.get(url, headers=headers)
    print(response.text)
    response = requests.get(url, headers=headers)
    data2  = json.loads(response.text)
    return data2

@router.get("/insert_transactions")
def insert_transactions(db:Session = Depends(get_db)):
    url = URL+("/iclock/api/transactions/")
    token = get_token()
    word1 = "JWT"
    word2 = token
    auth = word1+" "+word2
    # return auth
# or use JWT tokn
    headers = {
    "Content-Type": "application/json",
    # "Authorization": token,
    "Authorization": auth
    }
    # return headers
    response = requests.get(url, headers=headers)
    # print(response.text)
    response = requests.get(url, headers=headers)
    data2  = json.loads(response.text)
    transactions = data2['data']
    return data2
    for entry in transactions:
        print(entry) 
        # val = Transactions(emp_code =entry['emp_code'], punch_time=entry['punch_time'], terminal_sn=entry['terminal_sn'],area_alias=entry['area_alias'],upload_time=entry['upload_time'])
        # db.add(val)
        # db.commit()