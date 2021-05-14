from sqlite3 import Connection as SQLite3Connection
from flask import Flask, request, jsonify
from datetime import datatime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

# app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQL_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key constraints


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datatime.now()

#  models


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(50))
    email = db.column(db.String(50))
    address = db.column(db.String(200))
    phone = db.column(db.String(50))
    posts = db.relationship("Blogpost")
