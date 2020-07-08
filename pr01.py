from abc import ABCMeta, abstractmethod

class Book(metaclass = ABCMeta):

    @abstractmethod
    def num_of_pages(self):
        pass

class Head_First_Python(Book):

    def num_of_pages(self):
        print("500")

class Python_CookBook(Book):

    def num_of_pages(self):
        print("250")


#publication factory
class PublicationFactory():

    def Book_publicator(self, object_type):
        return eval(object_type)().num_of_pages()
                #Head_First_Python.num_of_pages()
#client code
if __name__ == '__main__':
    pf = PublicationFactory()
    book = input("select your book: ") # ---> Head_First_Python
    pf.Book_publicator(book)
