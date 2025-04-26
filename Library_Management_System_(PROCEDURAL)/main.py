import module as lib

# Get data from JSON file
booksData = lib.read_json('books.json')
membersData = lib.read_json('members.json')

## BOOK FUNCTIONS

#desplay data
def display_books():
    # Display the header
    print('-'*209)
    print(f"{'ID'}{" "*3}| {'Title'}{' '*65}| {'Author'}{' '*44}| {'Year'}{' '*1}| {'Genre'}{' '*10}| {'Borrowed'} | {'Borrowed To'} | {'Borrowed Date'} | {'Return Date'} |")
    #print(f"{'-'*5}|{'-'*71}|{'-'*51}|{'-'*6}|{'-'*16}|{'-'*10}|{'-'*13}|{'-'*15}|{'-'*13}|")
    # Get lenth of database
    datalen = booksData.keys()
    for i in datalen:
        id = str(i)
        title = booksData[id]['title']
        author = booksData[id]['author']
        year = str(booksData[id]['year'])
        genre = booksData[id]['genre']
        isBorrowed = booksData[id]['status']['isBorrowed']
        borrowedDate = booksData[id]['status']['borrowedDate']
        returnDate = booksData[id]['status']['returnDate']
        borrowedTo = booksData[id]['status']['borrowedTo']
        # Borrowed status
        def borrowed():
            if isBorrowed == True:
                return 'Yes'
            else:
                return 'No'
        def borrowed_to():
            if borrowedTo == None:
                return 'N/A'
            else:
                return borrowedTo
        def borrowed_date():
            if borrowedDate == None:
                return 'N/A'
            else:
                return borrowedDate
        def return_date():
            if returnDate == None:
                return 'N/A'
            else:
                return returnDate
        # Get the length of each data
        len_id = len(id)
        len_title = len(title)
        len_author = len(author)
        len_year = len(year)
        len_genre = len(genre)
        len_borrowed = len(borrowed())
        len_borrowed_to = len(borrowed_to())
        len_borrowed_date = len(borrowed_date())
        len_return_date = len(return_date())
        len_borrowed_to = len(borrowed_to())
        # Display the data
        print(f"{'-'*5}|{'-'*71}|{'-'*51}|{'-'*6}|{'-'*16}|{'-'*10}|{'-'*13}|{'-'*15}|{'-'*13}|")
        print(f'{id}{" "*(5-len_id)}| {title}{" "*(70-len_title)}| {author}{" "*(50-len_author)}| {year}{" "*(5-len_year)}| {genre}{" "*(15-len_genre)}| {borrowed()}{" "*(9-len_borrowed)}| {borrowed_to()}{" "*(12-len_borrowed_to)}| {borrowed_date()}{" "*(14-len_borrowed_date)}| {return_date()}{" "*(12-len_return_date)}|')
    print('-'*209)
# Add a new book
def add_book(title, author, year, genre):
    # Get new ID
    newId = str(len(booksData))
    # Add the new book
    booksData[newId] = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'status': {
            'isBorrowed': False,
            'borrowedTo': None,
            'borrowedDate': None,
            'returnDate': None
        }
    }
    # Add to database
    lib.write_json('books.json', booksData)
    return True
# Delete a book
def delete_book(id):
    # Check if the ID exists
    if id in booksData:
        # Delete the book
        del booksData[id]
        # Update to database
        lib.write_json('books.json', booksData)
        return True
    else:
        return False
# Borrow a book
def borrow_book(id, borrowedTo, borrowedDate, returnDate):
    # Check if the ID exists
    if id in booksData:
        # Update the status
        booksData[id]['status']['isBorrowed'] = True
        booksData[id]['status']['borrowedTo'] = borrowedTo
        booksData[id]['status']['borrowedDate'] = borrowedDate
        booksData[id]['status']['returnDate'] = returnDate
        # Update to database
        lib.write_json('books.json', booksData)
        return True
    else:
        return False
# Return a book
def return_book(id):
    # Check if the ID exists
    if id in booksData:
        # Update the status
        booksData[id]['status']['isBorrowed'] = False
        booksData[id]['status']['borrowedTo'] = None
        booksData[id]['status']['borrowedDate'] = None
        booksData[id]['status']['returnDate'] = None
        # Update to database
        lib.write_json('books.json', booksData)
        return True
    else:
        return False
