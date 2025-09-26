from neomodel import db
from .models import User, Post
from .schemas import UserCreate, UserUpdate, PostCreate
from datetime import datetime

# User CRUD Operations
class UserController:
    @staticmethod
    def create_user(user_data: UserCreate) -> User:
        user = User(
            username=user_data.username,
            email=user_data.email
        )
        user.save()
        return user
    
    @staticmethod
    def get_user(uid: str) -> User:
        user = User.nodes.get(uid=uid)
        return user
    
    @staticmethod
    def get_all_users() -> list[User]:
        users = User.nodes.all()
        return users
    
    @staticmethod
    def update_user(uid: str, user_data: UserUpdate) -> User:
        user = User.nodes.get(uid=uid)
        
        if user_data.username is not None:
            user.username = user_data.username
        if user_data.email is not None:
            user.email = user_data.email
        
        user.updated_at = datetime.utcnow()
        user.save()
        return user
    
    @staticmethod
    def delete_user(uid: str) -> bool:
        user = User.nodes.get(uid=uid)
        user.delete()
        return True

# Post CRUD Operations
class PostController:
    @staticmethod
    def create_post(user_uid: str, post_data: PostCreate) -> Post:
        user = User.nodes.get(uid=user_uid)
        post = Post(content=post_data.content)
        post.save()
        post.author.connect(user)
        return post
    
    @staticmethod
    def get_post(uid: str) -> Post:
        post = Post.nodes.get(uid=uid)
        return post
    
    @staticmethod
    def get_user_posts(user_uid: str) -> list[Post]:
        user = User.nodes.get(uid=user_uid)
        posts = user.posts.all()
        return posts
    
    @staticmethod
    def get_all_posts() -> list[Post]:
        posts = Post.nodes.all()
        return posts
    
    @staticmethod
    def delete_post(uid: str) -> bool:
        post = Post.nodes.get(uid=uid)
        post.delete()
        return True

# Relationship Operations
class RelationshipController:
    @staticmethod
    def follow_user(user_uid: str, target_uid: str) -> bool:
        user = User.nodes.get(uid=user_uid)
        target_user = User.nodes.get(uid=target_uid)
        user.following.connect(target_user)
        return True
    
    @staticmethod
    def unfollow_user(user_uid: str, target_uid: str) -> bool:
        user = User.nodes.get(uid=user_uid)
        target_user = User.nodes.get(uid=target_uid)
        user.following.disconnect(target_user)
        return True
    
    @staticmethod
    def get_followers(user_uid: str) -> list[User]:
        user = User.nodes.get(uid=user_uid)
        followers = user.followers.all()
        return followers
    
    @staticmethod
    def get_following(user_uid: str) -> list[User]:
        user = User.nodes.get(uid=user_uid)
        following = user.following.all()
        return following
    
    @staticmethod
    def add_friend(user_uid: str, friend_uid: str) -> bool:
        user = User.nodes.get(uid=user_uid)
        friend = User.nodes.get(uid=friend_uid)
        user.friends.connect(friend)
        return True
    
    @staticmethod
    def get_friends(user_uid: str) -> list[User]:
        user = User.nodes.get(uid=user_uid)
        friends = user.friends.all()
        return friends
    
    @staticmethod
    def like_post(user_uid: str, post_uid: str) -> bool:
        user = User.nodes.get(uid=user_uid)
        post = Post.nodes.get(uid=post_uid)
        user.likes.connect(post)
        return True