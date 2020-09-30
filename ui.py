import database

def choice_one():

    name = input('Enter artist name: ')
    email = input('Enter artist email: ')

    return name, email

def choice_two(): 
    artist = input('Enter artist name: ')
    if database.does_artist_exist(artist):
        artwork = input('Enter art piece name: ')
        price = input('Enter price: (integers only)')
        status = input('Enter status: (available or sold)')

        return artist, artwork, price, status
    else:
        print('artist not in database')
        
####View All Art by Artist
#5. View All Available Art by Artist
#6. Change Availability of Art Piece

def get_artist_name():
    artist = input('Enter artist name: ')
    if database.does_artist_exist(artist):
        return artist
    else:
        print('artist not in database')

def choice_six():
    art = int(input('Enter art piece id: '))
    new_status = input('New status of artwork (available or sold): ')

    return art, new_status