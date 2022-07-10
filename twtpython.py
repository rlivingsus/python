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

#here we are connecting to my Books DB using the client object created previously then method to list collections name and print
book_db = client.Books
collections = book_db.list_collection_names()
#print(collections)

def insert_doc():
    collection = book_db.Books_Read
    test_document = {
        "First_Name": "Anne", 
        "Last_Name": "McCaffrey", 
        "Book_Title": "Nerilka's Story", 
        "Book_Series": "Dragonriders of Pern Sixth Pass", 
        "Subject": "Fantasy", 
        "Type": "e-book", 
        "End_Date": datetime.fromisoformat('2022-06-23'), 
        "Summary": "Book 8, simultaneous story of Moreta but the story is about Nerilka one of the daughter's of a lord holder who chases her away and she ends up helping Ruatha? hold" 
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

#uncomment when we want to insert an item
#insert_doc()

#creating a query function
def find_all_books():
