import os

def export_report(dataframe, report_name):

    try:
        output_folder = "reports"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_path = f"{output_folder}/{report_name}.csv"

        dataframe.to_csv(output_path, index=False)

        return f"Report exported successfully: {output_path}"

    except Exception as e:
        return f"Export Error: {str(e)}"