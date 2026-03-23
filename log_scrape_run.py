import csv
import os
from datetime import datetime

LOG_FILE = "logs/scrape_runs_log.csv"

def log_scrape_run(script_name, brand, category, rows_collected, rows_saved):
    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "script_name",
                "brand",
                "category",
                "rows_collected",
                "rows_saved"
            ])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            script_name,
            brand,
            category,
            rows_collected,
            rows_saved
        ])