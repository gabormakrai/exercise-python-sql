
from sqlalchemy import Column, Integer, Table, Text
from sqlalchemy.ext.declarative import declarative_base

from src.utils import get_element_or_none

Base = declarative_base()


class Tag(Base):
    __tablename__ = 'tag'

    id = Column('Id', Integer, primary_key=True)
    tag_name = Column('TagName', Text)
    count = Column('Count', Integer)
    excerpt_post_id = Column('ExcerptPostId', Integer)
    wiki_post_id = Column('WikiPostId', Integer)

    @staticmethod
    def create_table(metadata_obj):
        return Table(
            "tag",
            metadata_obj,
            Column('Id', Integer),
            Column('TagName', Text),
            Column('Count', Integer),
            Column('ExcerptPostId', Integer),
            Column('WikiPostId', Integer)
        )

    @staticmethod
    def create_from_xml_element_data(data):
        try:
            return Tag(
                id=get_element_or_none(data, 'Id', int),
                tag_name=get_element_or_none(data, 'TagName', str),
                count=get_element_or_none(data, 'Count', int),
                excerpt_post_id=get_element_or_none(data, 'ExcerptPostId', int),
                wiki_post_id=get_element_or_none(data, 'WikiPostId', int)
            )
        except ValueError:
            return None
