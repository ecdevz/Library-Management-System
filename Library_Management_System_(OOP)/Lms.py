# Import the json & operation system libraries
import json
import os

## BOOKS SECTION
class Books:
    def __init__(self):
        # Read the data from the json file - (Private)
        self._booksData = self.__read_json('books.json')
    # Read from json file - (Protected)
    def __read_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)
    # Write to json file - (Protected)
    def __write_json(self, path, data):
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
    # Display all books - (Public)
    def display_books(self):
        # Display the header
        print('-'*209)
        print(f"{'ID'}{" "*3}| {'Title'}{' '*65}| {'Author'}{' '*44}| {'Year'}{' '*1}| {'Genre'}{' '*10}| {'Borrowed'} | {'Borrowed To'} | {'Borrowed Date'} | {'Return Date'} |")
        # Get lenth of database
        datalen = self._booksData.keys()
        # Store the data in a list
        for i in datalen:
            id = str(i)
            title = self._booksData[id]['title']
            author = self._booksData[id]['author']
            year = str(self._booksData[id]['year'])
            genre = self._booksData[id]['genre']
            isBorrowed = self._booksData[id]['status']['isBorrowed']
            borrowedDate = self._booksData[id]['status']['borrowedDate']
            returnDate = self._booksData[id]['status']['returnDate']
            borrowedTo = self._booksData[id]['status']['borrowedTo']
            # Prepare borrowed status
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
            # Display the book data
            print(f"{'-'*5}|{'-'*71}|{'-'*51}|{'-'*6}|{'-'*16}|{'-'*10}|{'-'*13}|{'-'*15}|{'-'*13}|")
            print(f'{id}{" "*(5-len_id)}| {title}{" "*(70-len_title)}| {author}{" "*(50-len_author)}| {year}{" "*(5-len_year)}| {genre}{" "*(15-len_genre)}| {borrowed()}{" "*(9-len_borrowed)}| {borrowed_to()}{" "*(12-len_borrowed_to)}| {borrowed_date()}{" "*(14-len_borrowed_date)}| {return_date()}{" "*(12-len_return_date)}|')
        print('-'*209)
    # Add a new book - (Public)
    def add_book(self, title, author, year, genre):
        # Get the last id
        last_id = list(self._booksData.keys())[-1]
        # Add the new book
        self._booksData[str(int(last_id)+1)] = {
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
        # Write the new data to the json file
        self.__write_json('books.json', self._booksData)
        print('Book added successfully!')
    # Borrow a book - (Public)
    def borrow_book(self, id, name, borrowedDate, returnDate):
        # Check if the book is borrowed
        if self._booksData[id]['status']['isBorrowed'] == False:
            self._booksData[id]['status']['isBorrowed'] = True
            self._booksData[id]['status']['borrowedTo'] = name
            self._booksData[id]['status']['borrowedDate'] = borrowedDate
            self._booksData[id]['status']['returnDate'] = returnDate
            # Write the new data to the json file
            self.__write_json('books.json', self._booksData)
            print('Book borrowed successfully!')
        else:
            print('Book is already borrowed!')
    # Return a book - (Public)
    def return_book(self, id):
        # Check if the book is borrowed
        if self._booksData[id]['status']['isBorrowed'] == True:
            self._booksData[id]['status']['isBorrowed'] = False
            self._booksData[id]['status']['borrowedTo'] = None
            self._booksData[id]['status']['borrowedDate'] = None
            self._booksData[id]['status']['returnDate'] = None
            # Write the new data to the json file
            self.__write_json('books.json', self._booksData)
            print('Book returned successfully!')
        else:
            print('Book is not borrowed!')
    # Search a book - (Public)
    def search_book(self, details):
        try:
            for i in self._booksData:
                if details.lower() in self._booksData[i]['title'].lower():
                    return i
                elif details.lower() in self._booksData[i]['author'].lower():
                    return i
                elif details.lower() in self._booksData[i]['year']:
                    return i
                elif details.lower() in self._booksData[i]['genre'].lower():
                    return i
            return False
        except:
            return False
    # Delete a book - (Public)
    def delete_book(self, id):
        try:
            del self._booksData[id]
            self.__write_json('books.json', self._booksData)
            print('Book deleted successfully!')
        except:
            print('Book not found!')

## MEMBERS SECTION
class Members:
    def __init__(self):
        # Read the data from the json file - (Private)
        self._membersData = self.__read_json('members.json')
    # Read from json file - (Protected)
    def __read_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)
    # Write to json file - (Protected)
    def __write_json(self, path, data):
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
    # Display all members - (Public)
    def display_members(self):
        # Display the header
        print('-'*201)
        print(f"{'ID'}{" "*3}| {'Name'}{' '*45}| {'NIC'}{' '*13}| {'Contact'}{' '*5}| {'Address'}{' '*40}| {'Last Borrowed Date'} | {'Last Return Date'} | {'Last Borrowed Book ID'} |")
        # Get lenth of database
        datalen = self._membersData.keys()
        for i in datalen:
            id = str(i)
            nic = self._membersData[id]['nic']
            name = self._membersData[id]['name']
            address = self._membersData[id]['address']
            contact = self._membersData[id]['contact']
            lastBorrowedDate = self._membersData[id]["status"]['lastBorrowedDate']
            lastRerunDate = self._membersData[id]["status"]['lastReturnDate']
            lastBorrowedBookId = self._membersData[id]["status"]['lastBorrowedBookId']
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
    # Add a new member - (Public)
    def add_member(self, name, nic, contact, address):
        # Get the last id
        last_id = list(self._membersData.keys())[-1]
        # Add the new member
        self._membersData[str(int(last_id)+1)] = {
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
        # Write the new data to the json file
        self.__write_json('members.json', self._membersData)
        print('Member added successfully!')
    # Borrow a book - (Public)
    def borrow_book(self, id, bookId, borrowedDate, returnDate):
        # Check if the book is borrowed
        if self._membersData[id]['status']['lastBorrowedBookId'] == None:
            self._membersData[id]['status']['lastBorrowedDate'] = borrowedDate
            self._membersData[id]['status']['lastReturnDate'] = returnDate
            self._membersData[id]['status']['lastBorrowedBookId'] = bookId
            # Write the new data to the json file
            self.__write_json('members.json', self._membersData)
            print('Book borrowed successfully!')
        else:
            print('Book is already borrowed!')
    # Return a book - (Public)
    def return_book(self, id):
        # Check if the book is borrowed
        if self._membersData[id]['status']['lastBorrowedBookId'] != None:
            self._membersData[id]['status']['lastBorrowedDate'] = None
            self._membersData[id]['status']['lastReturnDate'] = None
            self._membersData[id]['status']['lastBorrowedBookId'] = None
            # Write the new data to the json file
            self.__write_json('members.json', self._membersData)
            print('Book returned successfully!')
        else:
            print('Book is not borrowed!')
    # Search a member - (Public)
    def search_member(self, details):
        try:
            for i in self._membersData:
                if details.lower() in self._membersData[i]['name'].lower():
                    return i
                elif details.lower() in self._membersData[i]['nic'].lower():
                    return i
                elif details.lower() in self._membersData[i]['contact']:
                    return i
                elif details.lower() in self._membersData[i]['address'].lower():
                    return i
            return False
        except:
            return False
    # Delete a member - (Public)
    def delete_member(self, id):
        try:
            del self._membersData[id]
            self.__write_json('members.json', self._membersData)
            print('Member deleted successfully!')
        except:
            print('Member not found!')
    # Update member status - (Public)
    def update_member_status(self, id, lastBorrowedDate, lastReturnDate, lastBorrowedBookId):
        try:
            self._membersData[id]['status']['lastBorrowedDate'] = lastBorrowedDate
            self._membersData[id]['status']['lastReturnDate'] = lastReturnDate
            self._membersData[id]['status']['lastBorrowedBookId'] = lastBorrowedBookId
            self.__write_json('members.json', self._membersData)
            print('Member status updated successfully!')
        except:
            print('Member not found!')

## SYSTEM SECTION
class System(Books, Members):
    def __init__(self):
        # Initialize the parent classes
        Books.__init__(self)
        Members.__init__(self)
    # Clear the screen - (Protected)
    def __clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    # Display the dashboard - (Private)
    def _display_dashboard(self):
        # Get the number of borrowed books
        count = 0
        for i in self._booksData:
            if self._booksData[i]['status']['isBorrowed'] == True:
                count += 1
        # Display
        print(f" {'-'*49} ")
        print(f"|{' '*20}DASHBOARD{' '*20}|")
        print(f" {'-'*49} ")
        print(f"|{' '*5}1. Books - {len(self._booksData)}{' '*(10-len(str(len(self._booksData))))}| {' '*8}Library{' '*9}|")
        print(f"|{' '*5}2. Members - {len(self._membersData)}{' '*(7-len(str(len(self._membersData))))}|{' '*7}Manegement{' '*8}|")
        print(f"|{' '*5}3. Borrow  - {count}{' '*(5-len(str(count)))}|{' '*10}System{' '*9}|")
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
        print('\n')
    # Run the system - (Public)
    def run(self):
        print("Welcome to Library Management System\n")
        self._display_dashboard()
        input_option = input("Enter an option: ")
        # Enter option is show books
        if input_option == '1':
            self.__clear_screen()
            self.display_books()
            input("Press Enter to continue...")
            self.run()
        # Enter option is add book
        elif input_option == '2':
            self.__clear_screen()
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            year = input("Enter the year: ")
            genre = input("Enter the genre: ")
            self.add_book(title, author, year, genre)
            print("Book added successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is delete book
        elif input_option == '3':
            self.__clear_screen()
            self.display_books()
            id = input("Enter the ID of the book you want to delete: ")
            self.delete_book(id)
            print("Book deleted successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is borrow book
        elif input_option == '4':
            self.__clear_screen()
            self.display_books()
            id = input("Enter the ID of the book you want to borrow: ")
            borrowedTo = input("Enter the name of the person who borrowed the book: ")
            borrowedDate = input("Enter the borrowed date: ")
            returnDate = input("Enter the return date: ")
            self.borrow_book(id, borrowedTo, borrowedDate, returnDate)
            print("Book borrowed successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is return book
        elif input_option == '5':
            self.__clear_screen()
            self.display_books()
            id = input("Enter the ID of the book you want to return: ")
            self.return_book(id)
            print("Book returned successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is search book
        elif input_option == '6':
            self.__clear_screen()
            details = input("Enter the details you want to search: ")
            self.search_book(details)
            input("Press Enter to continue...")
            self.run()
        # Enter option is show members
        elif input_option == '7':
            self.__clear_screen()
            self.display_members()
            input("Press Enter to continue...")
            self.run()
        # Enter option is add member
        elif input_option == '8':
            self.__clear_screen()
            name = input("Enter the name: ")
            nic = input("Enter the NIC: ")
            contact = input("Enter the contact: ")
            address = input("Enter the address: ")
            self.add_member(name, nic, contact, address)
            print("Member added successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is delete member
        elif input_option == '9':
            self.__clear_screen()
            self.display_members()
            id = input("Enter the ID of the member you want to delete: ")
            self.delete_member(id)
            print("Member deleted successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is update member status
        elif input_option == '10':
            self.__clear_screen()
            self.display_members()
            id = input("Enter the ID of the member you want to update: ")
            lastBorrowedDate = input("Enter the last borrowed date: ")
            lastReturnDate = input("Enter the last return date: ")
            lastBorrowedBookId = input("Enter the last borrowed book ID: ")
            self.update_member_status(id, lastBorrowedDate, lastReturnDate, lastBorrowedBookId)
            print("Member status updated successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is update member details
        elif input_option == '11':
            self.__clear_screen()
            self.display_members()
            id = input("Enter the ID of the member you want to update: ")
            name = input("Enter the name: ")
            nic = input("Enter the NIC: ")
            contact = input("Enter the contact: ")
            address = input("Enter the address: ")
            self.update_member_details(id, name, nic, contact, address)
            print("Member details updated successfully!")
            input("Press Enter to continue...")
            self.run()
        # Enter option is search member
        elif input_option == '12':
            self.__clear_screen()
            details = input("Enter the details you want to search: ")
            self.search_member(details)
            input("Press Enter to continue...")
            self.run()
        # Enter option is exit
        elif input_option == '13':
            exit()
        # Invalid option
        else:
            print("Invalid option!")
            input("Press Enter to continue...")
            self.run()

## RUN THE SYSTEM
sys = System()
sys.run()
