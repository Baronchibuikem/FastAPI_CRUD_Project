from app.models import Vote, Post
from app.schemas import VoteBase
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Response, status,APIRouter, HTTPException, Depends
from app.utils.oauth2 import get_current_user


router = APIRouter(
    prefix="/vote",
    tags=["vote"]
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: VoteBase, db: Session= Depends(get_db), current_user:int = Depends(get_current_user)):

    post = db.query(Post).filter(Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {current_user.id} does not exist')
    vote_query = db.query(Vote).filter(Vote.post_id == vote.post_id, Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f'user {current_user.id} has already voted on Post {vote.post_id}')
        new_vote = Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {'message': 'successfully added vote'}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exit")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {'messgae': 'successfully deleted vote'}