
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from wtforms.validators import DataRequired





class BlogForm(FlaskForm):
     title = StringField('Title', validators=[DataRequired()])
     content = TextAreaField('Content',validators=[DataRequired()])
     submit = SubmitField('Blog')

