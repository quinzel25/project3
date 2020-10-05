import database_functions
import ui


def menu():

    print('Menu: ')
    print('1. Add New Artist')
    print('2. Add New Art Piece')
    print('3. View All Artists')
    print('4. View All Art by Artist')
    print('5. View All Available Art by Artist')
    print('6. Change Availability of Art Piece by ID')
    print('7. Delete Artwork by ID')
    print('8. Quit')


def main():

    menu()
    choice = int(input('Enter choice: '))
    #menu will loop until user hits quit
    while choice != 8:
        if choice == 1:
            try:
                name, email = ui.choice_one()
                database_functions.add_artist(name, email)
            except:
                # if name OR email is blank it returns None which throws the exception
                print('')
        elif choice == 2:
            try:
                artist, artwork, price, status = ui.choice_two()
                database_functions.add_art(artist, artwork, price, status)
            except:
                #if this function fails its due to artist not being found in database_functions
                print('')
        elif choice == 3:
            database_functions.view_all_artists()
        elif choice == 4:
            name = ui.get_artist_name()
            database_functions.all_art_by_artist(name)
        elif choice == 5:
            name = ui.get_artist_name()
            database_functions.all_available_art(name)
        elif choice == 6:
            art_id, status = ui.choice_six()
            database_functions.change_availability(art_id, status)
        elif choice == 7:
            art = ui.get_artwork_id()
            database_functions.delete_artwork(art)
        else:
            print('Invalid choice')
        print()
        menu()
        choice = int(input('Enter choice: '))

    print('Have a nice day! :)')

if __name__ == '__main__':
    main()