# Search a book
def search_book(details):
    try:
        # Search for the book
        for i in booksData:
            if details.lower() in booksData[i]['title'].lower():
                return i
            elif details.lower() in booksData[i]['author'].lower():
                return i
            elif details.lower() in booksData[i]['year']:
                return i
            elif details.lower() in booksData[i]['genre'].lower():
                return i
        return False
    except:
        return False

## MEMBER FUNCTIONS

# Display member list
def display_members():
    # Display the header
    print('-'*201)
    print(f"{'ID'}{" "*3}| {'Name'}{' '*45}| {'NIC'}{' '*13}| {'Contact'}{' '*5}| {'Address'}{' '*40}| {'Last Borrowed Date'} | {'Last Return Date'} | {'Last Borrowed Book ID'} |")
    # Get lenth of database
    datalen = membersData.keys()
    for i in datalen:
        id = str(i)
        nic = membersData[id]['nic']
        name = membersData[id]['name']
        address = membersData[id]['address']
        contact = membersData[id]['contact']
        lastBorrowedDate = membersData[id]["status"]['lastBorrowedDate']
        lastRerunDate = membersData[id]["status"]['lastReturnDate']
        lastBorrowedBookId = membersData[id]["status"]['lastBorrowedBookId']
        # Check status
        if lastBorrowedDate == None:
            lastBorrowedDate = 'N/A'
        else:
            lastBorrowedDate = lastBorrowedDate
        if lastRerunDate == None:
            lastRerunDate = 'N/A'
        else:
            lastRerunDate = lastRerunDate
        if lastBorrowedBookId == None:
            lastBorrowedBookId = 'N/A'
        else:
            lastBorrowedBookId = lastBorrowedBookId
        # Print the data
        print(f"{'-'*5}|{'-'*50}|{'-'*17}|{'-'*13}|{'-'*48}|{'-'*20}|{'-'*18}|{'-'*23}|")
        print(f'{id}{" "*(5-len(id))}| {name}{" "*(49-len(name))}| {nic}{" "*(16-len(nic))}| {contact}{" "*(12-len(contact))}| {address}{" "*(47-len(address))}| {lastBorrowedDate}{" "*(19-len(lastBorrowedDate))}| {lastRerunDate}{" "*(17-len(lastRerunDate))}| {lastBorrowedBookId}{" "*(22-len(lastBorrowedBookId))}|')
    print('-'*201)
# Add a new member
def add_member(name, nic, contact, address):
    # Get new ID
    newId = str(len(membersData) + 1)
    # Add the new member
    membersData[newId] = {
        'name': name,
        'nic': nic,
        'contact': contact,
        'address': address,
        'status': {
            'lastBorrowedDate': None,
            'lastReturnDate': None,
            'lastBorrowedBookId': None
        }
    }
    # Add to database
    lib.write_json('members.json', membersData)
    return True
# Delete a member
def delete_member(id):
    # Check if the ID exists
    if id in membersData:
        # Delete the member
        del membersData[id]
        # Update to database
        lib.write_json('members.json', membersData)
        return True
    else:
        return False
# Update member status
def update_member_status(id, lastBorrowedDate, lastReturnDate, lastBorrowedBookId):
    # Check if the ID exists
    if id in membersData:
        # Update the status
        membersData[id]['status']['lastBorrowedDate'] = lastBorrowedDate
        membersData[id]['status']['lastReturnDate'] = lastReturnDate
        membersData[id]['status']['lastBorrowedBookId'] = lastBorrowedBookId
        # Update to database
        lib.write_json('members.json', membersData)
        return True
    else:
        return False
# Update member details
def update_member_details(id, name, nic, contact, address):
    # Check if the ID exists
    if id in membersData:
        # Update the details
        membersData[id]['name'] = name
        membersData[id]['nic'] = nic
        membersData[id]['contact'] = contact
        membersData[id]['address'] = address
        # Update to database
        lib.write_json('members.json', membersData)
        return True
    else:
        return False
# Search a member
def search_member(details):
    try:
        # Search for the member
        for i in membersData:
            if details.lower() in membersData[i]['name'].lower():
                return i
            elif details.lower() in membersData[i]['nic'].lower():
                return i
            elif details.lower() in membersData[i]['contact'].lower():
                return i
            elif details.lower() in membersData[i]['address'].lower():
                return i
        return False
    except:
        return False


## DASHBOARD FUNCTIONS

