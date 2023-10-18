import csv

class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        csv_data = []
        with open(self.filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                csv_data.append(row)
        return csv_data