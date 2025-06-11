# Oracle Vector - Similarity Search Demo

It demonstrates how you can perform similarity search on Oracle AI Vector Search using Python.

---

## 🚀 Getting Started

You can quickly get an image of Oracle Graph Server (using Podman):

- [Oracle Container Registry](https://container-registry.oracle.com)  Go to **Database > free (23ai)**

```sh
podman run --name oracle32aifree -p 1521:1521 -e ORACLE_PWD=password container-registry.oracle.com/database/free:latest
```

## 📋 Steps

Load sample data:
```sh
python schema_setup.py
```

Vectorize the data using a transformer model:
```sh
python vectorize_table_SentenceTransformers.py
```

Perform similarity search:
```sh
python similarity_search_SentenceTransformers.py
```
