from fastapi import APIRouter, Depends, status, HTTPException
import requests
import json
from api.utills import get_token, get_are_by_area_name
from api.schema.bio_schema import AddArea
from api.settings import Settings
from api.db import get_db
from sqlalchemy.orm import Session
from api.models import Area

router = APIRouter(
    tags=["Bio Area"],
    prefix="/area"
)
URL = Settings.BASE_URL

@router.get("/")
def get_areas():
    get_url = URL
    # return get_url
    url = URL+('/personnel/api/areas/')
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

@router.get("/insert_data/")
def get_areas(db:Session = Depends(get_db)):
    url = URL+('/personnel/api/areas/')
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
    response = requests.get(url, headers=headers)
    data2  = json.loads(response.text)
    area_codes = data2['data']
    # return area_codes
    for entry in area_codes:
        parent_area=entry['parent_area']
        exist_areacode = get_are_by_area_name(db, entry['area_code'])
        if not exist_areacode:
            if parent_area != None:
                parent_area = entry['parent_area']['id']
            val = Area(area_code =entry['area_code'], area_name=entry['area_name'], parent_area=parent_area)
            db.add(val)
            db.commit()
            
       
        


    
    

@router.get("/{id}")
def get_areas_by_id(id:int):
    url = URL+("/personnel/api/areas/"+str(id)+"/")
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

@router.post("/add_area")
def add_readers(request:AddArea):
    payload = {'area_code':request.area_code, 'area_name':request.area_name, 'parent_area':request.parent_area}
    # return payload
    url = URL+("/personnel/api/areas/")
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

@router.put("/update_area/{id}")
def update_readers(id:int, request:AddArea):
    payload = get_areas_by_id(id)
    # return payload
    if payload is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Area id {id} not found")
    payload['area_code'] = request.area_code
    payload['area_name'] = request.area_name
    payload['parent_area'] = request.parent_area

    # return payload
    
    # return payload
    url = URL+("/personnel/api/areas/"+str(id)+"/")
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





