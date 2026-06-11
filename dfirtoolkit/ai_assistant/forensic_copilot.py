def answer_question(
    question,
    risk_results,
    ioc_results,
    metadata_results
):

    question = question.lower()

    if "why" in question and "suspicious" in question:

        response = []

        response.append(
            f"File: {metadata_results['File Name']}"
        )

        response.append("")

        response.append(
            "The file was flagged because:"
        )

        for item in ioc_results:
            if "No IOC" not in item:
                response.append(
                    f"- {item}"
                )

        response.append(
            f"- Risk Score: {risk_results['Risk Score']}"
        )

        return "\n".join(response)

    elif "risk" in question:

        return (
            f"Risk Level: "
            f"{risk_results['Risk Level']}"
        )

    elif "ioc" in question:

        return "\n".join(ioc_results)

    else:

        return (
            "I could not understand the investigation query."
        )