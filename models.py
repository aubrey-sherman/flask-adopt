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
            # SINGLE QUOTES FOR SQL
            "age IN " + "('baby', 'young', 'adult', 'senior')"),
        nullable=False
    )

    notes = db.mapped_column(
        db.Text,
        nullable=True  # FIXME: make nullable=False, empty string as default
    )

    available = db.mapped_column(
        db.Boolean,
        nullable=False,
        default=True
    )
