from class_models import Book,Library


print('initializing library...')
my_library = Library()

book1 = Book("Things Fall Apart", "Chinua Achebe", "111")
book2 = Book("Purple Hibiscus", "Chimamanda Adichie", "222")

my_library.add_book(book1)
my_library.add_book(book2)
print(my_library.check_out_book('111'))
# print(my_library.list_available_books())

