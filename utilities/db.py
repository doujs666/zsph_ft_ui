import pymysql.cursors
import settings


def execute(sql, params=None, db='credit_test', is_fetchone=True):
    # Connect to the database
    connection = pymysql.connect(host=settings.DB_CONFIG['HOST'],
                                 user=settings.DB_CONFIG['USER'],
                                 password=settings.DB_CONFIG['PASSWORD'],
                                 db=db,
                                 autocommit=True,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            if is_fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
    finally:
        connection.close()
