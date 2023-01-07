import xml.etree.ElementTree as E
import csv 
tree = E.parse('givenfile.xml')
root = tree.getroot()


with open('outputfile.csv', 'w', newline='') as file:

    output = csv.writer(file)


    output.writerow(['book_id', 'author_name', 'title', 'genre', 'price', 'publish_date', 'description'])
    for data in tree.findall('book'):
        bid = data.get('id')
        a_name  = data.find('author').text
        title = data.find('title').text
        genre = data.find('genre').text
        price = data.find('price').text
        date = data.find('publish_date').text
        des = data.find('description').text
        output.writerow([bid, a_name, title, genre, price, date, des])
        print("What we are writing in the file")
        print([bid, a_name, title, genre, price, date, des])
