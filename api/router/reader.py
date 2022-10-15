from fastapi import APIRouter, Depends, status, HTTPException
import requests
import json
from api.utills import get_token
from api.schema.bio_schema import AddDetails 
from api.settings import Settings
router = APIRouter(
    tags=["Bio Reader"],
    prefix="/reader"
)
URL = Settings.BASE_URL

@router.get("/")
def get_readers():
    url = URL+("/iclock/api/terminals/")
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



@router.get("/{id}")
def get_readers_by_id(id):
    
    url = URL+("/iclock/api/terminals/"+str(id)+"/")
    # return url
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

@router.post("/add_readers")
def add_readers(request:AddDetails):
    payload = {'sn':request.sn, 'alias':request.alias, 'ip_address':request.ip_address, 'terminal_tz':request.terminal_tz, 'heartbeat':request.heartbeat,'area':request.area}
    # return payload
    url = URL+("http://127.0.0.1:8081/iclock/api/terminals/")
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
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
    response = requests.get(url, headers=headers)
    data2  = json.loads(response.text)
    return data2

@router.put("/update_readers/{id}")
def update_readers(id:int, request:AddDetails):
    payload = get_readers_by_id(id)
    # return payload
    if payload is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reader id {id} not found")
    payload['sn'] = request.sn
    payload['alias'] = request.alias
    payload['ip_address'] = request.ip_address
    payload['terminal_tz'] = request.terminal_tz
    payload['heartbeat'] = request.heartbeat
    payload['area'] = request.area
    
    # return payload
    
    # return payload
    url = URL+("/iclock/api/terminals/"+str(id)+"/")
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
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    print(response.text)
    response = requests.get(url, headers=headers)
    data2  = json.loads(response.text)
    return data2
