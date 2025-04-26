import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Importing Book and Members classes
from book_class import BookClass
from members_class import MembersClass

# Define the colors
color = {
    "bg": "#303841",
    "bg1": "#3A4750",
    "secondery": "#00ADB5",
    "primery": "#EEEEEE",
    "front": "#EEEEEE",
    "error": "#D72323",
}

book_class = BookClass()
member_class = MembersClass() 

root = tk.Tk()
root.title("Library management system")
root.geometry("1000x600")
root.configure(background=color["bg"])

# Center the window dialog
def center_window(window, parent):
    window.update_idletasks()
    x = parent.winfo_rootx() + (parent.winfo_width() - window.winfo_width()) // 2
    y = parent.winfo_rooty() + (parent.winfo_height() - window.winfo_height()) // 2
    window.geometry(f"+{x}+{y}")

style = ttk.Style()
style.configure("Colored.TFrame", background=color["bg"]) 

# Header Section
header = ttk.Frame(root, padding="10 10 10 10", style="Colored.TFrame")
header_title = ttk.Label(header, text="Library Management System", font=("monopace", 15), background=color["bg"], foreground=color["front"])
header_title.pack(anchor="n")

# Display book function
def display_books():
    list_title.config(text="List books")
    books_area.configure(columns=("ID", "Title", "Author", "Year", "Genre", "Borrowed", "Borrowed To", "Borrowed Date", "Return Date"))
    books_area.heading("ID", text="ID")
    books_area.heading("Title", text="Title")
    books_area.heading("Author", text="Author")
    books_area.heading("Year", text="Year")
    books_area.heading("Genre", text="Genre")
    books_area.heading("Borrowed", text="Borrowed")
    books_area.heading("Borrowed To", text="Borrowed To")
    books_area.heading("Borrowed Date", text="Borrowed Date")
    books_area.heading("Return Date", text="Return Date")
    books_area.delete(*books_area.get_children())  # Clear existing items

    books_data = book_class.display_books()

    for book in books_data:
        books_area.insert("", tk.END, values=book)
    # Display buttons
    books_buttons_frame.pack(anchor="center", fill="x", padx=40, pady=40)
    members_buttons_frame.pack_forget()

# Display Members
def display_members():
    list_title.config(text="List members")
    books_area.configure(columns=("ID", "Name", "NIC", "Contact", "Address", "Last Borrowed Date", "Last Return Date", "Last Borrowed Book ID"))
    books_area.heading("ID", text="ID")
    books_area.heading("Name", text="Name")
    books_area.heading("NIC", text="NIC")
    books_area.heading("Contact", text="Contact")
    books_area.heading("Address", text="Address")
    books_area.heading("Last Borrowed Date", text="Last Borrowed Date")
    books_area.heading("Last Return Date", text="Last Return Date")
    books_area.heading("Last Borrowed Book ID", text="Last Borrowed Book ID")
    books_area.delete(*books_area.get_children())  # Clear existing items
    #books_area.configure(columns=("ID", "Name", "NIC", "Contact", "Address", "Last Borrowed Date", "Last Return Date", "Last Borrowed Book ID"))
    books_data = member_class.display_members()
    print(books_data)
    for book in books_data:
        books_area.insert("", tk.END, values=book)
    # Display buttons
    members_buttons_frame.pack(anchor="center", fill="x", padx=40, pady=40)
    books_buttons_frame.pack_forget()

# books && users buttons
books_button = ttk.Button(header, text="Books", style="Colored.TButton", command=display_books)
books_button.pack(side="left", padx=5)
users_button = ttk.Button(header, text="Members", style="Colored.TButton", command=display_members)
users_button.pack(side="left", padx=5)
header.pack(fill="x")

