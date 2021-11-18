from sqlalchemy.orm import Session

from db import create_sqlalchemy_engine, create_tags_and_posts_table
from post import Post
from test_helper import MockXmlData


def test_insert_with_sqlalchemy():
    sqlalchemy_engine = create_sqlalchemy_engine("")
    create_tags_and_posts_table(sqlalchemy_engine, create_tag_table=False)
    example_post = Post(
        id=1,
        post_type_id=2,
        accepted_answer_is=3,
        creation_date='date1',
        score=4,
        view_count=5,
        body='body1',
        owner_user_id=6,
        last_editor_user_id=7,
        last_edit_date='date2',
        last_activity_date='date3',
        title='title1',
        tags='tags1',
        answer_count=8,
        comment_count=9,
        favorite_count=10,
        content_license='license1')
    with Session(sqlalchemy_engine) as session:
        session.add(example_post)
        session.commit()

    connection = sqlalchemy_engine.raw_connection()
    cursor = connection.cursor()
    assert list(cursor.execute('select * from post')) == [(1, 2, 3, 'date1', 4, 5, 'body1', 6, 7, 'date2', 'date3', 'title1', 'tags1', 8, 9, 10, 'license1')]


def test_post_creation_happy_path():
    value = Post.create_from_xml_element_data(MockXmlData({
        'Id': '1',
        'PostTypeId': '2',
        'AcceptedAnswerId': '3',
        'CreationDate': 'date1',
        'Score': '4',
        'ViewCount': '5',
        'Body': 'body1',
        'OwnerUserId': '6',
        'LastEditorUserId': '7',
        'LastEditDate': 'date2',
        'LastActivityDate': 'date3',
        'Title': 'title1',
        'Tags': 'tags1',
        'AnswerCount': '8',
        'CommentCount': '9',
        'FavoriteCount': '10',
        'ContentLicense': 'license1'
    }))
    assert value.id == 1
    assert value.post_type_id == 2
    assert value.accepted_answer_is == 3
    assert value.creation_date == 'date1'
    assert value.score == 4
    assert value.view_count == 5
    assert value.body == 'body1'
    assert value.owner_user_id == 6
    assert value.last_editor_user_id == 7
    assert value.last_edit_date == 'date2'
    assert value.last_activity_date == 'date3'
    assert value.title == 'title1'
    assert value.tags == 'tags1'
    assert value.answer_count == 8
    assert value.comment_count == 9
    assert value.favorite_count == 10
    assert value.content_license == 'license1'


def test_post_creation_one_field_missing():
    value = Post.create_from_xml_element_data(MockXmlData({
        'Id': '1',
        'PostTypeId': '2',
        'AcceptedAnswerId': '3',
        'CreationDate': 'date1',
        'Score': '4',
        'ViewCount': '5',
        'Body': 'body1',
        'LastEditorUserId': '7',
        'LastEditDate': 'date2',
        'LastActivityDate': 'date3',
        'Title': 'title1',
        'Tags': 'tags1',
        'AnswerCount': '8',
        'CommentCount': '9',
        'FavoriteCount': '10',
        'ContentLicense': 'license1'
    }))
    assert value.id == 1
    assert value.post_type_id == 2
    assert value.accepted_answer_is == 3
    assert value.creation_date == 'date1'
    assert value.score == 4
    assert value.view_count == 5
    assert value.body == 'body1'
    assert not value.owner_user_id
    assert value.last_editor_user_id == 7
    assert value.last_edit_date == 'date2'
    assert value.last_activity_date == 'date3'
    assert value.title == 'title1'
    assert value.tags == 'tags1'
    assert value.answer_count == 8
    assert value.comment_count == 9
    assert value.favorite_count == 10
    assert value.content_license == 'license1'


def test_post_creation_one_field_is_incorrect():
    value = Post.create_from_xml_element_data(MockXmlData({
        'Id': 'not_a_number',
        'PostTypeId': '2',
        'AcceptedAnswerId': '3',
        'CreationDate': 'date1',
        'Score': '4',
        'ViewCount': '5',
        'Body': 'body1',
        'LastEditorUserId': '7',
        'LastEditDate': 'date2',
        'LastActivityDate': 'date3',
        'Title': 'title1',
        'Tags': 'tags1',
        'AnswerCount': '8',
        'CommentCount': '9',
        'FavoriteCount': '10',
        'ContentLicense': 'license1'
    }))
    assert not value
