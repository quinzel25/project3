from peewee import *
import ui

from database import Artist, Artwork
### Functions for database

### this module handles the queries into and from the database

def add_artist(name_input, email_input):
    try:
        name_input = name_input.lower()
        email_input = email_input.lower()
        Artist.create(name=name_input, email=email_input, artistID = AutoField)
        
        print(f'{name_input} has been added into the Artist database')
    except:
        print('Error adding artist')

def add_art(artist_input, artwork, price_input, status_input):

    try:
      
        artist_get_id = Artist.get(Artist.name == artist_input).artistID
        
        artist_get_id = int(artist_get_id)
        Artwork.create( artist=artist_input, artName=artwork, price=price_input,status=status_input, artist_id= artist_get_id)

        print(f'{artwork} added for {artist_input}')
    except:
        print('Error adding artpeice' )

def does_artist_exist(name):
    ###checks to see if artist is in database, returns a boolean
    name = name.lower()

    search = Artist.select().where(Artist.name == name)

    if search:
        return True
    else:
        return False

def view_all_artists():
    
    query = Artist.select()
    
    for x in query:
        print(f'Artist: {x.name} | Email: {x.email} | Artist ID: {x.artistID}')


def change_availability(art_id, new_status):

    try:
        new_status = new_status.lower().strip()
        change = Artwork.update(status=new_status).where(Artwork.artwork_id == art_id)
        change.execute()

        print(f'Status changed to {new_status}')
    except:
        print('Error changing status')

def all_art_by_artist(name):
    try:
        artist_id = get_artist_id(name)
        name = name.lower()
        query = Artwork.select().where(Artwork.artist_id == artist_id)
      
        print(f'All artwork from {name}: \n')
        for x in query:
            print(f'Art ID: {x.artwork_id} | Art name: {x.artName} | price: ${x.price} | Status: {x.status} ')
    except:
       print('Error retrieving art')

def all_available_art(name):
    try:
       
        artist_id = get_artist_id(name)
        name = name.lower()
        query = Artwork.select().where(Artwork.artist_id == artist_id, Artwork.status == 'available')

        print(f'All available artwork from {name} : \n')
        for x in query:
            print(f'Art ID: {x.artwork_id} | Art name: {x.artName} | price: ${x.price} | Status: {x.status} ')
    except:
        print('Error retrieving art')

def get_artist_id(artist_input):

    artist_get_id = Artist.get(Artist.name == artist_input).artistID
    artist_get_id = int(artist_get_id)
    return artist_get_id
        
def delete_everything():
    Artwork.delete().where(Artwork.artwork_id >= 1).execute()
    Artwork.delete().where(Artist.artistID >=1).execute()

    

def delete_artwork(id_input):
    try:
        query = Artwork.delete().where(Artwork.artwork_id == id_input)
        query.execute()
        print('Artwork deleted')
    except:
        print('Error deleting artwork')

# functions for testing

def exact_match_artist(artist):
    search = Artist.get_or_none( (Artist.artistID == artist.artistID) & (Artist.name == artist.name) & (Artist.email == artist.name))
    return search is not None 

def exact_match_artwork(artwork):
    search = Artwork.get_or_none( (Artwork.artwork_id == artwork.artwork_id) & (Artwork.artName == artwork.name) & (Artwork.price == artwork.price) & (Artwork.status == artwork.status) & (Artwork.artist == artwork.artist))
    return search is not None 


