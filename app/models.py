from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))

    
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'{self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'



class BlogCategory(db.Model):

    __tablename__ = 'categories'

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    # save blog
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = BlogCategory.query.all()
        return categories


#blog class
class Blog(db.Model):
    """ List of blogs in each category """

    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="blog", lazy = "dynamic")
    



    def save_blog(self):
        ''' Save the blog '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_blog(cls):
        Blog.all_blog.clear()

    # display blog

    def get_blog(id):
        blog = Blog.query.filter_by(category_id=id).all()
        return blog


# comments
class Comments(db.Model):
    '''User comment model for each blog '''

    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer, primary_key=True)
    opinion = db.Column(db.String(255))
#     time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))


    def save_comment(self):
        '''
        Save the Comments/comments per blog
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.time_posted.desc()).filter_by(blog_id=id).all()
        return comment

class Quotes:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
