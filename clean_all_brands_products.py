import csv
import re

INPUT_CSV = "data_raw/all_brands_products_raw.csv"
OUTPUT_CSV = "data_clean/all_brands_products_clean.csv"

def clean_text(value):
    if value is None:
        return ""
    value = value.strip()
    value = value.replace("â„¢", "™")
    value = value.replace("â€“", "–")
    value = value.replace("â€™", "’")
    value = value.replace("Â", "")
    return value

def standardize_brand(value):
    v = clean_text(value).lower()
    if v == "alo":
        return "ALO"
    if v == "vuori":
        return "Vuori"
    if v == "lululemon":
        return "lululemon"
    return clean_text(value)

def standardize_category(value):
    v = clean_text(value).lower()
    if "legging" in v:
        return "Leggings"
    if "bra" in v:
        return "Sports Bras"
    if "short" in v:
        return "Shorts"
    if "top" in v:
        return "Tops"
    if "outerwear" in v:
        return "Outerwear"
    return clean_text(value)

def extract_price(price_text):
    text = clean_text(price_text)
    match = re.search(r"\$([0-9]+)", text)
    if match:
        return int(match.group(1))
    return ""

clean_rows = []

with open(INPUT_CSV, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        brand = standardize_brand(row.get("brand", ""))
        product_name = clean_text(row.get("product_name", ""))
        category_raw = clean_text(row.get("category_raw", ""))
        category_standardized = standardize_category(category_raw)
        price_text = clean_text(row.get("price_text", ""))
        price = extract_price(price_text)
        product_url = clean_text(row.get("product_url", ""))
        source_website = clean_text(row.get("source_website", ""))
        scrape_date = clean_text(row.get("scrape_date", ""))

        clean_rows.append({
            "brand": brand,
            "product_name": product_name,
            "category_raw": category_raw,
            "category_standardized": category_standardized,
            "price_text": price_text,
            "price": price,
            "product_url": product_url,
            "source_website": source_website,
            "scrape_date": scrape_date,
        })

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
    writer.writerows(clean_rows)

print(f"Cleaned {len(clean_rows)} rows into {OUTPUT_CSV}")
print("\nFirst 10 cleaned rows:\n")
for row in clean_rows[:10]:
    print(row)