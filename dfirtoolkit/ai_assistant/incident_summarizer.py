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
            "The file contains indicators that warrant further review."
        )

    else:
        report.append(
            "No major indicators of malicious activity were identified."
        )

    report.append("")
    report.append("Recommended Actions:")

    recommendations = []

    for item in ioc_results:

        item_lower = item.lower()

        if "double extension" in item_lower:
            recommendations.append(
                "Investigate possible phishing or masquerading techniques."
            )

        if ".exe" in item_lower:
            recommendations.append(
                "Review process execution logs for executable activity."
            )

        if "powershell" in item_lower:
            recommendations.append(
                "Inspect PowerShell command history."
            )

    if risk_score >= 60:
        recommendations.append(
            "Consider isolating the affected endpoint."
        )

    recommendations.append(
        "Preserve evidence for further investigation."
    )

    recommendations = list(set(recommendations))

    for index, recommendation in enumerate(recommendations, start=1):
        report.append(
            f"{index}. {recommendation}"
        )

    return "\n".join(report)