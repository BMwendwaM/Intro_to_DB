USE alx_book_store;

alx_book_store.execute("SELECT * FROM books")
result = alx_book_store.fetchall()

for i in result:
    print(i)