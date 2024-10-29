from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def get_user_info(self):
        pass
