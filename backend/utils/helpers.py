import csv

def extract_data_from_csv(filename):
    """
    Extract data from a CSV file and return it as a list of dictionaries.
    
    Args:
    filename (str): The name of the CSV file to extract data from.
    
    Returns:
    list: A list of dictionaries where each dictionary represents a row of data from the CSV file.
    """
    data = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(dict(row))
    return data
