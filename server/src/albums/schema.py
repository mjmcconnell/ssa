# third-party imports
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

# local imports
from albums.models import AlbumModel, ImageModel


class AlbumSchema(SQLAlchemyObjectType):
    class Meta:
        model = AlbumModel
        interfaces = (relay.Node,)


class ImageSchema(SQLAlchemyObjectType):
    class Meta:
        model = ImageModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_albums = SQLAlchemyConnectionField(AlbumSchema.connection)
    all_images = SQLAlchemyConnectionField(ImageSchema.connection)


schema = graphene.Schema(query=Query)
