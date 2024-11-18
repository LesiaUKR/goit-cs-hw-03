import psycopg2
from contextlib import contextmanager
from config import DB_CONFIG

@contextmanager
def connect():
   try:
       conn = psycopg2.connect(**DB_CONFIG)
       try:
          yield conn
       finally:
          conn.close()
   except  psycopg2.OperationalError:
      print("Connection failed")