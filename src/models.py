from abc import ABC, abstractmethod
from utils import IDGenerator, PasswordManager
from services import DataService


class User:

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username

    def generate_id(self, generator: IDGenerator):
        generator = generator()
        self.id = generator.generate_id()

    def set_password(self, password, password_manager: PasswordManager):
        password_manager = password_manager()
        self.password = password_manager.set_password(password)

    def save(self, save_service: DataService):
        save_service = save_service()
        save_service.save(self)
