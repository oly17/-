class Book: 
     def __init__(self, author, title, year, genre): 
         self.author = author 
         self.title = title 
         self.year = year 
         self.genre = genre 
  
 
class Library: 
     books = [] 
     def addBook(self, book): 
         self.books.append(book) 
      
     def removeBook(self, book): 
         self.books.remove(book) 
  
 
     def searchByAuthor(self, author): 
         books = [] 
         for book in self.books: 
             if book.author == author: 
                 books.append(book) 
         return books 
      
     def searchByYear(self, year): 
         books = [] 
         for book in self.books: 
             if book.year == year: 
                 books.append(book) 
         return books 
  
 
     def searchByGenre(self, genre): 
         books = [] 
         for book in self.books: 
             if book.genre == genre: 
                 books.append(book) 
         return books 
  
 
     def main(): 
     library = Library() 
     library.addBook(Book('Джоан Роулінг', 'Гаррі Поттер', '2001', 'Роман')) 
     library.addBook(Book('Федір Достоєвський', 'Преступление и наказание', '2005', 'Роман')) 
     library.addBook(Book('Вальтер Скотт', 'Айвенго', '1819', 'Роман')) 
  
 
     author = 'Анджей Сапковський' 
     books = library.searchByAuthor (author) 
     if len(books) == 0: 
         return 
     book = books[0] 
  
 
     print('Кількість книг автора'+ author, len(books)) 
     print('Автор книги', author) 
     print('Титульна сторінка книги' , book.title) 
  
 
     library.removeBook(book) 
     books = library.searchByAuthor(author) 
     print('Нова кількість книг автора' + author, len(books)) 
  
 
    if name == '__main__': 
     main()