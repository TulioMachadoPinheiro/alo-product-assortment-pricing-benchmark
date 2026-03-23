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
ORDER BY brand, category_standardized, price DESC;