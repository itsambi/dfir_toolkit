import os
import shutil
import sqlite3
import pandas as pd
from utils.timestamp_converter import chrome_time_to_datetime

def extract_download_history():

    history_path = os.path.expanduser(
        r"~\AppData\Local\Google\Chrome\User Data\Default\History"
    )

    if not os.path.exists(history_path):
        return "Chrome history database not found."

    temp_history = "temp_downloads"

    try:
        shutil.copy2(history_path, temp_history)

        connection = sqlite3.connect(temp_history)

        query = """
        SELECT
            downloads.target_path,
            downloads.tab_url,
            downloads.start_time
        FROM downloads
        ORDER BY downloads.start_time DESC
        LIMIT 10
        """

        df = pd.read_sql_query(query, connection)
        df["start_time"] = df["start_time"].apply(chrome_time_to_datetime)

        connection.close()

        os.remove(temp_history)

        return df

    except Exception as e:
        return f"Error: {str(e)}"