import csv
import sys
from collections import defaultdict

INPUT_CSV = "data_clean/all_brands_products_deduped.csv"

errors = []
brand_category_counts = defaultdict(int)

with open(INPUT_CSV, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader, start=2):  # row 1 is header
        brand = row["brand"].strip()
        category = row["category_standardized"].strip()
        price_raw = row["price"].strip()
        product_url = row["product_url"].strip()
        product_name = row["product_name"].strip()

        brand_category_counts[(brand, category)] += 1

        if not product_name:
            errors.append(f"Row {i}: missing product_name")

        if not product_url:
            errors.append(f"Row {i}: missing product_url")

        if not price_raw:
            errors.append(f"Row {i}: missing price")
        else:
            try:
                price = float(price_raw)
                if price < 0:
                    errors.append(f"Row {i}: negative price {price}")
            except ValueError:
                errors.append(f"Row {i}: invalid price '{price_raw}'")

# Minimum expected counts per brand-category
minimum_expected = {
    ("ALO", "Leggings"): 10,
    ("ALO", "Sports Bras"): 10,
    ("ALO", "Tops"): 10,
    ("ALO", "Shorts"): 10,
    ("ALO", "Outerwear"): 10,
    ("Vuori", "Leggings"): 10,
    ("Vuori", "Sports Bras"): 10,
    ("Vuori", "Tops"): 10,
    ("Vuori", "Shorts"): 10,
    ("Vuori", "Outerwear"): 10,
    ("lululemon", "Leggings"): 10,
    ("lululemon", "Sports Bras"): 10,
    ("lululemon", "Tops"): 10,
    ("lululemon", "Shorts"): 10,
    ("lululemon", "Outerwear"): 10,
}

for key, minimum in minimum_expected.items():
    actual = brand_category_counts.get(key, 0)
    if actual < minimum:
        errors.append(
            f"Low count for {key[0]} / {key[1]}: found {actual}, expected at least {minimum}"
        )

if errors:
    print("VALIDATION FAILED\n")
    for err in errors:
        print("-", err)
    sys.exit(1)
else:
    print("VALIDATION PASSED\n")
    print("Counts by brand/category:")
    for key in sorted(brand_category_counts):
        print(f"- {key[0]} / {key[1]}: {brand_category_counts[key]}")