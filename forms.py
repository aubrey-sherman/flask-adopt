"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")

    species = StringField(
        "Species")
    # TODO: add choices as validation for three options

    photo_url = StringField("Photo URL")

    age = SelectField("Age", choices=[
        ('baby', 'Baby'),
        ('young', 'Young'),
        ('adult', 'Adult'),
        ('senior', 'Senior')])

    notes = TextAreaField("Notes")

    # not in form! available = BooleanField("Available?")
