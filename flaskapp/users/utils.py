import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskapp import  mail


def save_picture(form_picture):
    ramdom_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = ramdom_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn) 

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn  



def send_reset_email(user):
    token = user.get_reset_tokon()
    msg = Message('Password Reset Request',
                sender='yabalmicheal@gmail.com',
                recipients=[user.email])


    msg.body = f'''To reset your password visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, simply ignore this email and changes will be made.
'''
    mail.send(msg)