import pandas as pd


def export_results_to_excel(df, file_path='results.xlsx'):
    """
    Export the DataFrame to an Excel file.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the results.
    file_path (str): The path where the Excel file will be saved.
    """
    try:
        with pd.ExcelWriter(file_path) as writer:
            df.to_excel(writer, index=False, sheet_name='Results')
        print(f"Results successfully exported to {file_path}")
    except Exception as e:
        print(f"Error exporting results to Excel: {e}")
