#!/usr/bin/python

from config import config
from configparser import ConfigParser

from psycopg2 import Error
import psycopg2

"""
https://www.postgresqltutorial.com/postgresql-python/connect/
https://pynative.com/python-postgresql-tutorial/
"""
class PostgreIO:

    def __init__(self, cfg):
        self.cfg = cfg
        self.user = cfg['user']
        self.password = cfg['password']
        self.host = cfg['host']
        self.port = cfg['port']
        self.database = cfg['database']

    def connect(self):
        """
        method get conn, cursor
        """
        try:
            conn = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.password,
                port=self.port,
                database=self.password
                )
            cursor = conn.cursor()
            return conn, cursor
        except Exception as e:
            print ("Error while connecting to postgre", e)

    def run_sql(self, query):
        """
        method simply execute sql command
        """
        try:
            conn, cursor = self.connect()
            print (query)
            cursor.execute(query)
            conn.commit()
            print ("query OK")
        except Exception as e:
            print ("query failed", e)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def create_table(self, schema, query):
        pass

    def insert_to_db(self, query):
        pass

    def query_sql(self, query):
        results = []
        try:
            conn, cursor = self.connect()
            print (query)
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                results.append(row)
            print ("query sql OK")
            return results
        except Exception as e:
            print ("query sql failed", e)
        finally:
            if conn:
                cursor.close()
                conn.close()