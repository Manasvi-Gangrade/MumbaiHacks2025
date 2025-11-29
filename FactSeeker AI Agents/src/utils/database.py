import pymongo
from src.utils.config import Config

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        
    def connect(self):
        try:
            print(f"Connecting to MongoDB at {Config.MONGODB_URI}...")
            # For now, we will just print success. 
            # Uncomment the next lines when a real DB is available.
            # self.client = pymongo.MongoClient(Config.MONGODB_URI)
            # self.db = self.client[Config.DB_NAME]
            # self.collection = self.db["raw_data"]
            print("✅ Connected to Database (Mock Mode)")
        except Exception as e:
            print(f"❌ Database connection failed: {e}")

    def insert_data(self, data):
        """
        Insert a document into the database.
        """
        print(f"💾 Saving to DB: {data.get('content')[:30]}...")
        # if self.collection:
        #     self.collection.insert_one(data)

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.insert_data({"test": "data"})
