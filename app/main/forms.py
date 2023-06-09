from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Length
from app.models import User
from flask_babel import _, lazy_gettext as _l

class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args ,**kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
                user = User.query.filter_by(username=self.username.data).first()
                if user is not None:
                    raise ValidationError(_('Please use a different username.'))

class EmptyForm(FlaskForm):
    submit = SubmitField(_l('Submit'))

class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something...'), validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))