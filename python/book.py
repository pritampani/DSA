
def books():
    B=int(input("enter the number of book you want to insert"))
    for i in range(B):
        bookno=int(input("enter book number:"))
        bookname=input("enter the book name")
        bookauth=input("enter the book author")
        data=[bookno,bookname,bookauth]
        print(books.append(data))  
books()