import pandas as pd
from io_processing.data_source_reader.various_data_source_readers import ExcelReader
from core.current_rank_finder import CurrentRankFinder
from core.metrics_calculation_assistant import MetricsCalculationAssistant
from io_processing.presenter.presenter import RankPresenter

# For excel with multiple sheets
def rank_issues_from_a_report(file_name, sheet_name, top_n=10):
    data_frame = ExcelReader().read_data_from_data_source(
        file_name=file_name,
        sheet_name=sheet_name
    )
    current_issue_ranks = CurrentRankFinder(data_frame=data_frame).get_top_n_ranked_issues(top_n=top_n)
    rank_presenter = RankPresenter()
    rank_presenter.present_current_rank_data(current_issue_ranks)

# For excel with multiple sheets
def rank_issues_from_reports(file_name, top_n=10):
    data_frame = ExcelReader().read_data_from_data_sources(file_name=file_name)
    current_issue_ranks = CurrentRankFinder(data_frame=data_frame).get_top_n_ranked_issues(top_n=top_n)
    rank_presenter = RankPresenter()
    rank_presenter.present_current_rank_data(current_issue_ranks)

def get_passed_tests_count(file_name, sheet_name=""):
    data_frame = None
    if sheet_name == "":
        data_frame = ExcelReader().read_data_from_data_sources(file_name=file_name)
    else:
        data_frame = ExcelReader().read_data_from_data_source(file_name=file_name, sheet_name=sheet_name)
    return int(MetricsCalculationAssistant(data_frame=data_frame).get_passed_test_cases().count()["ReportData"])

def get_passed_new_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name,
                                 sheet_name=sheet_name,
                                 status_needed="pass",
                                 criterias=[
                                    {
                                        "column": "sprint and week",
                                        "operation": "isin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_passed_old_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="pass",
                                 criterias=[
                                    {
                                        "column": "sprint and week",
                                        "operation": "notin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_tests_count(file_name, sheet_name=""):
    data_frame = None
    if sheet_name == "":
        data_frame = ExcelReader().read_data_from_data_sources(file_name=file_name)
    else:
        data_frame = ExcelReader().read_data_from_data_source(file_name=file_name, sheet_name=sheet_name)
    return int(MetricsCalculationAssistant(data_frame=data_frame).get_failed_test_cases().count()["ReportData"])

def get_failed_automation_tests_count(file_name, sheet_name=""):
    return __get_desired_metrics(file_name=file_name,
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "notin",
                                        "value": ["Appllication"]
                                    }
                                ])

def get_failed_application_tests_count(file_name, sheet_name=""):
    return __get_desired_metrics(file_name=file_name,
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "isin",
                                        "value": ["Appllication"]
                                    }
                                ])

def get_failed_tech_or_env_tests_count(file_name, sheet_name=""):
    return __get_desired_metrics(file_name=file_name,
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "isin",
                                        "value": ["<placeholder>"]
                                    }
                                ])

def get_failed_new_test_cases_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "sprint and week",
                                        "operation": "isin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_new_automation_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "notin",
                                        "value": ["Appllication"]
                                    },
                                    {
                                        "column": "sprint and week",
                                        "operation": "isin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_new_application_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "isin",
                                        "value": ["Appllication"]
                                    },
                                    {
                                        "column": "sprint and week",
                                        "operation": "isin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_new_tech_or_env_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name,
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "isin",
                                        "value": ["<placeholder>"]
                                    },
                                    {
                                        "column": "sprint and week",
                                        "operation": "isin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_old_test_cases_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "sprint and week",
                                        "operation": "notin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_old_automation_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "notin",
                                        "value": ["Appllication"]
                                    },
                                    {
                                        "column": "sprint and week",
                                        "operation": "notin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_old_application_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "isin",
                                        "value": ["Appllication"]
                                    },
                                    {
                                        "column": "sprint and week",
                                        "operation": "notin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def get_failed_old_tech_or_env_tests_count(file_name, new_sprint_and_weeks, sheet_name=""):
    return __get_desired_metrics(file_name=file_name, 
                                 sheet_name=sheet_name,
                                 status_needed="fail",
                                 criterias=[
                                    {
                                        "column": "Fail Categories",
                                        "operation": "isin",
                                        "value": ["<placeholder>"]
                                    },
                                    {
                                        "column": "sprint and week",
                                        "operation": "notin",
                                        "value": new_sprint_and_weeks
                                    }
                                ])

def __get_desired_metrics(*, file_name, sheet_name="", status_needed, criterias):
    data_frame = None
    if sheet_name == "":
        data_frame = ExcelReader().read_data_from_data_sources(file_name=file_name)
    else:
        data_frame = ExcelReader().read_data_from_data_source(file_name=file_name, sheet_name=sheet_name)
    metrics = MetricsCalculationAssistant(data_frame=data_frame)
    if status_needed.lower() == "pass":
        metrics.get_passed_test_cases()
    elif status_needed.lower() == "fail":
        metrics.get_failed_test_cases()
    metrics.apply_filter(criterias=criterias)
    return int(metrics.data_frame.count()["ReportData"])