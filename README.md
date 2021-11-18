## Exercise Instructions

This is a bootstrap project to load interesting data from a Stack Exchange dataset into a data warehouse.
You are free to change anything about this bootstrap solution as you see fit, so long as it can still be executed by a reviewer.

- The project is set up to use Pipenv & Python 3.8
- SQLite3 provides an infrastructure-free simple data warehouse stand-in
- Facilites for linting etc. are provided as scripts and integrated with Pipenv

[scripts/fetch_data.sh](scripts/fetch_data.sh) is provided to download and decompress the dataset.

Your task is to make the Posts and Tags content available in an SQLite3 database.
[src/main.py](src/main.py) is provided as an entrypoint, and has an example of parsing the source data.
[src/db.py](src/db.py) is empty, but the associated test demonstrates interaction with an SQLite3 database.
You should ensure your code is correctly formatted and lints cleanly.

You will aim to make it convenient for data scientists to execute analytics-style queries reliably over the Posts and Tags tables.
You will be asked to demonstrate the solution, including:
- how you met the data scientist needs
- how you did (or would) ensure data quality
- what would need to change for the solution scale to work with a 10TB dataset with new data arriving each day

## My Solution

### Main

I completely rewrote `main.py` to have a user-friendly command line interface. I am using `argparse` ([link](https://docs.python.org/3/library/argparse.html))  to parse command
line arguments.

For usage:
```
python3 main.py -h
```

This will give the following output
```
usage: main.py [-h] --posts-file POSTS_FILE --tags-file TAGS_FILE
               --output-db-file OUTPUT_DB_FILE
               [--delete-output-db-file-if-exists]

optional arguments:
  -h, --help            show this help message and exit
  --posts-file POSTS_FILE
                        File that contains the Posts xml data
  --tags-file TAGS_FILE
                        File that contains the Tags xml data
  --output-db-file OUTPUT_DB_FILE
                        Sqlite db file to write the data
  --delete-output-db-file-if-exists
                        Delete the output db file if it exists
```

### SqlAlchemy

The solution is using SQLAlchemy ([link](https://www.sqlalchemy.org/)) for database operations. The application will create the tables and create the insert calls via SQLAlchemy safely, so I don't need to worry about sql injection problems.

### Data quality

There are simple checks for the Tag and Post entries. Id/counters/numbers are checked whether they can be converted into `int`. There are no checks on dates (that is one possible improvement).

### Possible improvements / next steps

This solution doesn't create nicely indexed / partitioned tables. Indexing is certainly possible in Sqlite which could help the analysts to run their queries faster. Partitioning is not possible in Sqlite, but would be beneficial for other database technologies to speed up the queries for the analysts.  

Also, testing can be further improved by parametrized tests. (Additionally, moving out the test python files to a separate directory would be nice to avoid having one large directory)
