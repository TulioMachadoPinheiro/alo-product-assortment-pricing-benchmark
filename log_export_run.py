import csv
import os
from datetime import datetime

LOG_FILE = "logs/export_runs_log.csv"

def log_export_run(script_name, input_rows, detail_rows_exported, summary_rows_exported, rows_discarded):
    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "script_name",
                "input_rows",
                "detail_rows_exported",
                "summary_rows_exported",
                "rows_discarded"
            ])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            script_name,
            input_rows,
            detail_rows_exported,
            summary_rows_exported,
            rows_discarded
        ])