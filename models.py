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
        nullable=False  # can't be unknown, a.k.a. required
    )

    species = db.mapped_column(
        # to fill in
        db.String(75),
        nullable=False
    )

    photo_url = db.mapped_column(
        db.String(200),  # TODO: where do I make it '' if not provided?
        nullable=False
    )

    age = db.mapped_column(
        # to fill in
        db.Text  # FIXME: check how to pick from provided options,
    )

    notes = db.mapped_column(
        db.Text
        # TODO: confirm that nullable=True is implicit default
    )

    available = db.mapped_column(
        # to fill in
        db.Boolean,
        nullable=False
        # TODO: add default to available
    )
