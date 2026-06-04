import os

def calculate_risk(file_path):

    score = 0
    findings = []

    filename = os.path.basename(file_path).lower()

    suspicious_extensions = [
        ".exe",
        ".bat",
        ".scr",
        ".cmd",
        ".ps1"
    ]

    # Executable file
    for ext in suspicious_extensions:
        if filename.endswith(ext):
            score += 40
            findings.append("Executable file detected")
            break

    # Double extension
    parts = filename.split(".")

    if len(parts) > 2:
        score += 25
        findings.append("Double extension detected")

    # Large file
    try:
        size = os.path.getsize(file_path)

        if size > 50 * 1024 * 1024:
            score += 10
            findings.append("Large file size")

    except:
        pass

    if score >= 70:
        level = "HIGH"

    elif score >= 40:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "Risk Score": score,
        "Risk Level": level,
        "Findings": findings
    }