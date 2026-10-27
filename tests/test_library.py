from library import Library

def test_borrow_return():
    lib = Library()
    lib.add("1", "X", "Y")
    lib.borrow("1", "Arjun")
    assert lib.books["1"].borrowed_by == "Arjun"
    lib.return_book("1")
    assert lib.books["1"].borrowed_by is None
