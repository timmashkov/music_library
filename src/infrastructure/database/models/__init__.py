from .album import Album
from .artist import Artist
from .base import Base
from .genre import Genre
from .track import Track

__all__: tuple[str] = ("Base", "Artist", "Album", "Track", "Genre")
