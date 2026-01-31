import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.excpetion import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        def cv_to_json_convertor(self,file_path):
            try:
                data=pd.read_csv(file_path)
                data.reset_index(drop=True,inplace=True)
                records=list(json.loads(data.T.to_json()).values())
            except Exception as e:
                raise NetworkSecurityException(e,sys)   
            
        def insert_record_mongodb(self,records,db_name,collection_name):
            try:
                self.database_name=db_name
                self.collection_name=collection_name
                self.records=records
                self.client=pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
                self.database=self.mongo_client[self.database_name]
                self.collection=self.database[self.collection_name]
                self.collection.insert_many(self.records)
                return(len(self.records))
            except Exception as e:
                raise NetworkSecurityException(e,sys)

if __name__=='__main__':
    file_path="Network_Data\phisingData.csv"
    database="souvikai"
    collection="NetworkData"
    networkobj=NetworkDataExtract()
    networkobj.cv_to_json_convertor(file_path)
    records=networkobj.cv_to_json_convertor(file_path)
    count=networkobj.insert_record_mongodb(records,database,collection)
    print(f"Total records inserted to mongodb is {count}")            