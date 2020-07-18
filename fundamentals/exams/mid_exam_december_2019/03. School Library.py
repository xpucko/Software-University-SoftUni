books = input().split('&')

while True:
    line = input()
    if line == 'Done':
        break

    tokens = line.split(' | ')
    command = tokens[0]
    if command == 'Add Book':
        book = tokens[1]
        if book not in books:
            books.insert(0, book)
    if command == 'Take Book':
        book = tokens[1]
        if book in books:
            books.remove(book)
    if command == 'Swap Books':
        book_1, book_2 = tokens[1], tokens[2]
        if book_1 in books and book_2 in books:
            index_1, index_2 = books.index(book_1), books.index(book_2)
            books[index_1], books[index_2] = books[index_2], books[index_1]
    if command == 'Insert Book':
        book = tokens[1]
        books.append(book)
    if command == 'Check Book':
        index = int(tokens[1])
        if index in range(len(books)):
            print(books[index])

print(', '.join(books))
