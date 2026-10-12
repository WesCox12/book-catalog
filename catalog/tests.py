from django.test import TestCase
from django.urls import reverse
# Create your tests here.
#A book that exists in the database appears on the Books page.#
from .models import Publisher, Book

class BookListTest(TestCase):
    def test_book_appears_on_books_page(self):
        publisher = Publisher.objects.create(name="Test Publisher")
        Book.objects.create(
            title="Narnia",
            page_count=110,
            publisher=publisher
        )

        response = self.client.get(reverse("book_list"))

        self.assertContains(response, "Narnia")