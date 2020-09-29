from peewee import *

db = SqliteDatabase('art.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()
    

    class Meta:
        database = db

class Artwork(Model):
    artwork_id = AutoField()
    artist_id = ForeignKeyField(Artist, backref= 'artist_id')
    artist = CharField()
    artName = CharField()
    price = IntegerField()
    status = CharField(default='available')

    class Meta:
        database = db

db.connect()
db.create_tables([Artist, Artwork])


### Functions for database


def add_artist(name_input, email_input):
    try:
        name_input = name_input.lower()
        email_input = email_input.lower()
        Artist.create(name=name_input, email=email_input)
        
        print(f'{name_input.capitalize()} has been added into the Artist db')
    except:
        print('Error adding artist')

def add_art(artist, artwork, price, status):

    try:
        Artwork.create(artist=artist, artName=artwork, price=price,status=status)

        print(f'{artwork.capitalize()} added for {artist.capitalize()}')
    except:
        print('Error adding artpeice')


def does_artist_exist(name):
    ###checks 
    name = name.lower()

    search = Artist.select().where(Artist.name == name)

    if search:
        return True
    else:
        return False

def change_availability(art_id, new_status):

    try:
        change = Artwork.update(status=new_status).where(Artwork.artwork_id == art_id)
        change.execute

        print(f'Status changed to {new_status}')
    except:
        print('Error changing status')

def all_art_by_artist(name):

    pass






