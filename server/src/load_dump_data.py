#!/opt/app-root/bin/python

from albums.models import AlbumModel, ImageModel
from core.models import ModelBase, db_session, engine

ModelBase.metadata.create_all(bind=engine)

# create albums
foo = AlbumModel(name="Foo")
db_session.add(foo)
bar = AlbumModel(name="Bar")
db_session.add(bar)

# add images to album
first = ImageModel(name="Image 1", album=foo)
db_session.add(first)
second = ImageModel(name="Image 2", album=foo)
db_session.add(second)

db_session.commit()
