from database import create,insert
import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv('MONGO_URI')
client = create.connect_to_db(URI)
db = create.create_db("ski_info",client)
collection = create.create_collection(db,"resorts")
# TODO: Add snow amount and calculated difficulty column to the db
columns = ["Difficulty","Latitude","Longitude", "Open January","Open February", "Open March","Open April","Open May", "Open June", "Open July", "Open August", "Open September", "Open October", "Open November", "Open December"]
insert.insert_records(collection,"../data/df_merged_final.csv",columns)