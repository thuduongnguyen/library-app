'''
This Python scripts provides features like book search, borrowing, returning, adding, and removing books.
Users interact with a menu interface, and librarians have additional capabilities.
It is a comprehensive tool for efficient library collection management.

Notes:
Ensure that the book catalog file exists and is accessible before starting the application.
The application provides error handling and input validation to ensure smooth operation.
Librarian-specific options are available after entering a special code (2130) in the main menu.
'''
import book
import os

def load_books(book_list, file_name):
    book_list = []
    with open (file_name, "r") as file:
        for line in file:
            book_info = line.strip().split(",")
            isbn = book_info[0]
            title = book_info[1]
            author = book_info[2]
            genre = int(book_info[3])
            available = book_info[4]
            single_book = book.Book(isbn, title, author, genre, available)
            book_list.append(single_book)
    return book_list


def print_menu(menu_heading, menu_options):
    print(menu_heading)
    for key, value in menu_options.items():
        print(f"{key}: {value}")
#Validates user's input
    while True:
        choice = input("Enter your selection: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in menu_options:
                return choice
            elif choice == 2130:
                return choice
            else:
                print("Invalid option")
        else:
            print("Invalid option")

def search_books(book_list, search_string):
    books = []
    for book_info in book_list:
        if search_string in book_info.get_isbn() or search_string in book_info.get_title() or search_string in book_info.get_author() or search_string in book_info.get_genre_name() or search_string in book_info.get_availability():
            books.append(book_info)
    return books

def borrow_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)

    if index != -1:
        book = book_list[index]
        if book.get_availability() == "Available":
            book.borrow_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully borrowed.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently available.")
    else:
        print(f"No book found with that ISBN.")

def find_book_by_isbn(book_list, isbn):
    for book_info in book_list:
        if book_info.get_isbn() in isbn and len(book_info.get_isbn()) == len(isbn):
            return book_list.index(book_info)
    return -1


def return_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)

    if index != -1:
        book = book_list[index]
        if book.get_availability() == "Borrowed":
            book.return_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully returned.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")

def add_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    genre_name = input("Enter genre: ")
    #Validate and translating of genre name to integer value
    valid_genres = book.Book.GENRE_NAMES
    while genre_name not in valid_genres:
        print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
        genre_name = input("Enter genre: ")

    genre_id = valid_genres.index(genre_name)
    added_book = book.Book(isbn, title, author, genre_id, available= "True")
    book_list.append(added_book)
    print(f"'{title}' with ISBN {isbn} successfully added.")

def remove_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index != -1:
        removed_book = book_list.pop(index)
        print(f"{removed_book.get_title()} with ISBN {isbn} successfully removed.")
    else:
        print(f"No book found with that ISBN.")

def print_books(books):
    print("{:<14} {:<26} {:<24} {:<20} {:<12}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    print("-------------- ------------------------- ------------------------- -------------------- ------------")
    for book_info in books:
        print(str(book_info))

def save_books(book_list, file_name):
    with open(file_name, "w") as file:
        for book_info in book_list:
            book_string = f"{book_info.get_isbn()},{book_info.get_title()},{book_info.get_author()},{book_info.get_genre()},{book_info.get_available()}".strip() +"\n"
            file.write(book_string)

def main():
    menu_heading = ("\nReader's Guild Library - Main Menu\n==================================")
    menu_options = {1:"Search for books", 2: "Borrow a book", 3: "Return a book", 0: "Exit the system"}
    book_list = []

    #Validates file existence
    print("Starting the system...")
    file_name = input("Enter book catalog filename: ")
    while True:
        if os.path.exists(file_name):
            book_list = load_books(book_list, file_name)
            print("Book catalog has been loaded.")
            break
        else:
            file_name = input("File not found. Re-enter book catalog filename: ")
            continue

    while True:
            choice = print_menu(menu_heading, menu_options)
            if choice == 1:
                print("\n-- Search for books --")
                search_string = input("Enter search value: ").capitalize()
                books = search_books(book_list, search_string)
                if len(books) != 0:
                    print_books(books)
                    continue
                else:
                    print("No matching books found.")
                    continue
            elif choice == 2:
                print("\n-- Borrow a book --")
                borrow_book(book_list)
                save_books(book_list, file_name)
                continue
            elif choice == 3:
                print("\n-- Return a book --")
                return_book(book_list)
                save_books(book_list, file_name)
                continue
            elif choice == 2130:
                #Updates heading for Librarian Menu
                menu_heading = ("\nReader's Guild Library - Librarian Menu\n=======================================")
                del menu_options[0]
                menu_options[4] = "Add a Book"
                menu_options[5] = "Remove a book"
                menu_options[6] = "Print catalog"
                menu_options[0] = "Exit the system"
                continue
            elif choice == 4:
                print("-- Add a book --")
                add_book(book_list)
                save_books(book_list, file_name)
                continue
            elif choice == 5:
                print("-- Remove a book --")
                remove_book(book_list)
                save_books(book_list, file_name)
                continue
            elif choice == 6:
                books = book_list
                print_books(books)
                continue
            elif choice == 0:
                print("-- Exit the system --\nBook catalog has been saved.\nGoodbye!")
                break

if __name__ == "__main__":
    main()