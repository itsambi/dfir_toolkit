from hashing.file_hash import calculate_hashes
from metadata.file_metadata import get_file_metadata
from analysis.suspicious_detector import analyze_file
from browser_forensics.chrome_history import extract_chrome_history
from browser_forensics.downloads_history import extract_download_history
from timeline.timeline_engine import build_timeline
from reporting.report_exporter import export_report
from risk_engine.risk_scoring import calculate_risk

file_path = input("Enter file path: ")

# Analysis
hash_results = calculate_hashes(file_path)
metadata_results = get_file_metadata(file_path)
analysis_results = analyze_file(file_path)
risk_results = calculate_risk(file_path)

# Browser artifacts
history_data = extract_chrome_history()
download_data = extract_download_history()

# Timeline
timeline_df = build_timeline(
    metadata_results,
    history_data,
    download_data
)

# HASH REPORT
print("\n--- FORENSIC HASH REPORT ---\n")

for key, value in hash_results.items():
    print(f"{key}: {value}")

# METADATA REPORT
print("\n--- FILE METADATA REPORT ---\n")

for key, value in metadata_results.items():
    print(f"{key}: {value}")

# SUSPICIOUS ANALYSIS
print("\n--- SUSPICIOUS FILE ANALYSIS ---\n")

for item in analysis_results:
    print(f"[!] {item}")

# RISK ASSESSMENT
print("\n--- RISK ASSESSMENT ---\n")

print(f"Risk Score : {risk_results['Risk Score']}")
print(f"Risk Level : {risk_results['Risk Level']}")

print("\nFindings:")

if risk_results["Findings"]:
    for finding in risk_results["Findings"]:
        print(f"[!] {finding}")
else:
    print("No risk indicators detected")

# CHROME HISTORY
print("\n--- CHROME HISTORY FORENSICS ---\n")
print(history_data)

# DOWNLOAD FORENSICS
print("\n--- DOWNLOAD FORENSICS ---\n")
print(download_data)

# TIMELINE
print("\n--- FORENSIC TIMELINE RECONSTRUCTION ---\n")
print(timeline_df)

# EXPORT REPORTS
print("\n--- EXPORTING REPORTS ---\n")

timeline_export = export_report(
    timeline_df,
    "forensic_timeline"
)

history_export = export_report(
    history_data,
    "browser_history"
)

download_export = export_report(
    download_data,
    "download_history"
)

print(timeline_export)
print(history_export)
print(download_export)