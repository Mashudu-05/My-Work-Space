import sqlite3

def create_database():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        qty INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def populate_database():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    books = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 30),
        (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12)
    ]
    cursor.executemany("INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)", books)
    conn.commit()
    conn.close()

def enter_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    conn.close()
    print("Book added successfully!")

def update_book():
    id = int(input("Enter book ID to update: "))
    field = input("Enter field to update (title, author, qty): ")
    new_value = input("Enter new value: ")
    if field == "qty":
        new_value = int(new_value)
    
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE book SET {field} = ? WHERE id = ?", (new_value, id))
    conn.commit()
    conn.close()
    print("Book updated successfully!")

def delete_book():
    id = int(input("Enter book ID to delete: "))
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully!")

def search_books():
    search = input("Enter book title or author to search: ")
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?", (f"%{search}%", f"%{search}%"))
    books = cursor.fetchall()
    conn.close()
    if books:
        for book in books:
            print(book)
    else:
        print("No books found.")

def main():
    create_database()
    populate_database()
    while True:
        print("""
        1. Enter book
        2. Update book
        3. Delete book
        4. Search books
        0. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            enter_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_books()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
