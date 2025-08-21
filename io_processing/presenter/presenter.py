class RankPresenter:
    def present_current_rank_data(self, ranked_issues, display_length=110):
        for ix in ranked_issues.index:
            issue = ""
            if len(ix) < display_length:
                issue = ix + " " * (display_length - len(ix))
            else:
                issue = ix[:display_length]
            print(f"{issue}\t|\t{ranked_issues[ix]}")