import csv


class Dataset:
    def __init__(self, csv_file, column_type):
        """Accepts a csv file and a list of what data type the columns are (binary, categorical (string),
            or continuous) """
        # The functions in this __init__ are temporally coupled
        # The order in which they are called does matter
        self.csv_file = csv_file
        self.column_type = column_type
        self.rows = self.get_rows()
        self.column_headers = self.rows.pop(0)
        self.columns = self.get_columns()
        self.convert_to_type()
        self.cls = self.columns.pop()
        self.cls_type = self.column_type.pop()

    def columns_that_are(self, column_type):
        """Returns columns that are of a certain type (based on self.column_type)"""
        ret = []
        for i, ct in enumerate(self.column_type):
            if ct == column_type:
                ret.append(self.columns[i])
        return ret

    def get_rows(self):
        """Returns the dataset's rows"""
        with open(self.csv_file) as f:
            reader = csv.reader(f)
            return [row[1:] for row in list(reader)]  # Slice each row to remove ids

    def convert_to_type(self):
        """Converts continuous data to floating type, and binary data into bool type"""
        for i, ct in enumerate(self.column_type):
            if ct == 'continuous':
                self.columns[i] = list(map(float, self.columns[i]))
            elif ct == 'binary':
                self.columns[i] = list(map(int, self.columns[i]))
                self.columns[i] = list(map(bool, self.columns[i]))
        self.rows = list(zip(*self.columns))

    def get_columns(self):
        """Returns the dataset's columns"""
        return list(zip(*self.rows))
