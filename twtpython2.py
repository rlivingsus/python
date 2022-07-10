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
        "First_Name": "Robert", 
        "Last_Name": "Jordan", 
        "Book_Title": "Lord of Chaos", 
        "Book_Series": "The Wheel of Time", 
        "Subject": "Fantasy", 
        "Type": "Audio", 
        "End_Date": datetime.fromisoformat('2022-07-03'), 
        "Summary": "Book6, Rand controls Andor and start up training of me saidin army with maizim tain; matrim distract with his red palm army; Perrin and lady falcon ruling in that part and meet up with Rand while Mat leads Elaine and Nynaeve to a city with a magical bowl.  Egwene becomes Amrylin Seat for the Rebels" 
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

#creating a query function
#def find_all_books():

def main():

    #uncomment when we want to insert an item
    insert_doc()

if __name__ == '__main__':
    main()