'Entrypoint to populate the database'

import argparse
import logging

from sqlalchemy.orm import Session

from db import create_sqlalchemy_engine, create_tags_and_posts_table
from post import Post
from tag import Tag
from utils import delete_file_if_exists, file_exists
from xml_reader import read_xml_file_and_call_method

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
LOGGER = logging.getLogger(__name__)


def stream_data_to_sqlite_db(posts_file_path, tags_file_path, output_db_file_path, delete_if_exists):

    LOGGER.info("Application setup")
    LOGGER.info("Input Tags file: %s", tags_file_path)
    LOGGER.info("Input Posts file: %s", posts_file_path)
    LOGGER.info("Output DB file: %s", output_db_file_path)

    if delete_if_exists:
        LOGGER.info("Deleting output db file if it exists")
        delete_file_if_exists(output_db_file_path)

    if file_exists(output_db_file_path):
        LOGGER.error(
            "Output db file exists, please run with --delete-output-db-file-if-exists or delete the file")
        return

    LOGGER.info("Creating database")
    sqlalchemy_engine = create_sqlalchemy_engine(output_db_file_path)
    create_tags_and_posts_table(sqlalchemy_engine)

    LOGGER.info("Streaming Tags")
    with Session(sqlalchemy_engine) as session:

        def process_tag_data(xml_data):
            tag = Tag.create_from_xml_element_data(xml_data)
            if not tag:
                LOGGER.error("Couldn't create Tag from %s", xml_data)
                return
            session.add(tag)

        read_xml_file_and_call_method(tags_file_path, process_tag_data)
        session.commit()

    LOGGER.info("Streaming Posts")
    with Session(sqlalchemy_engine) as session:

        def process_post_data(xml_data):
            post = Post.create_from_xml_element_data(xml_data)
            if not post:
                LOGGER.error("Couldn't create Post from %s", xml_data)
                return
            session.add(post)

        read_xml_file_and_call_method(posts_file_path, process_post_data)
        session.commit()

    LOGGER.info("Exit")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--posts-file', required=True,
                        help='File that contains the Posts xml data')
    parser.add_argument('--tags-file', required=True,
                        help='File that contains the Tags xml data')
    parser.add_argument('--output-db-file', required=True,
                        help='Sqlite db file to write the data')
    parser.add_argument(
        '--delete-output-db-file-if-exists',
        action='store_true',
        help='Delete the output db file if it exists')

    args = parser.parse_args()

    stream_data_to_sqlite_db(
        args.posts_file,
        args.tags_file,
        args.output_db_file,
        args.delete_output_db_file_if_exists
    )


if __name__ == "__main__":
    main()
