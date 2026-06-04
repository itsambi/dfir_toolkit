import os

SUSPICIOUS_EXTENSIONS = [
    ".exe",
    ".bat",
    ".scr",
    ".vbs",
    ".ps1",
    ".dll"
]

def analyze_file(file_path):

    findings = []

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # Check suspicious extensions
    extension = os.path.splitext(file_name)[1].lower()

    if extension in SUSPICIOUS_EXTENSIONS:
        findings.append(f"Suspicious executable extension detected: {extension}")

    # Check double extensions
    parts = file_name.split(".")

    if len(parts) > 2:
        findings.append("Possible double extension detected")

    # Check hidden files
    if file_name.startswith("."):
        findings.append("Hidden file detected")

    # Check unusually large files
    if file_size > 50 * 1024 * 1024:
        findings.append("Large file detected (>50MB)")

    if not findings:
        findings.append("No obvious suspicious indicators found")

    return findings