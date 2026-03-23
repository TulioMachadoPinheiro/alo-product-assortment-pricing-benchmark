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
ORDER BY category_standardized, avg_price DESC;