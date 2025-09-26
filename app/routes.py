from fastapi import APIRouter, HTTPException
from .controllers import UserController, PostController, RelationshipController
from .schemas import User, UserCreate, UserUpdate, Post, PostCreate, FollowCreate, FriendshipCreate, LikeCreate

router = APIRouter()

# User Routes
@router.post("/users/", response_model=User)
def create_user(user: UserCreate):
    try:
        return UserController.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{uid}", response_model=User)
def get_user(uid: str):
    try:
        return UserController.get_user(uid)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/users/", response_model=list[User])
def get_all_users():
    return UserController.get_all_users()

@router.put("/users/{uid}", response_model=User)
def update_user(uid: str, user: UserUpdate):
    try:
        return UserController.update_user(uid, user)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{uid}")
def delete_user(uid: str):
    try:
        UserController.delete_user(uid)
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

# Post Routes
@router.post("/users/{user_uid}/posts/", response_model=Post)
def create_post(user_uid: str, post: PostCreate):
    try:
        return PostController.create_post(user_uid, post)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/posts/{uid}", response_model=Post)
def get_post(uid: str):
    try:
        return PostController.get_post(uid)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Post not found")

@router.get("/users/{user_uid}/posts/", response_model=list[Post])
def get_user_posts(user_uid: str):
    try:
        return PostController.get_user_posts(user_uid)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/posts/", response_model=list[Post])
def get_all_posts():
    return PostController.get_all_posts()

@router.delete("/posts/{uid}")
def delete_post(uid: str):
    try:
        PostController.delete_post(uid)
        return {"message": "Post deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Post not found")

# Follow/Unfollow Routes
@router.post("/users/{user_uid}/follow/")
def follow_user(user_uid: str, follow: FollowCreate):
    try:
        RelationshipController.follow_user(user_uid, follow.target_uid)
        return {"message": "User followed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/users/{user_uid}/unfollow/")
def unfollow_user(user_uid: str, follow: FollowCreate):
    try:
        RelationshipController.unfollow_user(user_uid, follow.target_uid)
        return {"message": "User unfollowed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{user_uid}/followers/", response_model=list[User])
def get_followers(user_uid: str):
    try:
        return RelationshipController.get_followers(user_uid)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/users/{user_uid}/following/", response_model=list[User])
def get_following(user_uid: str):
    try:
        return RelationshipController.get_following(user_uid)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

# Friendship Routes
@router.post("/users/{user_uid}/friends/")
def add_friend(user_uid: str, friendship: FriendshipCreate):
    try:
        RelationshipController.add_friend(user_uid, friendship.friend_uid)
        return {"message": "Friend added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{user_uid}/friends/", response_model=list[User])
def get_friends(user_uid: str):
    try:
        return RelationshipController.get_friends(user_uid)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

# Like Routes
@router.post("/users/{user_uid}/likes/")
def like_post(user_uid: str, like: LikeCreate):
    try:
        RelationshipController.like_post(user_uid, like.post_uid)
        return {"message": "Post liked successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))