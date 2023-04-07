from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.model_blog import Blog
from schemas.schema_blog import BlogBase
from db.database import get_db
from api.repos import repo_blog

router = APIRouter()


@router.post('/create')
def new_blog(blog: BlogBase, db: Session = Depends(get_db)):
    aBlog = repo_blog.create_blog(blog, db)
    return aBlog


@router.get('/all')
def getAllBlog(db: Session = Depends(get_db)):
    aBlog = repo_blog.list_allBlog(db)
    return aBlog


@router.get('/{id}')
def getById(id: int, db: Session = Depends(get_db)):
    allBlog = repo_blog.retrive_Blog(id, db)
    return allBlog


@router.delete('/delete/{id}')
def deleteBlogId(id: int, db: Session = Depends(get_db)):
    deleteBy = repo_blog.delete_blogs(id, db)
    return deleteBy


@router.put('/update/{id}')
def updateBlogId(id: int, blog: BlogBase, db: Session = Depends(get_db)):
    blogUpdate = db.query(Blog).filter(Blog.id == id)
    if not blogUpdate.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The details with the id {id} not found"
        )
    if blogUpdate.first():
        blog.__dict__.update(id=id)
        blogUpdate.update(blog.__dict__)
        db.commit()
        return {"message": "Successfully Updated"}
    else:
        return {"message": " Your are not authorized"}

