import database
import ui


def menu():
    print('Menu: ')
    print('1. Add New Artist')
    print('2. Add New Art Piece')
    print('3. View All Artists')
    print('4. View All Art by Artist')
    print('5. View All Available Art by Artist')
    print('6. Change Availability of Art Piece')
    print('7. Quit')


def main():

    menu()
    choice = int(input('Enter choice: '))

    while choice != 7:
        if choice == 1:
            try:
                name, email = ui.choice_one()
                database.add_artist(name, email)
            except:
                # if name OR email is blank it returns None which throws the exception
                print('')
        elif choice == 2:
            try:
                artist, artwork, price, status = ui.choice_two()
                database.add_art(artist, artwork, price, status)
            except:
                #if this function fails its due to artist not being found in database
                print('')
        elif choice == 3:
            database.view_all_artists()
        elif choice == 4:
            name = ui.get_artist_name()
            database.all_art_by_artist(name)
        elif choice == 5:
            name = ui.get_artist_name()
            database.all_available_art(name)
        elif choice == 6:
            art_id, status = ui.choice_six()
            database.change_availability(art_id, status)
        else:
            print('Invalid choice')
        print()
        menu()
        choice = int(input('Enter choice: '))

    print('Have a nice day! :)')

if __name__ == '__main__':
    main()