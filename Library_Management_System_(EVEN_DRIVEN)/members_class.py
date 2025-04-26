import json
class MembersClass:
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
        return_data = []
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
            return_data.append([id, name, nic, contact, address, lastBorrowedDate, lastRerunDate, lastBorrowedBookId])
        return return_data
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
        return_data = None
        self._membersData[id]['status']['lastBorrowedDate'] = borrowedDate
        self._membersData[id]['status']['lastReturnDate'] = returnDate
        self._membersData[id]['status']['lastBorrowedBookId'] = bookId
        # Write the new data to the json file
        self.__write_json('members.json', self._membersData)
        return_data = True
        return return_data
    # Return a book - (Public)
    def return_book(self, id):
        return_data = None
        self._membersData[id]['status']['lastBorrowedDate'] = None
        self._membersData[id]['status']['lastReturnDate'] = None
        self._membersData[id]['status']['lastBorrowedBookId'] = None
            # Write the new data to the json file
        self.__write_json('members.json', self._membersData)
        return_data = True
        return return_data
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
        retun_data = None
        try:
            del self._membersData[id]
            self.__write_json('members.json', self._membersData)
            retun_data = True
        except:
            retun_data = False
        return retun_data
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