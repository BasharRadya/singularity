#!/usr/bin/env python3
import peewee
import config

DB = peewee.SqliteDatabase(config.database)


class BaseModel(peewee.Model):
    class Meta:
        database = DB
        strict_tables = True


class User(BaseModel):
    username = peewee.TextField(unique=True)
    pwdhash = peewee.TextField()
    student_id = peewee.TextField(unique=True, null=True)

    class Meta:
        table_name = 'users'


class Session(BaseModel):
    token = peewee.TextField(primary_key=True)
    username = peewee.TextField(unique=True)
    expiry = peewee.FloatField()

    class Meta:
        table_name = 'sessions'


class Registration(BaseModel):
    student_id = peewee.TextField(unique=True)
    username = peewee.TextField(unique=True)
    password = peewee.TextField()

    class Meta:
        table_name = 'newusers'


if __name__ == '__main__':
    DB.create_tables(BaseModel.__subclasses__())
