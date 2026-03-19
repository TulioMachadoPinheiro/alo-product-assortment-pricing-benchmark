# ALO Product Assortment & Pricing Benchmark Dashboard

Tableau dashboard benchmarking ALO, Lululemon, and Vuori across pricing, category mix, and assortment depth.

## Project Overview
This project analyzes how ALO is positioned relative to key athleisure competitors by comparing product assortment and pricing across five categories:
- Leggings
- Sports Bras
- Tops
- Shorts
- Outerwear

The workflow included:
- scraping public product data with Python and Playwright
- cleaning and deduplicating the dataset
- loading the final dataset into SQLite for analysis
- building an interactive Tableau dashboard

## Tools Used
- Python
- Playwright
- SQLite
- Tableau

## Dashboard Questions
This dashboard answers:
- Which brand has the highest average price?
- How does average price differ by category?
- How are products distributed across price bands?
- Which categories are broader or narrower by brand?

## Key Findings
- ALO has the highest average price in the final sample.
- ALO is especially premium in leggings, shorts, and sports bras.
- Outerwear is premium across all three brands.
- Vuori has the broadest tops assortment in the sample.

## Files
- `tableau/ALO_Product_Assortment_Pricing.twbx` – Tableau workbook
- `tableau/products_detail_tableau.csv` – detail-level Tableau dataset
- `tableau/products_summary_tableau.csv` – summary Tableau dataset
- `data_clean/all_brands_products_deduped.csv` – final cleaned and deduplicated dataset

## Tableau Public
[View the interactive dashboard here](https://public.tableau.com/app/profile/tulio.machado.pinheiro/viz/ALOProductAssortmentPricingBenchmarkDashboard/ALOProductAssortmentPricingBenchmarkDashboard?publish=yes)

## Preview

![Dashboard Preview](dashboard-preview.png)
