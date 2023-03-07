from abc import ABC, abstractmethod
from hashlib import md5
import uuid


class IDGenerator(ABC):

    @abstractmethod
    def generate_id(self):
        pass


class UUID4Generator(IDGenerator):

    def generate_id(self):
        return str(uuid.uuid4())


class PasswordManager(ABC):

    @abstractmethod
    def set_password(self, password):
        pass

    @abstractmethod
    def check_password(self, password):
        pass


class UserPasswordManager(PasswordManager):
    def set_password(self, password):
        return md5(password.encode()).hexdigest()

    def check_password(self, password, passwordHash):
        return md5(password.encode()).hexdigest() == passwordHash
