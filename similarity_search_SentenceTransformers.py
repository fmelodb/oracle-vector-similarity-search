import os
import array
import time
import oracledb
from sentence_transformers import SentenceTransformer, CrossEncoder
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

def connect_database():
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    dsn = os.getenv("DB_URL")
    try:
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        print("Connected to the Oracle Database!")
        return connection
    except Exception as e:
        print("Fail to connect to the database:", e)
        exit(1)

def main():
    topK = 3
    sql = """select info from test_data 
             order by vector_distance(embedding, :1, cosine)
             fetch first :2 rows only"""

    embedding_model_name = 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
    rerank_model_name = 'cross-encoder/mmarco-mMiniLMv2-L12-H384-v1'
    embedding_model = SentenceTransformer(embedding_model_name, trust_remote_code=False)

    print("Using embedding model:", embedding_model_name)
    print("Top K:", topK)

    connection = connect_database()

    with connection.cursor() as cursor:
        while True:
            input_text = input("Type search text ('exit' to quit): ")
            if input_text.lower() in ['exit', 'quit']:
                break

            rerank_input = input("Rerank? (y/n): ").strip().lower()
            rerank = rerank_input == 'y'

            input_vector = list(embedding_model.encode(input_text))
            input_vector_array = array.array('f', input_vector)

            docs = []
            cross = []

            tic = time.perf_counter()
            for info, in cursor.execute(sql, [input_vector_array, topK]):
                docs.append(info)
                if rerank:
                    cross.append([input_text, info])
            toc = time.perf_counter()
            print(f"\nElapsed Time: {toc - tic:0.3f} seconds.")

            if not rerank:
                print("\nResults without rerank:")
                for hit in docs:
                    print(hit)
            else:
                cross_encoder = CrossEncoder(rerank_model_name, max_length=512)
                scores = cross_encoder.predict(cross)
                reranked = sorted(zip(scores, docs), reverse=True, key=lambda x: x[0])
                print("\nResults with rerank:")
                for score, hit in reranked:
                    print(f"Score: {score:.4f} - {hit}")
            print()

if __name__ == "__main__":
    main()