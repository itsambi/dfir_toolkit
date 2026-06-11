def generate_incident_summary(
    risk_results,
    ioc_results,
    timeline_df,
    metadata_results
):

    report = []

    filename = metadata_results.get(
        "File Name",
        "Unknown File"
    )

    risk_level = risk_results["Risk Level"]
    risk_score = risk_results["Risk Score"]

    report.append(
        f"The analyzed file '{filename}' was investigated."
    )

    report.append("")

    report.append("Evidence Identified:")

    for item in ioc_results:
        if "No IOC" not in item:
            report.append(f"- {item}")

    report.append(
        f"- Risk Score: {risk_score} ({risk_level})"
    )

    report.append("")

    report.append("Assessment:")

    if risk_score >= 60:

        report.append(
            "The file exhibits characteristics commonly associated with suspicious or potentially malicious activity."
        )

    elif risk_score >= 30:

        report.append(
            "The file contains several indicators that warrant additional review."
        )

    else:

        report.append(
            "No major indicators of malicious activity were identified."
        )

    report.append("")

    report.append("Recommended Actions:")

    report.append(
        "1. Preserve the file as evidence."
    )

    report.append(
        "2. Review execution history."
    )

    report.append(
        "3. Investigate related downloads."
    )

    report.append(
        "4. Review browser activity."
    )

    return "\n".join(report)