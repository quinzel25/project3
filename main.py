import database



# def add_new_holder():
#     nameInput = input('Enter Holder\'s name: ')
#     countryInput = input('Enter Holder\'s country: ' )
#     catches = input('Enter Holder\'s amount of catches: ')

#     add = Catches(name=nameInput, country=countryInput, num_of_catches=catches)
#     add.save

#     print(f'{nameInput} has been entered into the database')

def main():
    
    database.add_artist('test', 'test@gmail.com')
    



if __name__ == '__main__':
    main()