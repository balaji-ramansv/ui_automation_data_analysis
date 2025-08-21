from io_processing.data_source_reader.various_data_source_readers import ExcelReader
from io_processing.presenter.historical_line_chart import HistoricalLineChart
import pandas as pd
import main_helper


def get_report(file_name, report_date, sprint_and_week="", sheet_name=""):
    report_data = {
        "sprint_and_week": sprint_and_week,
        "report_date": report_date
    }
    # passed tests
    report_data["passed_tests_count"] = main_helper.get_passed_tests_count(file_name=file_name, sheet_name=sheet_name)
    report_data["passed_new_tests_count"] = main_helper.get_passed_new_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    report_data["passed_old_tests_count"] = main_helper.get_passed_old_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    # failed tests
    report_data["failed_tests_count"] = main_helper.get_failed_tests_count(file_name=file_name, sheet_name=sheet_name)
    report_data["failed_new_test_cases_count"] = main_helper.get_failed_new_test_cases_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    report_data["failed_old_test_cases_count"] = main_helper.get_failed_old_test_cases_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    # breakdown of new failed test cases
    report_data["failed_new_automation_tests_count"] = main_helper.get_failed_new_automation_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    report_data["failed_new_application_tests_count"] = main_helper.get_failed_new_application_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    # breakdown of old failed test cases
    report_data["failed_old_automation_tests_count"] = main_helper.get_failed_old_automation_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    report_data["failed_old_application_tests_count"] = main_helper.get_failed_old_application_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week], sheet_name=sheet_name)
    return report_data


if __name__ == "__main__":
    file_name = r"C:\Users\balaji.ramakrishnan\Downloads\Regression Triage Dev.xlsx"
    spreadsheets = pd.ExcelFile(file_name)
    reports = []
    for sheet_name in spreadsheets.sheet_names:
        excel = ExcelReader()
        #df = excel.read_data_from_data_source(file_name=file_name, sheet_name=sheet_name)
        reports.append(get_report(file_name=file_name, report_date=sheet_name, sprint_and_week="NA", sheet_name=sheet_name))
    hlc = HistoricalLineChart(reports=reports)
    hlc.create_line_chart()