from sqlalchemy.orm import Session

from db import create_sqlalchemy_engine, create_tags_and_posts_table
from test_helper import MockXmlData
from tag import Tag


def test_insert_with_sqlalchemy():
    sqlalchemy_engine = create_sqlalchemy_engine("")
    create_tags_and_posts_table(sqlalchemy_engine, create_post_table=False)
    example_tag = Tag(id=1, tag_name='value1', count=None, excerpt_post_id=5, wiki_post_id=111)
    with Session(sqlalchemy_engine) as session:
        session.add(example_tag)
        session.commit()

    connection = sqlalchemy_engine.raw_connection()
    cursor = connection.cursor()
    assert list(cursor.execute('select * from tag')) == [(1, 'value1', None, 5, 111)]


def test_tag_creation_happy_path():
    value = Tag.create_from_xml_element_data(MockXmlData({
        'Id': '1',
        'TagName': 'value1',
        'Count': '55',
        'ExcerptPostId': '12',
        'WikiPostId': '5'
    }))
    assert value.id == 1
    assert value.tag_name == 'value1'
    assert value.count == 55
    assert value.excerpt_post_id == 12
    assert value.wiki_post_id == 5


def test_tag_creation_one_field_missing():
    value = Tag.create_from_xml_element_data(MockXmlData({
        'Id': '1',
        'TagName': 'value1',
        'ExcerptPostId': '12',
        'WikiPostId': '5'
    }))
    assert value.id == 1
    assert value.tag_name == 'value1'
    assert not value.count
    assert value.excerpt_post_id == 12
    assert value.wiki_post_id == 5


def test_tag_creation_one_field_is_incorrect():
    value = Tag.create_from_xml_element_data(MockXmlData({
            'Id': '1',
            'TagName': 'value1',
            'ExcerptPostId': 'not_a_number',
            'WikiPostId': '5'
    }))
    assert not value
