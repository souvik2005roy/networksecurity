from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

username = quote_plus("souvikroy0946_db_user")
password = quote_plus("souvikmr")  

uri = f"mongodb+srv://{username}:{password}@cluster0.kp1tarm.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
