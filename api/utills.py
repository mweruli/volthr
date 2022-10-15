import requests
import json
from api.settings import Settings
from sqlalchemy.orm import Session
from api.models import Area

URL = Settings.BASE_URL

def get_token():
   url = URL+("/jwt-api-token-auth/")

   headers = {
    "Content-Type": "application/json",
   }
   data = {
    "username": Settings.BIO_USERNAME,
    "password": Settings.BIO_PASSWORD
   }

   response = requests.post(url, data=json.dumps(data), headers=headers)
   data2  = json.loads(response.text)
   token = data2['token']
   return token

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
    # print(response.text)
    # response = requests.get(url, headers=headers)
    data2  = json.loads(response.text)
    return data2

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

def get_are_by_area_name(db: Session, area_code: str):
    return db.query(Area).filter(Area.area_code == area_code).first()

# def update_area(id:int, area_code:Optional[str], area_name:Optional[str], parent_area:Optional[str]):
#     payload = get_areas_by_id(id)
#     # return payload
#     if payload is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Area id {id} not found")
#     if payload.area_code != None:
#         payload.area_code = area_code
#     if area_name:
#         payload = payload.values(area_name=area_name)
#     if parent_area:
#         payload = payload.values(parent_area=parent_area)
        
    
#     return payload