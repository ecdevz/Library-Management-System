import json

class BookClass:
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
        return_data = []
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
            # return the data
            #print(f"{'-'*5}|{'-'*71}|{'-'*51}|{'-'*6}|{'-'*16}|{'-'*10}|{'-'*13}|{'-'*15}|{'-'*13}|")
            return_data.append([id, title, author, year, genre, borrowed(), borrowed_to(), borrowed_date(), return_date()])
            #print(f'|{id}{" "*(5-len_id)}| {title}{" "*(70-len_title)}| {author}{" "*(50-len_author)}| {year}{" "*(5-len_year)}| {genre}{" "*(15-len_genre)}| {borrowed()}{" "*(9-len_borrowed)}| {borrowed_to()}{" "*(12-len_borrowed_to)}| {borrowed_date()}{" "*(14-len_borrowed_date)}| {return_date()}{" "*(12-len_return_date)}|')
        return return_data
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
        return_data = " "
        # Check if the book is borrowed
        if self._booksData[id]['status']['isBorrowed'] == False:
            self._booksData[id]['status']['isBorrowed'] = True
            self._booksData[id]['status']['borrowedTo'] = name
            self._booksData[id]['status']['borrowedDate'] = borrowedDate
            self._booksData[id]['status']['returnDate'] = returnDate
            # Write the new data to the json file
            self.__write_json('books.json', self._booksData)
            return_data = 'Book borrowed successfully!'
        else:
            return_data = 'Book is already borrowed!'
        return return_data
    # Return a book - (Public)
    def return_book(self, id):
        return_data = None
        # Check if the book is borrowed
        if self._booksData[id]['status']['isBorrowed'] == True:
            self._booksData[id]['status']['isBorrowed'] = False
            self._booksData[id]['status']['borrowedTo'] = None
            self._booksData[id]['status']['borrowedDate'] = None
            self._booksData[id]['status']['returnDate'] = None
            # Write the new data to the json file
            self.__write_json('books.json', self._booksData)
            return_data = True
        else:
            return_data = False
        return return_data
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