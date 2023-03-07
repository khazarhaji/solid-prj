from abc import ABC, abstractmethod
from hashlib import md5
import uuid
from services import FileDataService


class PasswordManager(ABC):

    @abstractmethod
    def set_password(self, password):
        pass

    @abstractmethod
    def check_password(self, password):
        pass


class IDGenerator(ABC):

    @abstractmethod
    def generate_id(self):
        pass


class UUID4Generator(IDGenerator):

    def generate_id(self):
        return str(uuid.uuid4())


class User(PasswordManager, UUID4Generator, FileDataService):

    def __init__(self, username) -> None:
        self.id = self.generate_id()
        self.username = username

    def __str__(self):
        return self.username

    def set_password(self, password):
        self.password = md5(password.encode()).hexdigest()

    def check_password(self, password):
        return md5(password.encode()).hexdigest() == self.password
