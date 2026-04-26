from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1:{
        'name':'Aditya',
        'website':'adi.director.com',
        'age':20
    }
}

#Base Pydantic Models
class User(BaseModel):
    name: str
    website: str
    age: int

class UpdateUser(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None


#Endpoint (URL)
@app.get('/')
def root():
    return {'message':'Hello'}

@app.get('/users/{user_id}')
def get_user(user_id: int = Path(..., description='enter the user detail', gt=0, lt=100)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='user not found')
    return users[user_id]

#create a User
@app.post('/users/{user_id}', status_code=status.HTTP_201_CREATED)
def create_user(user_id: int, user:User):
    if user_id in users:
        raise HTTPException(status_code=400, detail='user Already Exist')
    
    users[user_id] = user.dict()
    return user

#Update a User
@app.put('/user/{user_id}')
def update_user(user_id: int, user:UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='user not Exist')
    
    current_user = users[user_id]

    if user.name is not None:
        current_user['name'] = user.name
    if user.website is not None:
        current_user['website'] = user.website
    if user.age is not None:
        current_user['age'] = user.age

    return current_user

#Delete a user
@app.delete('users/{user_id}')
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='user not Exist')
    
    deleted_user = users.pop(user_id)
    return{'message':' User has been deleted', 'deleted_user':delete_user}

#Search for a user
@app.get('/users/search/')
def search_by_name(name: Optional[str] = None):
    if not name:
        return {'message':'Name parameter is required'}
    
    for user in users.values():
        if user['name'] == name:
            return user
        
    raise HTTPException(status_code=404, detail='User not found!')