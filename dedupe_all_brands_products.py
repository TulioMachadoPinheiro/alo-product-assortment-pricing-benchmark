import csv

INPUT_CSV = "data_clean/all_brands_products_clean.csv"
OUTPUT_CSV = "data_clean/all_brands_products_deduped.csv"

seen = set()
deduped_rows = []

with open(INPUT_CSV, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (
            row["brand"].strip(),
            row["product_name"].strip(),
            row["category_standardized"].strip(),
            str(row["price"]).strip(),
        )

        if key in seen:
            continue

        seen.add(key)
        deduped_rows.append(row)

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "brand",
            "product_name",
            "category_raw",
            "category_standardized",
            "price_text",
            "price",
            "product_url",
            "source_website",
            "scrape_date",
        ],
    )
    writer.writeheader()
    writer.writerows(deduped_rows)

print(f"Deduped to {len(deduped_rows)} rows into {OUTPUT_CSV}")
print("\nFirst 10 deduped rows:\n")
for row in deduped_rows[:10]:
    print(row)