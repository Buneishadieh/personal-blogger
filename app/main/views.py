from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db,photos
from app.requests import GetQuotes
from flask_login import login_required,current_user
from .forms import BlogForm

#display categories on the landing page
@main.route('/')
def index():
    """ View root page function that returns index page """
    
    quotes = GetQuotes()
    print(quotes)
    title = 'Home- Welcome'
    return render_template('index.html', title = title,quotes = quotes)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comment', methods = ['GET','POST'])
def comment():
    form =BlogForm()
    if form.validate_on_submit():
      blog = Blog(title = form.title.data, category =form.category.data, content = form.content.data, author = form.author.data,upvote = 0,downvote = 0,user_id=current_user.id)
      blog.save_blog()
    return render_template('comment.html',form=form)

# @main.route('/comments/<int:blog_id>/comment',methods=['POST','GET'])
# @login_required
# def comment(blog_id):
#     form = CommentsForm()
#     blog = Blog.query.filter_by(id = blog_id).first()
#     user = current_user.username
#     if form.validate_on_submit():
#         comment = Comment(content = form.comment.data,user_id = current_user.id,blog_id = blog.id)
#         db.session.add(comment)
#         db.session.commit()
#         return redirect(url_for('./comment'),blog_id=blog_id))
#     return render_template('comments.html', form = form,blog=blog,blog_id=blog_id,user=user)

@main.route('/view', methods = ['GET','POST'])
def view():

    return render_template('view.html')

@main.route('/about', methods = ['GET','POST'])
def about():
    
    return render_template('about.html')

@main.route('/profile', methods = ['GET','POST'])
def profile():
    
    return render_template('profile.html')

