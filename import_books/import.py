import csv
from models import *
complate=0
with open('books.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(row['isbn']+"    "+row['title']+"    "+row['author']+"    "+row['year'])
        us=books(isbn=row['isbn'], title=row['title'],author=row['author'],year=row['year'])
        complate=complate+1
        try:
                print(complate)
                db.session.add(us)
                db.create_all()
                db.session.commit()
        except Exception as e:
             print(e)

        line_count += 1
    print(f'Processed {line_count} lines.')
    
    