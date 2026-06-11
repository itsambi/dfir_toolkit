import pandas as pd

def build_timeline(metadata_results, history_df, downloads_df):

    timeline = []

    # File metadata events
    timeline.append({
        "Event Type": "File Created",
        "Timestamp": metadata_results.get("Created Time"),
        "Details": metadata_results.get("File Name"),
        "Severity": "LOW"
    })

    timeline.append({
        "Event Type": "File Modified",
        "Timestamp": metadata_results.get("Modified Time"),
        "Details": metadata_results.get("File Name"),
        "Severity": "LOW"
    })

    # Browser history events
    for _, row in history_df.head(5).iterrows():

        severity = "LOW"

        url = str(row["url"]).lower()

        suspicious_keywords = [
            "mega",
            "pastebin",
            "anonfiles",
            "temp-mail",
            "dark"
        ]

        for keyword in suspicious_keywords:
            if keyword in url:
                severity = "HIGH"

        timeline.append({
            "Event Type": "Browser Visit",
            "Timestamp": row["last_visit_time"],
            "Details": row["url"],
            "Severity": severity
        })

    # Download events
    for _, row in downloads_df.head(5).iterrows():

        severity = "LOW"

        target = str(row["target_path"]).lower()

        suspicious_extensions = [
            ".exe",
            ".bat",
            ".cmd",
            ".ps1",
            ".scr"
        ]

        for ext in suspicious_extensions:
            if target.endswith(ext):
                severity = "HIGH"

        timeline.append({
            "Event Type": "Download",
            "Timestamp": row["start_time"],
            "Details": row["target_path"],
            "Severity": severity
        })

    timeline_df = pd.DataFrame(timeline)

    return timeline_df