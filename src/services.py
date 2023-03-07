from abc import ABC, abstractmethod
import json


class DataService(ABC):

    @abstractmethod
    def save(self):
        pass


class FileDataService(DataService):

    def __init__(self, path_to_save):
        self.path_to_save = path_to_save

    def save(self):
        user = vars(self)
        json_object = json.dumps(user, indent=4)
        with open("users.json", "w") as outfile:
            outfile.write(json_object)
