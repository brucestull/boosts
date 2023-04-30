import pymongo
import sys
import os


######################################################
# This section is only needed if your IDE does not automatically load
# environment variables from the .env file.
######################################################

# os.environ['DOTENV_LOAD'] = 'False'

# # If we are in a local environment, load the environment variables
# from the .env file.
# if os.getenv("LOCAL_ENVIRONMENT") == "TRUE":
#     from dotenv import load_dotenv

#     load_dotenv()
######################################################

mongo_db_username = os.getenv("MONGO_DB_USERNAME")
mongo_db_password = os.getenv("MONGO_DB_PASSWORD")
mongo_cluster_url = os.getenv("MONGO_CLUSTER_URL")

# Try to create a new client instance of `pymongo.MongoClient`:
try:
    client = pymongo.MongoClient(
        f"mongodb+srv://{mongo_db_username}:{mongo_db_password}@{mongo_cluster_url}/?retryWrites=true&w=majority"
    )
    print("Connected successfully!!!")

# return a friendly error if a URI error is thrown
except pymongo.errors.ConfigurationError:
    print(
        "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
    )
    sys.exit(1)

# Create/use a database named "boostsDatabase"
db = client.boostsDatabase

# Create/use a collection named "boostsCollection" which is part of the "boostsDatabase" database.
boosts_collection = db["boostsCollection"]

local_environment = os.getenv("LOCAL_ENVIRONMENT")

# Create a single document to insert into the collection.
boosts_documents = [
    {
        "local_environment": local_environment,
    },
    {
        "application": "boosts",
    }
]

# Try to drop the collection in case it already exists.
try:
    boosts_collection.drop()
    print("Collection dropped")
# Throw an exception if `boosts_collection` collection does not exist.
except pymongo.errors.OperationFailure:
    print("Collection does not exist")
    sys.exit(1)

# Try to insert the documents into the collection.
try:
    result = boosts_collection.insert_many(boosts_documents)
    print(f"Multiple documents: {result.inserted_ids}")
# Throw an exception on a BulkWriteError.
except pymongo.errors.BulkWriteError as e:
    print(e.details["writeErrors"][0]["errmsg"])
    sys.exit(1)
# Throw an exception if an `OperationFailure` is raised.
except pymongo.errors.OperationFailure as e:
    print(f"Invalid insert operation: {e}")
    sys.exit(1)
# If the documents are successfully inserted, print out the number of documents inserted.
else:
    inserted_count = len(result.inserted_ids)
    print(f"{inserted_count} documents successfully inserted")
    print("\n")

print("Done!")
