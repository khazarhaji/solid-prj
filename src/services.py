from abc import ABC, abstractmethod
import json


class DataService(ABC):

    @abstractmethod
    def save(self):
        pass


class FileDataService(DataService):

    def save(self, obj):
        user = vars(obj)
        json_object = json.dumps(user, indent=4)
        with open("users.json", "w") as outfile:
            outfile.write(json_object)
            outfile.close()
