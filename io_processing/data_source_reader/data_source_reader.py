from abc import ABC, abstractmethod

class DataSourceReader(ABC):
    @abstractmethod
    def read_data_from_data_source(self, *args, **kwargs):
        pass
