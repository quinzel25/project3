from peewee import *
from database_config import database_path
#this creates the two tables and the database
db = SqliteDatabase(database_path)

class Artist(Model):
    artistID = AutoField()
    name = CharField(unique= True)
    email = CharField(unique= True)
    
    class Meta:
        database = db

class Artwork(Model):
    artwork_id = AutoField()
    artist_id = ForeignKeyField(Artist, backref= 'artistID')
    artist = CharField()
    artName = CharField()
    price = IntegerField()
    status = CharField(default='available')

    class Meta:
        database = db

db.connect()
db.create_tables([Artist, Artwork])







