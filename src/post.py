
from sqlalchemy import Column, Integer, Table, Text
from sqlalchemy.ext.declarative import declarative_base

from utils import get_element_or_none

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'

    id = Column('Id', Integer, primary_key=True)
    post_type_id = Column('PostTypeId', Integer)
    accepted_answer_is = Column('AcceptedAnswerId', Integer)
    creation_date = Column('CreationDate', Text)
    score = Column('Score', Integer)
    view_count = Column('ViewCount', Integer)
    body = Column('Body', Text)
    owner_user_id = Column('OwnerUserId', Integer)
    last_editor_user_id = Column('LastEditorUserId', Integer)
    last_edit_date = Column('LastEditDate', Text)
    last_activity_date = Column('LastActivityDate', Text)
    title = Column('Title', Text)
    tags = Column('Tags', Text)
    answer_count = Column('AnswerCount', Integer)
    comment_count = Column('CommentCount', Integer)
    favorite_count = Column('FavoriteCount', Integer)
    content_license = Column('ContentLicense', Text)

    @staticmethod
    def create_table(metadata_obj):
        return Table(
            "post",
            metadata_obj,
            Column('Id', Integer),
            Column('PostTypeId', Integer),
            Column('AcceptedAnswerId', Integer),
            Column('CreationDate', Text),
            Column('Score', Integer),
            Column('ViewCount', Integer),
            Column('Body', Text),
            Column('OwnerUserId', Integer),
            Column('LastEditorUserId', Integer),
            Column('LastEditDate', Text),
            Column('LastActivityDate', Text),
            Column('Title', Text),
            Column('Tags', Text),
            Column('AnswerCount', Integer),
            Column('CommentCount', Integer),
            Column('FavoriteCount', Integer),
            Column('ContentLicense', Text)
        )

    @staticmethod
    def create_from_xml_element_data(data):
        try:
            return Post(
                id=get_element_or_none(data, 'Id', int),
                post_type_id=get_element_or_none(data, 'PostTypeId', int),
                accepted_answer_is=get_element_or_none(data, 'AcceptedAnswerId', int),
                creation_date=get_element_or_none(data, 'CreationDate', str),
                score=get_element_or_none(data, 'Score', int),
                view_count=get_element_or_none(data, 'ViewCount', int),
                body=get_element_or_none(data, 'Body', str),
                owner_user_id=get_element_or_none(data, 'OwnerUserId', int),
                last_editor_user_id=get_element_or_none(data, 'LastEditorUserId', int),
                last_edit_date=get_element_or_none(data, 'LastEditDate', str),
                last_activity_date=get_element_or_none(data, 'LastActivityDate', str),
                title=get_element_or_none(data, 'Title', str),
                tags=get_element_or_none(data, 'Tags', str),
                answer_count=get_element_or_none(data, 'AnswerCount', int),
                comment_count=get_element_or_none(data, 'CommentCount', int),
                favorite_count=get_element_or_none(data, 'FavoriteCount', int),
                content_license=get_element_or_none(data, 'ContentLicense', str)
            )
        except ValueError:
            return None
