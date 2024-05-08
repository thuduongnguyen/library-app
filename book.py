#Book Class with attributes: isbn, title, author, genre, available

class Book:
#Genre Names Constant
    GENRE_NAMES = ("Romance", "Mystery", "Science Fiction", "Thriller", "Young Adult", "Children's Fiction", "Self-help", "Fantasy", "Historical Fiction", "Poetry")

    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author 
        self.__genre = genre 
        self.__available = available

#Getters for each attribute
    def get_isbn (self):
        return self.__isbn
    
    def get_title (self):
        return self.__title
    
    def get_author (self):
        return self.__author
    
    def get_genre (self):
        return self.__genre
    
    def get_available (self):
        return self.__available

#Getter method that returns name of genre as string
    def get_genre_name(self):
        genre_index = self.get_genre()
        if genre_index >= 0 and genre_index < len(self.GENRE_NAMES):
            return self.GENRE_NAMES[genre_index]
        else:
            return "Error"

    def get_availability (self):
        if self.get_available() == "True":
            return "Available"
        else:
            return "Borrowed"

#Setters for each attribute
    def set_isbn (self, new_isbn):
        self.__isbn = new_isbn

    def set_title (self, new_title):
        self.__title = new_title

    def set_author (self, new_author):
        self.__author = new_author

    def set_genre (self, new_genre):
        self.__genre = new_genre

#Sets books available attribute to FALSE
    def borrow_it(self):
        self.__available = "False"

#Sets books available attribute to TRUE
    def return_it(self):
        self.__available = "True"

#Returns string representaton of book formatted disply
    def __str__(self):
        return "{:<14} {:<26} {:<24} {:<20} {:<12}".format(self.get_isbn(), self.get_title(), self.get_author(), self.get_genre_name(), self.get_availability())
