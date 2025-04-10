class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id         # Инкапсуляция ID
        self.__name = name               # Инкапсуляция имени
        self.__access_level = 'user'     # По умолчанию уровень доступа - обычный

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, new_name):
        self.__name = new_name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__user_list = []  # Список пользователей, которыми управляет админ

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)
            print(f"✅ Пользователь {user.get_name()} добавлен.")
        else:
            print("❌ Невозможно добавить: объект не является User.")

    def remove_user(self, user_id):
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                self.__user_list.remove(user)
                print(f"🗑 Пользователь {user.get_name()} удален.")
                return
        print("❌ Пользователь с таким ID не найден.")

    def list_users(self):
        print("📋 Список пользователей:")
        for user in self.__user_list:
            print(f" - {user.get_user_id()} | {user.get_name()} | {user.get_access_level()}")


# ▶ Пример использования
admin = Admin(0, "AdminUser")

user1 = User(1, "Иван")
user2 = User(2, "Мария")
user3 = User(3, "Алексей")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

admin.list_users()

admin.remove_user(2)

admin.list_users()
