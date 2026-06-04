import os
import time

def get_file_metadata(file_path):

    try:
        stats = os.stat(file_path)

        metadata = {
            "File Name": os.path.basename(file_path),
            "Absolute Path": os.path.abspath(file_path),
            "File Size (Bytes)": stats.st_size,
            "Created Time": time.ctime(stats.st_ctime),
            "Modified Time": time.ctime(stats.st_mtime),
            "Last Accessed": time.ctime(stats.st_atime),
            "File Extension": os.path.splitext(file_path)[1]
        }

        return metadata

    except FileNotFoundError:
        return {"Error": "File not found"}

    except Exception as e:
        return {"Error": str(e)}