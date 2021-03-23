from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    items = db.query(models.item).all()
    return items

def create(request: schemas.item,db: Session):
    new_item = models.item(title=request.title, description=request.description,user_id=1)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def destroy(id:int,db: Session):
    item = db.query(models.item).filter(models.item.id == id)

    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item with id {id} not found")

    item.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.item, db:Session):
    item = db.query(models.item).filter(models.item.id == id)

    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item with id {id} not found")

    item.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    item = db.query(models.item).filter(models.item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item with the id {id} is not available")
    return item