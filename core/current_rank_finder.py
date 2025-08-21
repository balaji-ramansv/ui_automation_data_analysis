class CurrentRankFinder:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    def get_top_n_ranked_issues(self, *, top_n):
        return self.data_frame["Reason"].value_counts()[:top_n]