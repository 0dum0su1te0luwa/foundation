class Book:
    def __init__(self,t,a,i):
        self.title = t
        self.author = a
        self.isbn = i
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out == False:
            self.is_checked_out = True
            return True
        else: 
            return False

    
    def return_book(self):
        if self.is_checked_out == True:
            self.is_checked_out = False 
            return True
        else:
            return False
    
    def __str__(self):
        if self.is_checked_out == True:
            status = 'Checked out'
        else:
            status = 'Available'
        return f'{self.title},by {self.author}, {status}'
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
    
    def remove_book(self,isbn):
        for book in self.books:
            if isbn == book.isbn:
                self.books.remove(book)
                return True
        return False
        
    def check_out_book(self,isbn):
        for book in self.books:
            if isbn == book.isbn:
                return book.check_out()
        return False
        
    def list_available_books(self):
        avail_list = []
        for book in self.books:
            if book.is_checked_out == False:
                avail_list.append(str(book))
        return avail_list        


        

