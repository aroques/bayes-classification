import csv
from collections import defaultdict


class Dataset:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.rows = self.get_rows()
        self.column_headers = self.rows.pop(0)
        self.columns = self.get_columns()
        self.categorical_columns = 0
        self.continuous_columns = 0

    def get_rows(self):
        """Returns the dataset's rows"""
        with open(self.csv_file) as f:
            reader = csv.reader(f)
            rows = list(reader)
            rows = [row[1:] for row in rows]  # Slice each row to remove ids
            return self.convert_to_numerical(rows)

    @staticmethod
    def convert_to_numerical(rows):
        """Converts any data that can be to float"""
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                try:
                    rows[i][j] = float(col)
                except ValueError:
                    pass
        return rows

    def get_columns(self):
        """Returns the dataset's columns"""
        columns = defaultdict(list)
        for row in self.rows:
            for i, col in enumerate(row):
                columns[i].append(col)
        return columns

    @staticmethod
    def binarize(rows):
        """Converts any data that can be to float"""
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                try:
                    rows[i][j] = float(col)
                except ValueError:
                    pass
        return rows

    @property
    def cls(self):
        """Returns the last column of the dataset"""
        return self.columns[len(self.rows[0]) - 1]


