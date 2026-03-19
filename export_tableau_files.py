import csv
import sqlite3

DB_FILE = "sql/alo_competitor_pricing.db"

DETAIL_OUTPUT = "tableau/products_detail_tableau.csv"
SUMMARY_OUTPUT = "tableau/products_summary_tableau.csv"

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

detail_query = """
SELECT
    brand,
    product_name,
    category_standardized,
    price,
    product_url,
    source_website,
    scrape_date
FROM products
WHERE price IS NOT NULL
ORDER BY brand, category_standardized, price DESC
"""

summary_query = """
SELECT
    brand,
    category_standardized,
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY brand),
        2
    ) AS category_share_pct
FROM products
WHERE price IS NOT NULL
GROUP BY brand, category_standardized
ORDER BY category_standardized, avg_price DESC
"""

detail_rows = cur.execute(detail_query).fetchall()
detail_cols = [d[0] for d in cur.description]

with open(DETAIL_OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(detail_cols)
    writer.writerows(detail_rows)

summary_rows = cur.execute(summary_query).fetchall()
summary_cols = [d[0] for d in cur.description]

with open(SUMMARY_OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(summary_cols)
    writer.writerows(summary_rows)

print(f"Exported {len(detail_rows)} detail rows to {DETAIL_OUTPUT}")
print(f"Exported {len(summary_rows)} summary rows to {SUMMARY_OUTPUT}")

conn.close()