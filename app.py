"""Flask app for adopt app."""

import os

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, dbx, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SECRET_KEY'] = "secret"
db.init_app(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def show_homepage():
    """ List all pets."""

    q = db.select(Pet).order_by(Pet.species, Pet.age)
    # first shows as groups by species, within will sort by age

    # save data as scalar values, i.e. pet instances
    pets = dbx(q).scalars().all()

    # pass to jinja template to render on page
    return render_template("index.jinja", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Form for adding a pet; handle adding."""

    # make instance of pet form
    form = AddPetForm()

    # validate the form
    if form.validate_on_submit():  # returns boolean
        # create the new pet; #TODO: is there a more concise way?
        new_pet = Pet(
            name=request.form['name'],
            species=request.form['species'],
            photo_url=request.form['photo_url'],
            age=request.form['age'],
            notes=request.form['notes']
        )

        db.session.add(new_pet)
        db.session.commit()

        # confirm add to user and redirect to homepage
        flash("Your ador*aub*le pet has been added!")
        return redirect("/")

    # if validation fails, re-render the form
    else:
        return render_template("add_pet_form.jinja", form=form)
