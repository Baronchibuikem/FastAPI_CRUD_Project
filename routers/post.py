from ..models import Post, Base
from ..schemas import PostCreate, PostResponse
from ..database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status,APIRouter, HTTPException, Depends


router = APIRouter()
Base.metadata.create_all(bind=engine)

@router.get('/posts', response_model=list[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    """Get all post."""
    result = db.query(Post).all()
    return result


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """Create a Post."""
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/posts/{id}", response_model=PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    """Get a Post by id."""
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {id} does not match')
    return post


@router.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):
    """Delete a Post by id"""
    post = db.query(Post).filter(Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/post/{id}', response_model=PostResponse)
def update_post(id: int, update_post: PostCreate, db: Session = Depends(get_db)):
    """Update a Post by id"""
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()