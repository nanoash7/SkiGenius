from database import create,insert
import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv('MONGO_URI')
client = create.connect_to_db(URI)
db = create.create_db("ski_info",client)
collection = create.create_collection("ski_info","resorts")
# TODO: Add snow amount and calculated difficulty column to the db
columns = ["Season","Difficulty","Latitude_y","Longitude_y"]
insert.insert_records(collection,"../data/df_merged.csv",columns)