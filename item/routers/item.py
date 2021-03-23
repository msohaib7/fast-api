from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import item

router = APIRouter(
    prefix="/item",
    tags=['items']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.Showitem])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.item, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.item, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.update(id,request, db)


@router.get('/{id}', status_code=200, response_model=schemas.Showitem)
def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.show(id,db)