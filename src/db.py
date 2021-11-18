from sqlalchemy import MetaData, create_engine

from post import Post
from tag import Tag


def create_tags_and_posts_table(engine, create_tag_table=True, create_post_table=True):
    metadata_obj = MetaData()
    if create_tag_table:
        Tag.create_table(metadata_obj)
    if create_post_table:
        Post.create_table(metadata_obj)
    metadata_obj.create_all(engine)


def create_sqlalchemy_engine(file_path):
    return create_engine(f"sqlite+pysqlite:///{file_path}", future=True)

