from sqlalchemy import MetaData, create_engine

from src.post import Post
from src.tag import Tag


def create_tags_and_posts_table(engine):
    metadata_obj = MetaData()
    Tag.create_table(metadata_obj)
    Post.create_table(metadata_obj)
    metadata_obj.create_all(engine)


def create_sqlalchemy_engine(file_path):
    return create_engine(f"sqlite+pysqlite:///{file_path}", future=True)

