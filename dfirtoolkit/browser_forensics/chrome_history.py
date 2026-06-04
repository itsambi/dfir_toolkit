import os
import shutil
import sqlite3
import pandas as pd
from utils.timestamp_converter import chrome_time_to_datetime

def extract_chrome_history():

    history_path = os.path.expanduser(
        r"~\AppData\Local\Google\Chrome\User Data\Default\History"
    )

    if not os.path.exists(history_path):
        return "Chrome history file not found."

    temp_history = "temp_history"

    try:
        # Copy database because Chrome locks original file
        shutil.copy2(history_path, temp_history)

        connection = sqlite3.connect(temp_history)

        query = """
        SELECT
            url,
            title,
            visit_count,
            last_visit_time
        FROM urls
        ORDER BY last_visit_time DESC
        LIMIT 10
        """

        df = pd.read_sql_query(query, connection)
        df["last_visit_time"] = df["last_visit_time"].apply(chrome_time_to_datetime)

    
        connection.close()

        os.remove(temp_history)

        return df

    except Exception as e:
        return f"Error: {str(e)}"