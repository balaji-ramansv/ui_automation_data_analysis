from core.data_frame_filter_operations import DataFrameFilterOperations
import pdb
class MetricsCalculationAssistant:
    def __init__(self, *, data_frame):
        self.data_frame = data_frame

    def get_passed_test_cases(self):
        self.data_frame = self.data_frame[self.data_frame["status"].str.lower() == "pass"]
        # pdb.set_trace()
        return self.data_frame

    def get_failed_test_cases(self):
        self.data_frame = self.data_frame[self.data_frame["status"].str.lower() == "fail"]
        return self.data_frame

    def get_passed_test_cases_with_filters(self, *, filters):
        self.data_frame = self.get_passed_test_cases()


    def __get_filter(self):
        return DataFrameFilterOperations(data_frame=self.data_frame)

    def apply_filter(self, *, criterias):
        filter_obj = self.__get_filter()
        for criteria in criterias:
            filter_obj.filter_by(column=criteria["column"], operation=criteria["operation"], value=criteria["value"])
            self.data_frame = filter_obj.data_frame
        return filter_obj.data_frame