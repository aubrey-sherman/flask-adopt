"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
dbx = db.session.execute


class Pet(db.Model):
    """ Potentially adoptable pet. """

    __tablename__ = "pets"

    id = db.mapped_column(
        db.Integer,
        db.Identity(),
        primary_key=True
    )

    name = db.mapped_column(
        db.String(75),
        nullable=False
    )

    species = db.mapped_column(
        db.String(75),
        nullable=False
    )

    photo_url = db.mapped_column(
        db.Text,
        nullable=False,
        default=""
    )

    age = db.mapped_column(
        db.Text,
        db.CheckConstraint(
            "age IN " + "('baby', 'young', 'adult', 'senior')"),
        nullable=False
    )

    notes = db.mapped_column(
        db.Text
        # TODO: confirm that nullable=True is implicit default
    )

    available = db.mapped_column(
        db.Boolean,
        nullable=False,
        default="available"
    )
