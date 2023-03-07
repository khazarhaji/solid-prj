from abc import ABC, abstractmethod
from models import User
from utils import UUID4Generator, UserPasswordManager
from services import FileDataService


class ModelRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    # @abstractmethod
    # def update(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass

    # @abstractmethod
    # def read(self):
    #     pass


class UserRepository(ModelRepository):

    def __init__(self):
        self.user_model = User

    def create(self, username, password):
        user = self.user_model(username)
        user.generate_id(UUID4Generator)
        user.set_password(password, UserPasswordManager)
        user.save(FileDataService)
