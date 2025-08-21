import matplotlib.pyplot as plt

class HistoricalLineChart:
    def __init__(self, *, reports):
        self.reports = reports
    
    def __create_lists_of_historical_data(self):
        data = {}
        print("All reports\n", self.reports)
        for report in self.reports:
            for k, v in report.items():
                print(f"report: {report}; k: {k}; v: {v}")
                if k in data:
                    data[k].append(v)
                else:
                    data[k] = []
            print(f"data: {data}")
        return data
    
    def create_line_chart(self):
        self.data = self.__create_lists_of_historical_data()
        fig, axes = plt.subplots()
        dates = self.data.pop("report_date")
        self.data.pop("sprint_and_week")
        for dp in self.data:
            # print(f"parameter: {dp}; data points: {self.data[dp]}")
            axes.plot(dates, self.data[dp], marker="s")
        axes.legend(self.data.keys())
        plt.show()