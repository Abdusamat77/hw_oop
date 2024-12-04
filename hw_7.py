import sqlite3

# Функция для создания базы данных и таблицы
def create_table():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER
    )''')
    
    conn.commit()
    conn.close()

# Функция для добавления книги
def add_book(title, author, year):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO books (title, author, year)
    VALUES (?, ?, ?)''', (title, author, year))
    
    conn.commit()
    conn.close()

# Функция для поиска книги по названию
def find_book_by_title(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM books WHERE title = ?''', (title,))
    book = cursor.fetchone()
    
    conn.close()
    
    if book:
        return book
    else:
        return None

# Функция для обновления года издания книги
def update_book_year(title, new_year):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE books
    SET year = ?
    WHERE title = ?''', (new_year, title))
    
    conn.commit()
    conn.close()

# Функция для удаления книги по названию
def delete_book_by_title(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    DELETE FROM books WHERE title = ?''', (title,))
    
    conn.commit()
    conn.close()

# Функция для отображения меню
def show_menu():
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Найти книгу по названию")
    print("3. Обновить год издания книги")
    print("4. Удалить книгу по названию")
    print("5. Выйти")

# Основная функция программы
def main():
    create_table()  # Создаем таблицу при старте программы
    
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            add_book(title, author, year)
            print("Книга добавлена.")
        
        elif choice == '2':
            title = input("Введите название книги для поиска: ")
            book = find_book_by_title(title)
            if book:
                print(f"Найдена книга: {book}")
            else:
                print("Книга не найдена.")
        
        elif choice == '3':
            title = input("Введите название книги для обновления года издания: ")
            new_year = int(input("Введите новый год издания: "))
            update_book_year(title, new_year)
            print("Год издания обновлен.")
        
        elif choice == '4':
            title = input("Введите название книги для удаления: ")
            delete_book_by_title(title)
            print("Книга удалена.")
        
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
