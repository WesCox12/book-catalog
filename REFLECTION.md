# Homework 2 Reflection

## Test Failure Output

Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_book_appears_on_books_page (catalog.tests.BookListTest.test_book_appears_on_books_page)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Wesley Cox\cidm3312\book-catalog\catalog\tests.py", line 18, in test_book_appears_on_books_page
    self.assertContains(response, "Narnia")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'Narnia' in the following response
b'<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>Book Catalog</title>\n</head>\n<body>\n    <nav>\n        <a href="/">Books</a>\n        <a href="/publishers/">Publishers</a>\n        <a href="/reviews/">Reviews</a>\n    </nav>\n\n    <main>\n        \n    <h1>Books</h1>\n\n    \n\n    </main>\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.011s

FAILED (failures=1)
Destroying test database for alias 'default'...

## Test Failure Explaination
The test failed because I changed the Books view to return no books, which confirmed the test detects when a book in the database is missing from the page. 

## Question 1. 
The Book model containts a ForeignKey that points to the Publisher model. It is this way so that one Publisher model can pyublish multiple books, but each book belongs to one publisher. If it were reversed, I would have to assign each book to each publisher instead of assignming a publisher to each book. 

## Question 2. 
I did IntegerField for page_count because the this field would use whole numbers and not characters. If I were using characters I would use CharField. If I used CharField I would lose the ability to easily compare page counts.