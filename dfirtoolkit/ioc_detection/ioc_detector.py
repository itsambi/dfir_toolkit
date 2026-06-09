import os

def detect_iocs(file_path):

    findings = []

    filename = os.path.basename(file_path).lower()

    suspicious_names = [
        "mimikatz",
        "powershell",
        "cmd",
        "ransom",
        "backdoor",
        "payload",
        "keylogger"
    ]

    suspicious_extensions = [
        ".exe",
        ".bat",
        ".cmd",
        ".scr",
        ".ps1"
    ]

    for keyword in suspicious_names:
        if keyword in filename:
            findings.append(
                f"HIGH IOC: Suspicious keyword '{keyword}' found"
            )

    for ext in suspicious_extensions:
        if filename.endswith(ext):
            findings.append(
                f"HIGH IOC: Executable extension '{ext}'"
            )

    if filename.count(".") > 1:
        findings.append(
            "CRITICAL IOC: Double extension detected"
        )

    if not findings:
        findings.append(
            "No IOC indicators found"
        )

    return findings