# Book List Section
list_frame = ttk.Frame(root, padding="10 10 10 10", style="Colored.TFrame")
list_title = ttk.Label(list_frame, text="List of books", font=("monopace", 10), background=color["bg"], foreground=color["front"])
list_title.pack(anchor="center")
books_area = ttk.Treeview(list_frame, columns=("ID", "Title", "Author", "Year", "Genre", "Borrowed", "Borrowed To", "Borrowed Date", "Return Date"), show="headings")
#books_area.heading("ID", text="ID")
#books_area.heading("Title", text="Title")
#books_area.heading("Author", text="Author")
#books_area.heading("Year", text="Year")
#books_area.heading("Genre", text="Genre")
#books_area.heading("Borrowed", text="Borrowed")
#books_area.heading("Borrowed To", text="Borrowed To")
#books_area.heading("Borrowed Date", text="Borrowed Date")
#books_area.heading("Return Date", text="Return Date")
style.configure("Treeview", background="lightblue", foreground="black", fieldbackground="lightblue", font=("monopace", 10), rowheight=25, borderwidth=0)
style.map("Treeview", background=[('selected', 'green'), ('active', color["secondery"])], foreground=[('selected', 'white'), ('active', 'black')])
books_area.pack(fill="both", expand=True)
list_frame.pack(fill="both", expand=True)
# Add book function
def add_book(frame):
    # function to add book
    def submit():
        book_name = name_input.get()
        book_author = author_input.get()
        book_year = year_input.get()
        book_genre = genre_input.get()
        if book_name and book_author and book_year and book_genre:
            book_class.add_book(book_name, book_author, book_year, book_genre)
            display_books()
            dialog.destroy()
        else:
            messagebox.showerror("Warning", "Please enter all fields")
    dialog = tk.Toplevel(frame)
    dialog.transient(frame)
    dialog.title("Add Book")
    dialog.configure(background=color["bg"])
    dialog.resizable(False, False)
    # Center the dialog within the frame
    center_window(dialog, frame)
    ttk.Label(dialog, text="Enter book title:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    name_input = ttk.Entry(dialog, width=40)
    name_input.pack(padx=10, pady=5, fill="x")
    ttk.Label(dialog, text="Enter book author:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    author_input = ttk.Entry(dialog, width=40)
    author_input.pack(padx=10, pady=5)
    ttk.Label(dialog, text="Enter book year:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    year_input = ttk.Entry(dialog, width=40)
    year_input.pack(padx=10, pady=5)
    ttk.Label(dialog, text="Enter book genre:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    genre_input = ttk.Entry(dialog, width=40)
    genre_input.pack(padx=10, pady=5)
    # Submit button
    button = ttk.Button(dialog, text="Submit", command=submit)
    button.pack(pady=10)
# Delete book function
def delete_book():
    selected_item = books_area.selection()
    if selected_item:
        book_id = books_area.item(selected_item, "values")[0]
        book_class.delete_book(book_id)
        display_books()
    else:
        messagebox.showerror("Warning", "Please select a book to delete")

# Borrow book function
def borrow_book(frame):
    selected_item = books_area.selection()
    if selected_item:
        book_id = books_area.item(selected_item, "values")[0]
        # Submit Button
        def submit():
            member_id = member_id_input.get()
            borrowed_date = borrowed_date_input.get()
            return_date = return_date_input.get()
            if member_id and borrowed_date and return_date:
                let = book_class.borrow_book(book_id, member_id, borrowed_date, return_date)
                mem = member_class.borrow_book(member_id, book_id, borrowed_date, return_date)
                if let == "Book borrowed successfully!":
                    if mem == True:
                        messagebox.showinfo("Success", "Book borrowed successfully!")
                        display_books()
                        dialog.destroy()
                    else:
                        messagebox.showerror("Warning", "Member is already borrowed a book or not exist")
                else:
                    messagebox.showerror("Warning", "Book is already borrowed!")
            else:
                messagebox.showerror("Warning", "Please enter all fields")
        # open the dialog box
        dialog = tk.Toplevel(frame)
        dialog.transient(frame)
        dialog.title("Add Book")
        dialog.configure(background=color["bg"])
        dialog.resizable(False, False)
        # Center the dialog within the frame
        center_window(dialog, frame)
        ttk.Label(dialog, text="Enter member ID:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
        member_id_input = ttk.Entry(dialog, width=40)
        member_id_input.pack(padx=10, pady=5, fill="x")
        ttk.Label(dialog, text="Enter borrowed date:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
        borrowed_date_input = ttk.Entry(dialog, width=40)
        borrowed_date_input.pack(padx=10, pady=5)
        ttk.Label(dialog, text="Enter return date:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
        return_date_input = ttk.Entry(dialog, width=40)
        return_date_input.pack(padx=10, pady=5)
        # Submit button
        button = ttk.Button(dialog, text="Submit", command=submit)
        button.pack(pady=10)
    else:
        messagebox.showerror("Warning", "Please select a book to borrow")

# Return book function
def return_book():
    selected_item = books_area.selection()
    if selected_item:
        book_id = books_area.item(selected_item, "values")[0]
        member_id = books_area.item(selected_item, "values")[6]
        book_class.return_book(book_id)
        member_class.return_book(member_id)
        messagebox.showinfo("Success", "Book returned successfully!")
        display_books()
    else:
        messagebox.showerror("Warning", "Please select a book to return")

# Search book function
def search_book(frame):
    def submit():
        search_details = search_input.get()
        if search_details:
            for itemid in books_area.get_children():
                item_values = books_area.item(itemid, "values")
                for value in item_values:
                    if search_details in value:
                        books_area.selection_set(itemid)
                        books_area.focus(itemid)
                        dialog.destroy()
                        break
        else:
            messagebox.showerror("Warning", "Please enter book details")
    dialog = tk.Toplevel(frame)
    dialog.title("Search Book")
    dialog.configure(background=color["bg"])
    dialog.resizable(False, False)
    # Center the dialog within the frame
    center_window(dialog, frame)
    ttk.Label(dialog, text="Enter book details:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    search_input = ttk.Entry(dialog, width=40)
    search_input.pack(padx=10, pady=5, fill="x")
    # Submit button
    sumbit_button = ttk.Button(dialog, text="Submit", command=submit)
    sumbit_button.pack(pady=10)

# Books Buttons Section
books_buttons_frame = ttk.Frame(root, style="Colored.TFrame")
add_book_button = ttk.Button(books_buttons_frame, text="Add Book", width=20, command=lambda: add_book(root))
add_book_button.pack(side="left", padx=15)
delete_book_button = ttk.Button(books_buttons_frame, text="Delete Book", width=20, command=delete_book)
delete_book_button.pack(side="left", padx=15)
borrow_book_button = ttk.Button(books_buttons_frame, text="Let Book", width=20, command=lambda: borrow_book(root))
borrow_book_button.pack(side="left", padx=15)
return_book_button = ttk.Button(books_buttons_frame, text="Return Book", width=20, command=return_book)
return_book_button.pack(side="left", padx=15)
search_book_button = ttk.Button(books_buttons_frame, text="Search Book", width=20, command=lambda: search_book(root))
search_book_button.pack(side="left", padx=15)
exit_button = ttk.Button(books_buttons_frame, text="Exit", style="Colored.TButton", width=30, command=root.quit)
exit_button.pack(side="right", pady=10, padx=10)
#books_buttons_frame.pack(anchor="nw")

# Add Member function
def add_member(frame):
    # function to add member
    def submit():
        member_name = name_input.get()
        member_nic = nic_input.get()
        member_contact = contact_input.get()
        member_address = address_input.get()
        if member_name and member_nic and member_contact and member_address:
            member_class.add_member(member_name, member_nic, member_contact, member_address)
            display_members()
            dialog.destroy()
        else:
            messagebox.showerror("Warning", "Please enter all fields")
    dialog = tk.Toplevel(frame)
    dialog.transient(frame)
    dialog.title("Add Member")
    dialog.configure(background=color["bg"])
    dialog.resizable(False, False)
    # Center the dialog within the frame
    center_window(dialog, frame)
    ttk.Label(dialog, text="Enter member name:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    name_input = ttk.Entry(dialog, width=40)
    name_input.pack(padx=10, pady=5, fill="x")
    ttk.Label(dialog, text="Enter member NIC:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    nic_input = ttk.Entry(dialog, width=40)
    nic_input.pack(padx=10, pady=5)
    ttk.Label(dialog, text="Enter member contact:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    contact_input = ttk.Entry(dialog, width=40)
    contact_input.pack(padx=10, pady=5)
    ttk.Label(dialog, text="Enter member address:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    address_input = ttk.Entry(dialog, width=40)
    address_input.pack(padx=10, pady=5)
    # Submit button
    button = ttk.Button(dialog, text="Submit", command=submit)
    button.pack(pady=10)

# Delete Member function
def delete_member():
    selected_item = books_area.selection()
    if selected_item:
        member_id = books_area.item(selected_item, "values")[0]
        delmem = member_class.delete_member(member_id)
        if delmem == True:
            display_members()
            messagebox.showinfo("Success", "Member deleted successfully!")
        else:
            messagebox.showerror("Alart", "Delete failed") 
    else:
        messagebox.showerror("Warning", "Please select a member to delete")

# Search Member function
def search_member(frame):
    def submit():
        search_details = search_input.get()
        if search_details:
            for itemid in books_area.get_children():
                item_values = books_area.item(itemid, "values")
                for value in item_values:
                    if search_details in value:
                        books_area.selection_set(itemid)
                        books_area.focus(itemid)
                        dialog.destroy()
                        break
        else:
            messagebox.showerror("Warning", "Please enter member details")
    dialog = tk.Toplevel(frame)
    dialog.title("Search Member")
    dialog.configure(background=color["bg"])
    dialog.resizable(False, False)
    # Center the dialog within the frame
    center_window(dialog, frame)
    ttk.Label(dialog, text="Enter member details:", background=color["bg"], foreground=color["front"]).pack(padx=10, pady=10)
    search_input = ttk.Entry(dialog, width=40)
    search_input.pack(padx=10, pady=5, fill="x")
    # Submit button
    sumbit_button = ttk.Button(dialog, text="Submit", command=submit)
    sumbit_button.pack(pady=10)

# Members Buttons Section
members_buttons_frame = ttk.Frame(root, style="Colored.TFrame")
add_member_button = ttk.Button(members_buttons_frame, text="Add Member", width=30, command=lambda: add_member(root))
add_member_button.pack(side="left", padx=15)
delete_member_button = ttk.Button(members_buttons_frame, text="Delete Member", width=30, command=delete_member)
delete_member_button.pack(side="left", padx=15)
search_member_button = ttk.Button(members_buttons_frame, text="Search Member", width=30, command=lambda: search_member(root))
search_member_button.pack(side="left", padx=15)
exit_button = ttk.Button(members_buttons_frame, text="Exit", style="Colored.TButton", command=root.quit)
exit_button.pack(side="right", pady=10, padx=10)
#members_buttons_frame.pack(anchor="nw")

# Exit Button
#exit_button = ttk.Button(root, text="Exit", style="Colored.TButton", command=root.quit)
#exit_button.pack(anchor="e", pady=10, padx=10)
# Footer Section

# Display books by default
display_books()
# Run the app
root.mainloop()
