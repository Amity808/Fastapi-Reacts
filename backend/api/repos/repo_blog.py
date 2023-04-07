from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.schema_blog import BlogBase
from models.model_blog import Blog


def create_blog(blog: BlogBase, db: Session):
    blogs = Blog(**blog.dict())
    db.add(blogs)
    db.commit()
    db.refresh(blogs)
    return blog


def list_allBlog(db: Session):
    blogs = db.query(Blog).filter().all()
    return blogs


def retrive_Blog(id: int, db: Session):
    blogs = db.query(Blog).filter(Blog.id == id).first()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} not found"
        )
    return blogs


def delete_blogs(id: int, db: Session):
    existing_blog = db.query(Blog).filter(Blog.id == id)
    if not existing_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with the id {id} cant be found in the database"
        )
    existing_blog.delete(synchronize_session=False)
    db.commit()
    return {"details": f"Sucessfully deleted {existing_blog}"}