"""Simple library manager — Arjun Singh."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    borrowed_by: str | None = None
    due: str | None = None


@dataclass
class Library:
    books: dict[str, Book] = field(default_factory=dict)

    def add(self, isbn: str, title: str, author: str) -> Book:
        b = Book(isbn, title, author)
        self.books[isbn] = b
        return b

    def borrow(self, isbn: str, member: str, days: int = 14) -> Book:
        b = self.books[isbn]
        if b.borrowed_by:
            raise RuntimeError("already borrowed")
        b.borrowed_by = member
        b.due = (datetime.now(timezone.utc) + timedelta(days=days)).date().isoformat()
        return b

    def return_book(self, isbn: str) -> Book:
        b = self.books[isbn]
        b.borrowed_by = None
        b.due = None
        return b

    def search(self, q: str) -> list[Book]:
        q = q.lower()
        return [b for b in self.books.values() if q in b.title.lower() or q in b.author.lower()]


if __name__ == "__main__":
    lib = Library()
    lib.add("1", "Clean Code", "Robert Martin")
    lib.add("2", "Fluent Python", "Luciano Ramalho")
    lib.borrow("1", "Arjun")
    print(lib.search("python"))
    print(lib.books["1"])
