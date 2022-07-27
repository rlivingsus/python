from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

#grabbing PW from .env file
password = os.environ.get("MONGODB_PWD")

#print(password)
connection_string = f"mongodb+srv://rlivings:{password}@cluster0.mee6j.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

#to use list_database_names() method to see which DBs are out there.  Twelve so I deleted all the samples from the training.
dbs = client.list_database_names()
#print(dbs)

#here we are connecting to my Books database using the client object created previously then method to list collections name and print
book_db = client.Books
#collections = book_db.list_collection_names()
#print(collections)
book_collection = book_db.Books_Read   #to be used below in find_all_books()

#insert an item in a collection
#Books_Read collection is like a table in my Books DB
def insert_doc():
    collection = book_db.Books_Read
    test_document = {
        "First_Name": "Brandon", 
        "Last_Name": "Sanderson", 
        "Book_Title": "The Final Empire", 
        "Book_Series": "Mistborn", 
        "Subject": "Fantasy", 
        "Type": "Audio", 
        "End_Date": datetime.fromisoformat('2022-07-15'), 
        "Summary": "Book1, A world full of mist and ash ruled by the Hero of Ages, Lord Ruler who defeated an unknowned enemy 1000 years ago but now surpresses the SKAA lower caste people while certain higher caste folks are living well.  There are folks that hold power called allomancers who can burn metals internally to exhibit superpowers (this is heriditary).  Two of the high powered mistborns that are halfskaa plot to overthrow the Lord Ruler but aren't completely successful.  The army they put together and Eden (leader) conducts a premature attack which brings down most of their army." 
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

#pprinter declaration
printer = pprint.PrettyPrinter()

#creating a query find all books function
def find_all_books():
    all_books = book_collection.find()  #I originally tried to use find on a DB but it only works on a collection

    for book in all_books:
        printer.pprint(book)

#query function to find an author first instance using find_one() but find() will return all but error?
def find_author():
    author = book_collection.find({"First_Name": "Brandon"})
    
    for name in author:
        printer.pprint(name)

def main():
    #uncomment when we want to insert an item
    #insert_doc()

    #uncomment when we want to find all books
    #find_all_books()

    #uncomment when we want to find an author
    find_author()


if __name__ == '__main__':
    main()