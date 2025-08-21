import main_helper
from io_processing.presenter.weekly_result_chart import WeeklyResultChart

def get_report(file_name, report_date, sprint_and_week="NA"):
    report_data = {
        "sprint_and_week": sprint_and_week,
        "report_date": report_date
    }
    # passed tests
    report_data["passed_tests_count"] = main_helper.get_passed_tests_count(file_name=file_name)
    report_data["passed_new_tests_count"] = main_helper.get_passed_new_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    report_data["passed_old_tests_count"] = main_helper.get_passed_old_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    # failed tests
    report_data["failed_tests_count"] = main_helper.get_failed_tests_count(file_name=file_name)
    report_data["failed_new_test_cases_count"] = main_helper.get_failed_new_test_cases_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    report_data["failed_old_test_cases_count"] = main_helper.get_failed_old_test_cases_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    # breakdown of new failed test cases
    report_data["failed_new_automation_tests_count"] = main_helper.get_failed_new_automation_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    report_data["failed_new_application_tests_count"] = main_helper.get_failed_new_application_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    # breakdown of old failed test cases
    report_data["failed_old_automation_tests_count"] = main_helper.get_failed_old_automation_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    report_data["failed_old_application_tests_count"] = main_helper.get_failed_old_application_tests_count(file_name=file_name, new_sprint_and_weeks=[sprint_and_week])
    # print report
    for param, val in report_data.items():
        print(f"{param} : {val}")
    print(report_data)
    return report_data

if __name__ == "__main__":
    file_name = r"C:\Users\balaji.ramakrishnan\Downloads\Regression Triage Dev.xlsx"
    sheet_name = "July21-QA1"
    category = "SQL"
    sprint_and_week = "8.2 w3"
    report_date = "21-Jul-2025"

    #report = get_report(file_name, report_date, sprint_and_week)
    report = {
        "report_date": report_date,
        "sprint_and_week": "8.2 w3",
        'passed_tests_count': 1700, 'passed_new_tests_count': 93, 'passed_old_tests_count': 1607,
        'failed_tests_count': 600, 'failed_new_test_cases_count': 36, 'failed_old_test_cases_count': 564,
        'failed_new_automation_tests_count': 18, 'failed_new_application_tests_count': 18,
        'failed_old_automation_tests_count': 522, 'failed_old_application_tests_count': 42
    }
    chart = WeeklyResultChart(report=report)
    chart.draw_bar_chart()

    
