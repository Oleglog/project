import re

class UserSchema:
    pass

class DataBase:
    def __init__(self):
        self.users = []

    def get_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()

    def serializers(self, file_data):
        users_list = []
        for line in file_data:
            attributes = re.split(r';\s*', line.strip())
            user_dict = {}
            for attr in attributes:
                if '=' in attr:
                    key, value = attr.split('=', 1)  # Используем 1, чтобы разделить только на 2 части
                    user_dict[key.strip()] = value.strip()
                else:
                    print(f"Warning: '{attr}' does not contain '='")
            users_list.append(user_dict)
        return users_list

    def create_user(self, user_data):
        for data in user_data:
            user = UserSchema()
            for key, value in data.items():
                setattr(user, key, value)
            self.users.append(user)

    def search(self, **kwargs):
        results = []
        for user in self.users:
            match = all(getattr(user, key, None) == value for key, value in kwargs.items())
            if match:
                results.append(user)
        return results

class Translator:
    def __init__(self):
        self.tr = {}

    def add(self, eng, rus):
        if eng not in self.tr:
            self.tr[eng] = []
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng):
        return self.tr.get(eng, [None])[0]

if __name__ == "__main__":
    db = DataBase()
    file_data = db.get_data('main.txt')
    user_data = db.serializers(file_data)
    db.create_user(user_data)

    found_users = db.search(name='Олег')
    print(f"Найдено пользователей: {len(found_users)}")

    translator = Translator()
    translator.add('hello', 'привет')
    translator.add('hello', 'здравствуй')
    translator.add('world', 'мир')

    print(translator.translate('hello'))
    translator.remove('hello')
    print(translator.translate('hello'))