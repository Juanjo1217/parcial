class library:
    def __init__(self, book: str) -> None:
        self.book = book
        self.books = list
        

    """
    manejo de libros
    """
    def book_state(self, book: str):
        """
        Recive un string "book" y dice si el libro está disponible y en buen estado
        """
        books = ['reglamento']
        for r in books:
            if self.book == books[r]:
                print("Se encuentra disponible")

    def add_book(self, book: str):
        """
        Agrega un nuevo libro
        """
        self.books.append = book
        print("se agregó correctamente")
        

class user (library):
    def __init__(self, book: str) -> None:
        self.book = book
        pass

    def get_book(self, book: str):
        """
        toma presatado un libro
        """
        library.books.pop = self.book

    def return_book(self, book: str):
        """
        regresa el libro prestado
        """
        library.book.pop = self.book
        pass

    def display_book(self):
        """
        muestra los libros
        """
        print(library.books)

