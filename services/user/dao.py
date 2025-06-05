from services.dao.base import BaseDAO
from services.user.models.comments import Comments
from services.user.models.friends import Friends
from services.user.models.group_members import GroupMembers
from services.user.models.groups import Groups
from services.user.models.likes import Likes
from services.user.models.messages import Messages
from services.user.models.posts import Posts
from services.user.models.profiles import Profiles


class CommentsDAO(BaseDAO):
    model = Comments


class FriendsDAO(BaseDAO):
    model = Friends


class GroupMembersDAO(BaseDAO):
    model = GroupMembers


class GroupsDAO(BaseDAO):
    model = Groups


class LikesDAO(BaseDAO):
    model = Likes
    
    
class MessagesDAO(BaseDAO):
    model = Messages

    
class PostsDAO(BaseDAO):
    model = Posts
    
    
class ProfilesDAO(BaseDAO):
    model = Profiles
