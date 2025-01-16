import csv
import random
import xml.dom.minidom as minidom


with open('books-en.csv', 'r', encoding='latin-1') as file:
    reader = csv.reader(file, delimiter=';')
    
    next(reader)
    
    count = 0
    
    for row in reader:
        if len(row[1]) > 30:
            count += 1

print(f"Количество записей с длиной названия более 30 символов: {count}")
print()


def search_books_by_author(author_name):
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=';')
        
        next(reader)
        
        results = []
        
        for row in reader:
            if row[2].lower() == author_name.lower():
                results.append({
                    'title': row[1],  
                    'year': row[3],   
                    'publisher': row[4],  
                    'downloads': row[5],  
                    'price': row[6]       
                })
        
        if results:
            print(f"Найдено {len(results)} книг автора {author_name}:")
            for book in results:
                print(f"Название: {book['title']}")
                print(f"Год издания: {book['year']}")
                print(f"Издательство: {book['publisher']}")
                print(f"Загрузок: {book['downloads']}")
                print(f"Цена: {book['price']}")
                print()
        else:
            print(f"Книги автора {author_name} не найдены.")

author_name = input("Введите имя автора для поиска: ")
search_books_by_author(author_name)


def generate_bibliographic_references(output_file, num_entries=20):
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=';')
        
        next(reader)
        
        all_entries = list(reader)
        
        selected_entries = random.sample(all_entries, num_entries)
        
        references = []
        for entry in selected_entries:
            author = entry[2]  
            title = entry[1]   
            year = entry[3]    
            reference = f"{author}. {title} - {year}"
            references.append(reference)
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for i, ref in enumerate(references, start=1):
                outfile.write(f"{i}. {ref}\n")
        
        print(f"Сгенерировано {num_entries} библиографических ссылок и сохранено в файл '{output_file}'.")
        print()

output_file = "bibliographic_references.txt"
generate_bibliographic_references(output_file)


doc = minidom.parse('currency.xml')

char_codes = []
values = []

valutes = doc.getElementsByTagName('Valute')
for valute in valutes:
    char_code = valute.getElementsByTagName('CharCode')[0].firstChild.data
    value = valute.getElementsByTagName('Value')[0].firstChild.data.replace(',', '.')  
    char_codes.append(char_code)
    values.append(float(value))

print("CharCodes:", char_codes)
print("Values:", values)
print()

