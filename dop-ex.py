import csv

def get_unique_publishers():
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=';')
        
        next(reader)
        
        unique_publishers = set()
        
        for row in reader:
            publisher = row[4]  
            unique_publishers.add(publisher)
        
        print("Перечень уникальных издательств:")
        for publisher in sorted(unique_publishers):
            print(publisher)
            print()

get_unique_publishers()

def get_top_20_popular_books():
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=';')
        
        next(reader)
        
        books = []
        
        for row in reader:
            title = row[1]  
            author = row[2]  
            downloads = int(row[5])  
            books.append((title, author, downloads))
        
        sorted_books = sorted(books, key=lambda x: x[2], reverse=True)
        
        top_20_books = sorted_books[:20]
        
        print("Топ-20 самых популярных книг:")
        for i, (title, author, downloads) in enumerate(top_20_books, start=1):
            print(f"{i}. {title} by {author} (Загрузок: {downloads})")

get_top_20_popular_books()