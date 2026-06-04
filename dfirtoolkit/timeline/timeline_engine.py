import pandas as pd

def build_timeline(metadata_results, history_df, downloads_df):

    timeline = []

    # File metadata events
    timeline.append({
        "Event Type": "File Created",
        "Timestamp": metadata_results.get("Created Time"),
        "Details": metadata_results.get("File Name")
    })

    timeline.append({
        "Event Type": "File Modified",
        "Timestamp": metadata_results.get("Modified Time"),
        "Details": metadata_results.get("File Name")
    })

    # Browser history events
    if isinstance(history_df, pd.DataFrame):

        for _, row in history_df.head(5).iterrows():

            timeline.append({
                "Event Type": "Browser Visit",
                "Timestamp": row["last_visit_time"],
                "Details": row["url"]
            })

    # Download events
    if isinstance(downloads_df, pd.DataFrame):

        for _, row in downloads_df.head(5).iterrows():

            timeline.append({
                "Event Type": "Download",
                "Timestamp": row["start_time"],
                "Details": row["target_path"]
            })

    timeline_df = pd.DataFrame(timeline)

    return timeline_df