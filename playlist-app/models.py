"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(30))
    description = db.Column(db.Text)

    songs = db.relationship('Song',
                            secondary='playlists_songs',
                            backref='playlists')

    @classmethod
    def addPlaylist(self, name, desc):
        """Add playlist to DB"""
        playlist = Playlist(name=name, description=desc)
        
        db.session.add(playlist)
        db.session.commit()

class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(50))
    artist = db.Column(db.String(50))

    @classmethod
    def addSong(self, title, artist):
        """Add playlist to DB"""
        song = Song(title=title, artist=artist)
        
        db.session.add(song)
        db.session.commit()


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    playlist_id = db.Column(db.Integer,
                    db.ForeignKey('playlists.id'),
                    nullable=True)
    song_id = db.Column(db.Integer,
                    db.ForeignKey('songs.id'),
                    nullable=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
