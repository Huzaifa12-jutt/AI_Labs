library=[
{"title": "Introduction to AI", "author": "Stuart Russell",
"copies_available": 3, "rating": 4.8},
{"title": "Python Crash Course", "author": "Eric Matthes",
"copies_available": 0},
{"title": "Deep Learning", "author": "Ian Goodfellow",
"copies_available": 5, "rating": 4.6}
]
for book in library:
    print(book["title"],book["author"])


# part b: 
available_books = [book["title"] for book in library if book["copies_available"] > 0]
print(available_books)

#part c:
for book in library:
    print(book["title"],"Rating",book.get("Rating","Not rating"))

#part d:
