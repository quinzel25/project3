import database




def main():
    
    database.add_artist('test', 'test@gmail.com')
    database.all_art_by_artist('test')



if __name__ == '__main__':
    main()