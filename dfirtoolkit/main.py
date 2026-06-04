from hashing.file_hash import calculate_hashes
from metadata.file_metadata import get_file_metadata
from analysis.suspicious_detector import analyze_file
from browser_forensics.chrome_history import extract_chrome_history
from browser_forensics.downloads_history import extract_download_history
from timeline.timeline_engine import build_timeline
from reporting.report_exporter import export_report
from risk_engine.risk_scoring import calculate_risk
file_path = input("Enter file path: ")

hash_results = calculate_hashes(file_path)
metadata_results = get_file_metadata(file_path)
analysis_results = analyze_file(file_path)

risk_results = calculate_risk(file_path)

history_data = extract_chrome_history()
download_data = extract_download_history()

timeline_df = build_timeline(metadata_results, history_data, download_data)

print("\n--- FORENSIC HASH REPORT ---\n")

for key, value in hash_results.items():
    print(f"{key}: {value}")

print("\n--- FILE METADATA REPORT ---\n")

for key, value in metadata_results.items():
    print(f"{key}: {value}")

    print("\n--- SUSPICIOUS FILE ANALYSIS ---\n")

analysis_results = analyze_file(file_path)

for item in analysis_results:
    print(f"[!] {item}")


for item in analysis_results:
    print(f"[!] {item}")

    print("\n--- RISK ASSESSMENT ---\n")

print(f"Risk Score : {risk_results['Risk Score']}")
print(f"Risk Level : {risk_results['Risk Level']}")

print("\nFindings:")

if risk_results["Findings"]:
    for finding in risk_results["Findings"]:
        print(f"[!] {finding}")
else:
    print("No risk indicators detected")

    print("\n--- CHROME HISTORY FORENSICS ---\n")

history_data = extract_chrome_history()

print(history_data)

print("\n--- DOWNLOAD FORENSICS ---\n")

download_data = extract_download_history()

print(download_data)

print("\n--- FORENSIC TIMELINE RECONSTRUCTION ---\n")

timeline_df = build_timeline(
    metadata_results,
    history_data,
    download_data
)

print(timeline_df)

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