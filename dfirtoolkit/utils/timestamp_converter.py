from datetime import datetime, timedelta

def chrome_time_to_datetime(chrome_time):

    try:
        if chrome_time == 0:
            return "N/A"

        epoch_start = datetime(1601, 1, 1)

        converted_time = epoch_start + timedelta(
            microseconds=int(chrome_time)
        )

        return converted_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    except Exception:
        return "Invalid Timestamp"