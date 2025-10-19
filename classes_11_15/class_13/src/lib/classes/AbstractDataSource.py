from abc import ABC, abstractmethod


class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        raise NotImplementedError("Not implemented method")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Not implemented method")

    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Not implemented method")

    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Not implemented method")

    def hello_world(self):
        print("Hello World")
