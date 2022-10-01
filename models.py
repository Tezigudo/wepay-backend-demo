import datetime
from typing import List, Dict


class User:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.__user_id = user_id
        self.friend: List[User] = []
        # this may use forignkey on real implemenetation
        self.bills: Dict['Bill', bool] = {} # this is mapping between bill and amount

    @property
    def user_id(self):
        """return a id of that user"""
        return self.__user_id

    def is_payed(self, bill: 'Bill') -> bool:
        """return True if user payed the bill"""
        return self.bills[bill]


class Bill:
    def __init__(self, topic: str):
        self.topic = topic
        self.pub_date = datetime.datetime.now()

    def assign(*users: User):
        """assign bill to users"""
        for user in users:
            user.bills[self] = False


if __name__ == '__main__':
    pass
