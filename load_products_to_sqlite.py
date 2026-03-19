import csv
import sqlite3

INPUT_CSV = "data_clean/all_brands_products_deduped.csv"
DB_FILE = "sql/alo_competitor_pricing.db"
TABLE_NAME = "products"

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

cur.execute(f"""
CREATE TABLE {TABLE_NAME} (
    brand TEXT,
    product_name TEXT,
    category_raw TEXT,
    category_standardized TEXT,
    price_text TEXT,
    price INTEGER,
    product_url TEXT,
    source_website TEXT,
    scrape_date TEXT
)
""")

with open(INPUT_CSV, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = [
        (
            row["brand"],
            row["product_name"],
            row["category_raw"],
            row["category_standardized"],
            row["price_text"],
            int(row["price"]) if str(row["price"]).strip() else None,
            row["product_url"],
            row["source_website"],
            row["scrape_date"],
        )
        for row in reader
    ]

cur.executemany(f"""
INSERT INTO {TABLE_NAME} (
    brand,
    product_name,
    category_raw,
    category_standardized,
    price_text,
    price,
    product_url,
    source_website,
    scrape_date
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", rows)

conn.commit()

count = cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}").fetchone()[0]
print(f"Loaded {count} rows into {DB_FILE}, table: {TABLE_NAME}")

conn.close()