from core.current_rank_finder import CurrentRankFinder
from io_processing.data_source_reader.various_data_source_readers import ExcelReader
from io_processing.presenter.presenter import RankPresenter

if __name__ == "__main__":
    excel_reader = ExcelReader()
    data_frame = excel_reader.read_data_from_data_source(file_name=r"C:\Users\balaji.ramakrishnan\Downloads\Regression Triage Dev.xlsx", sheet_name="July28-SCC")
    rank = CurrentRankFinder(data_frame=data_frame)
    top_n_issues = rank.get_top_n_ranked_issues(top_n=20)
    rank = RankPresenter()
    rank.present_current_rank_data(ranked_issues=top_n_issues)
