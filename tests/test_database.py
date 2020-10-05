from unittest import TestCase
from peewee import * 


from database import Artist, Artwork
import database_functions
import database_config
database_config.database_path = 'database/test_art.db'

class TestBookstore(TestCase):

    def setUp(self):
        #clears test db and declares path
        database_config.database_path = 'database/test_art.db'
        self.clear_db()

    def add_test_data(self):
        #adds artists

        self.clear_db()
        self.ar1 = Artist(artistID= AutoField, name = 'frank', email= 'frank@gmail.com')
        self.ar2 = Artist(artistID= AutoField, name = 'erik', email= 'erik@gmail.com')
        self.ar3 = Artist(artistID= AutoField, name = 'matt', email= 'matt@gmail.com')

        self.ar1.save()
        self.ar2.save()
        self.ar3.save()

        #add artworks

        self.aw1 = Artwork(artist='frank', artName='Sunshine', price=321,status='available', artist_id= 1)
        self.aw2 = Artwork(artist='frank', artName='Moonlight', price=123,status='sold', artist_id= 1)

        self.aw3 = Artwork(artist='erik', artName='Windy', price=456,status='available', artist_id= 2)
        self.aw4 = Artwork(artist='matt', artName='Brisk', price=777,status='available', artist_id= 3)

        self.aw1.save()
        self.aw2.save()
        self.aw3.save()
        self.aw4.save()

    def clear_db(self):
        #clears db
        database_functions.delete_everything()

    def test_does_artist_exist(self):

        self.add_test_data()
        ## makes sure that artist checking is functional
        self.assertTrue(database_functions.does_artist_exist('frank'))

    def test_add_artist(self):
        test = Artist(artistID = AutoField, name= 'test', email= 'test@gmail.com')
        test.save()
        self.assertTrue(database_functions.exact_match_artist(test))

    def test_add_artwork(self):
        self.add_test_data
        test = Artwork(artist='frank', artName='artwork', price=123,status='sold', artist_id= 1)
        test.save
        self.assertTrue(database_functions.exact_match_artwork(test))


