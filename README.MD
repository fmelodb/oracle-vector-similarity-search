# Oracle Vector - Similarity Search Demo

It demonstrates how you can perform similarity search on Oracle AI Vector Search using Python (no framework).

---

## 🚀 Getting Started

You can quickly get an image of Oracle Graph Server (using Podman):

- [Oracle Container Registry](https://container-registry.oracle.com)  Go to **Database > free (23ai)**

```sh
podman run --name oracle32aifree -p 1521:1521 -e ORACLE_PWD=password container-registry.oracle.com/database/free:latest
```

Run the script [`hopcroftkarp.sql`](hopcroftkarp.sql) using `sqlcl` or `sqlplus`.

---

## 📋 Steps

# 1. load sample data
```sh
python schema_setup.py
```

# 2. vectorize the data using a transformers model
```sh
python vectorize_table_SentenceTransformers.py
```

# 3. perform similarity search
```sh
python similarity_search_SentenceTransformers.py
```