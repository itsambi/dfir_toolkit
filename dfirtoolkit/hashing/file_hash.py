import hashlib
import os

def calculate_hashes(file_path):

    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                md5_hash.update(chunk)
                sha1_hash.update(chunk)
                sha256_hash.update(chunk)

        file_size = os.path.getsize(file_path)

        return {
            "File": file_path,
            "Size": file_size,
            "MD5": md5_hash.hexdigest(),
            "SHA1": sha1_hash.hexdigest(),
            "SHA256": sha256_hash.hexdigest()
        }

    except FileNotFoundError:
        return {"Error": "File not found"}

    except Exception as e:
        return {"Error": str(e)}