#by croo
from pymongo import MongoClient
from datetime import date
import datetime
import subprocess
import gridfs

def CURRENT_DAY():
    return date.today().strftime("%B %d %Y") #should be month day year ie January 2 2023
#subprocess.run('md "C:\\data\\db"', shell=True) #do this manually as to not overwrite
#subprocess.run('C:\\Program Files\\MongoDB\\Server\\6.0\\bin\\mongod.exe --dbpath="C:\data\db"', shell=True)
#command = 'md "C:\\data\\db"'
#subprocess.run(['runas', '/user:Administrator', command], shell=True)

subprocess.run(['runas', '/user:Administrator', 'C:\\Program Files\\MongoDB\\Server\\6.0\\bin\\mongod.exe --dbpath="C:\data\db"'], shell=True)

#uri format: client = MongoClient("mongodb://localhost:27017/")
#below is the same as: client = MongoClient("localhost", 27017)

try:
    client = MongoClient()
except:
    print("Could not connect to MongoDB")

#move old data to relational db
db = client.master_database

collection = db[CURRENT_DAY()]
""" If your database name is such that using attribute style access won’t work
(like test-database), you can use dictionary style access instead:
db = client["test-database"] """

# test entry data
post = {

    "author": "Mike",

    "text": "My first blog post!",

    "tags": ["mongodb", "python", "pymongo"],

    "date": datetime.datetime.now(tz=datetime.timezone.utc), #or date.today()

}

posts = db.posts

post_id = posts.insert_one(post).inserted_id

#todo:
#below is how to update
""" filter = { 'appliance': 'fan' } #looks for the entry (think json) with a key: value that matches this

newvalues = { "$set": { 'quantity': 25 } } #$set is to update & then key: value

posts.update_one(filter, newvalues) """

result = collection.delete_one({"name": "Mr.Coder"})

""" # Check if the delete operation was successful
if result.deleted_count == 1:
    print("Document deleted successfully.")
else:
    print("No document was deleted.") """

#TODO: move all CRUD stuff into individual functions for error catching

#TODO: make face detection a thread
#TODO: need error catching here
fs = gridfs.GridFS(db)

i_names = [''] # here needs to be a dynamic way to read images
                # (possibly look for changes or figure out how the camera module will save the iamges)

image_data = open('/home/jimbo/faces/1.jpeg')# or just the directory: '/home/jimbo/faces' + i_names[-1])

new_image = fs.put(image_data.read(), filename = i_names[-1])