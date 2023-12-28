# third-party imports
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, backref

# local imports
from core.models import ModelBase


class AlbumModel(ModelBase):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class ImageModel(ModelBase):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())
    album_id = Column(Integer, ForeignKey("album.id"))
    album = relationship(
        AlbumModel, backref=backref("images", uselist=True, cascade="delete,all")
    )
