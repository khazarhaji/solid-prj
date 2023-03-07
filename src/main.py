from repositories import UserRepository


if __name__ == '__main__':
    user_repository = UserRepository()
    user_repository.create("khazar", "parol123")