# Display the dashboard
def display_dashboard():
    # Get the number of borrowed books
    count = 0
    for i in booksData:
        if booksData[i]['status']['isBorrowed'] == True:
            count += 1
    # Display
    print(f" {'-'*49} ")
    print(f"|{' '*20}DASHBOARD{' '*20}|")
    print(f" {'-'*49} ")
    print(f"|{' '*5}1. Books - {len(booksData)}{' '*(10-len(booksData))}| {' '*8}Library{' '*9}|")
    print(f"|{' '*5}2. Members - {len(membersData)}{' '*(7-len(membersData))}|{' '*7}Manegement{' '*8}|")
    print(f"|{' '*5}3. Borrow  - {count}{' '*(5-count)}|{' '*10}System{' '*9}|")
    print(f" {'-'*49} ")
    print('\n')
    print("OPTIONS:")
    print("1 - Get Books List")
    print("2 - Add a Book")
    print("3 - Delete a Book")
    print("4 - Borrow a Book")
    print("5 - Return a Book")
    print("6 - Search a Book")
    print("7 - Get Members List")
    print("8 - Add a Member")
    print("9 - Delete a Member")
    print("10 - Update Member Status")
    print("11 - Update Member Details")
    print("12 - Search a Member")
    print("13 - Exit")

## MAIN FUNCTION

def main():
    print("Welcome to Library Management System\n")
    display_dashboard()
    input_option = input("Enter an option: ")
    # Enter option is show books
    if input_option == '1':
        lib.clear_screen()
        display_books()
        input("Press Enter to continue...")
        main()
    # Enter option is add book
    elif input_option == '2':
        lib.clear_screen()
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = input("Enter the year: ")
        genre = input("Enter the genre: ")
        add_book(title, author, year, genre)
        print("Book added successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is delete book
    elif input_option == '3':
        lib.clear_screen()
        display_books()
        id = input("Enter the ID of the book you want to delete: ")
        delete_book(id)
        print("Book deleted successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is borrow book
    elif input_option == '4':
        lib.clear_screen()
        display_books()
        id = input("Enter the ID of the book you want to borrow: ")
        borrowedTo = input("Enter the name of the person who borrowed the book: ")
        borrowedDate = input("Enter the borrowed date: ")
        returnDate = input("Enter the return date: ")
        borrow_book(id, borrowedTo, borrowedDate, returnDate)
        print("Book borrowed successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is return book
    elif input_option == '5':
        lib.clear_screen()
        display_books()
        id = input("Enter the ID of the book you want to return: ")
        return_book(id)
        print("Book returned successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is search book
    elif input_option == '6':
        lib.clear_screen()
        details = input("Enter the details you want to search: ")
        search_book(details)
        input("Press Enter to continue...")
        main()
    # Enter option is show members
    elif input_option == '7':
        lib.clear_screen()
        display_members()
        input("Press Enter to continue...")
        main()
    # Enter option is add member
    elif input_option == '8':
        lib.clear_screen()
        name = input("Enter the name: ")
        nic = input("Enter the NIC: ")
        contact = input("Enter the contact: ")
        address = input("Enter the address: ")
        add_member(name, nic, contact, address)
        print("Member added successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is delete member
    elif input_option == '9':
        lib.clear_screen()
        display_members()
        id = input("Enter the ID of the member you want to delete: ")
        delete_member(id)
        print("Member deleted successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is update member status
    elif input_option == '10':
        lib.clear_screen()
        display_members()
        id = input("Enter the ID of the member you want to update: ")
        lastBorrowedDate = input("Enter the last borrowed date: ")
        lastReturnDate = input("Enter the last return date: ")
        lastBorrowedBookId = input("Enter the last borrowed book ID: ")
        update_member_status(id, lastBorrowedDate, lastReturnDate, lastBorrowedBookId)
        print("Member status updated successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is update member details
    elif input_option == '11':
        lib.clear_screen()
        display_members()
        id = input("Enter the ID of the member you want to update: ")
        name = input("Enter the name: ")
        nic = input("Enter the NIC: ")
        contact = input("Enter the contact: ")
        address = input("Enter the address: ")
        update_member_details(id, name, nic, contact, address)
        print("Member details updated successfully!")
        input("Press Enter to continue...")
        main()
    # Enter option is search member
    elif input_option == '12':
        lib.clear_screen()
        details = input("Enter the details you want to search: ")
        search_member(details)
        input("Press Enter to continue...")
        main()
    # Enter option is exit
    elif input_option == '13':
        exit()

main()

