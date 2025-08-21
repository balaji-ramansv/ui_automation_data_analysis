from io_processing.data_source_reader.data_source_reader import DataSourceReader as DSR
import pandas as pd
import pdb

class ExcelReader(DSR):
    def read_data_from_data_source(self, *, file_name, sheet_name):
        df = pd.read_excel(io=file_name, sheet_name=sheet_name)
        # pdb.set_trace()
        return df

    def read_data_from_data_sources(self, *, file_name):
        spreadsheets = pd.ExcelFile(file_name)
        sheet_names = spreadsheets.sheet_names
        data_frames_list = []
        for sheet_name in sheet_names:
            data_frames_list.append(pd.read_excel(io=file_name, sheet_name=sheet_name))
        return pd.concat(data_frames_list)
