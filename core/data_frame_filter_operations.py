class DataFrameFilterOperations:
    def __init__(self, *, data_frame):
        self.data_frame = data_frame

    def filter_by(self, *, column, operation, value):
        if type(value) == list and operation == "isin":
            self.data_frame = self.data_frame[self.data_frame[column].isin(value)]
        # ~ is a negation operator - creates a "notin" effect
        elif type(value) == list and operation == "notin":
            self.data_frame = self.data_frame[~self.data_frame[column].isin(value)]
        elif operation == "==":    
            self.data_frame = self.data_frame[self.data_frame[column] == value]
        return self