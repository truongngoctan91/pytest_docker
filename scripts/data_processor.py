import csv


def csv_reader(file_location):

    with open(file_location, mode='r') as csv_file:
        data = [line for line in csv.DictReader(csv_file)]
        for row in data:
            try:
                row['Lat'] = float(row['Lat'])
                row['Long'] = float(row['Long'])
                row['Altitude'] = float(row['Altitude'])

            except (FileNotFoundError, ValueError) as exp:
                raise exp

        return data
