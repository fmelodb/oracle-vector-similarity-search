import os
import oracledb
import sys
import array
import time
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

def connect_database():
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    dsn = os.getenv("DB_URL")

    try:
        connection = oracledb.connect(user=username, password=password, dsn=dsn)        
        print("Connection successful!")
        return connection
    except Exception as e:
        print("Connection failed!")
        
# select embedding model
model = 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
embedding_model = SentenceTransformer(model)        

connection = connect_database()
query_sql = "select id, info from test_data order by 1"
update_sql = "update test_data set embedding = :1 where id = :2"

with connection.cursor() as cursor:
    print("Vectorizing the following data:\n")

    #loop over the rows and vectorize the VARCHAR2 info column
    
    binds = []
    tic = time.perf_counter()
    
    for id_val, info in cursor.execute(query_sql):
        #convert input string format for SentenceTransformers
        data = f"[{info}]"
        #vectorize the input string
        embedding = list(embedding_model.encode(data))
        #convert to array of floats
        embedding_array = array.array('f', embedding)
        #append to binds list
        binds.append((embedding_array, id_val))
        
        print(info)
        
    toc = time.perf_counter()
    
    # update the database with the vectorized data
    cursor.executemany(update_sql, binds)
    connection.commit()
    print(f"\nVectorization completed in {toc - tic:0.3f} seconds.")
    print(f"\nAdded {len(binds)} vectors to the table using embedding model {model}\n")
    
    
    
        
        
    
        
    