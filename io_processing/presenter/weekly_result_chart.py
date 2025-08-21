import matplotlib.pyplot as plt
import numpy as np

class WeeklyResultChart:
    def __init__(self, *, report):
        self.report = report
        self.bar_width = 0.35

        # self.fig, self.axes = plt.subplots()
        
    def draw_bar_chart(self):
        regression_runs = [self.report["report_date"]]
        passed_new_tests_count = self.report["passed_new_tests_count"]
        passed_old_tests_count = self.report["passed_old_tests_count"]
        failed_new_automation_tests_count = self.report["failed_new_automation_tests_count"]
        failed_old_automation_tests_count = self.report["failed_old_automation_tests_count"]
        failed_new_application_tests_count = self.report["failed_new_application_tests_count"]
        failed_old_application_tests_count = self.report["failed_old_application_tests_count"]

        n_groups = len(regression_runs)

        # Create an array for the x-axis positions for the groups
        index = np.arange(n_groups)

        self.fig, self.axes = plt.subplots() # Adjust figure size for better readability

        # PASS bars
        bar1 = self.axes.bar(index - self.bar_width/2, passed_new_tests_count, self.bar_width,
                      label='New automations pass', color='lawngreen')
        
        bar_start_height = passed_new_tests_count
        bar2 = self.axes.bar(index - self.bar_width/2, passed_old_tests_count, self.bar_width,
                      label='Old automations pass', color='palegreen', bottom=bar_start_height)

        # FAIL bars
        bar3 = self.axes.bar(index + self.bar_width/2, failed_new_automation_tests_count, self.bar_width, 
                      label='New automation script failures', color='orangered')
        
        bar_start_height = failed_new_automation_tests_count
        bar4 = self.axes.bar(index + self.bar_width/2, failed_old_automation_tests_count, self.bar_width, 
                      label='Old automation script failures', color='peachpuff', bottom=bar_start_height)
        
        bar_start_height = bar_start_height + failed_old_automation_tests_count
        bar5 = self.axes.bar(index + self.bar_width/2, failed_new_application_tests_count, self.bar_width, 
                      label='New application failures', color='crimson', bottom=bar_start_height)
        
        bar_start_height = bar_start_height + failed_new_application_tests_count
        bar6 = self.axes.bar(index + self.bar_width/2, failed_old_application_tests_count, self.bar_width, 
                      label='Application Fail', color='mistyrose', bottom=bar_start_height, )
        
        bars_tuples = [(bar1, passed_new_tests_count), (bar2, passed_old_tests_count), (bar3, failed_new_automation_tests_count),
                       (bar4, failed_old_automation_tests_count), (bar5, failed_new_application_tests_count), (bar6, failed_old_application_tests_count)]
        for bar, val in bars_tuples:
            print(bar.datavalues)


        self.axes.set_xlabel(f'Automation Test Run {self.report["report_date"]}')
        self.axes.set_ylabel('Count')
        self.axes.set_title('Pass vs. Fail Counts')
        self.axes.set_xticks(index)
        self.axes.set_xticklabels(regression_runs)
        self.axes.legend()
        self.axes.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
