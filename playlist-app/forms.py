"""Forms for playlist app."""

from tokenize import String
from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional, Length, URL


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name",
                        validators=[InputRequired(message="Playlist must have a name")])
    description = TextAreaField("Description",
                        validators=[Optional()])

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title",
                        validators=[InputRequired(message="Song must have a name")])
    artist = StringField("Artist Name",
                        validators=[InputRequired(message="Song must have an artist")])

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
