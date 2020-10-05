import database_functions

## this module handles the user inputs and returns the data along with some validation 


def choice_one():
    
    name = input('Enter artist name: ')
    email = input('Enter artist email: ')

    if name == '' or email == '':
        print('Please provide name or email')
        return None

    return name, email

def choice_two(): 
    artist = input('Enter artist name: ')
    #validation for checking if an artist is in the database_functions
    if database_functions.does_artist_exist(artist):
        artwork = input('Enter art piece name: ')
        price = int(input('(integers only) Enter price: '))
        status = input('(available or sold) Enter status:  ')

        return artist, artwork, price, status
    else:
        print('artist not in database_functions')
        
        

def get_artist_name():
    artist = input('Enter artist name: ')
    if database_functions.does_artist_exist(artist):
        return artist
    else:
        print('artist not in database')
        

def choice_six():
    art = int(input('Enter art piece id: '))
    #input validation to makesure user doesnt type in random words for the availability
    while True:
        new_status = input('New status of artwork (available or sold): ')
        if new_status.strip() == 'avaiable' or new_status.strip() == 'sold':
            break
        else:
            print('must be \"available\" or \"sold\" ')

    return art, new_status

def get_artwork_id():
    #grabs id 
    art = int(input('Enter art piece id to be delete: '))    
    return art
      
    