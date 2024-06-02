import logging
from psycopg2 import DatabaseError

from connect import create_connection


def create_table(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
     id integer PRIMARY KEY,
     name text NOT NULL,
     begin_date text,
     end_date text
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_projects_table)
            # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")
