import datetime
from typing import List, Dict, Set


class User:
    """some User model"""
    ids = 0

    def __init__(self, name: str):
        User.ids += 1
        self.name = name
        self.__user_id = User.ids
        self.user_history: Set[User] = set()
        self.friend: Set[User] = set()
        # this may use forignkey on real implemenetation
        # this is mapping between bill and amount
        self.bills: Dict['Bill', float] = {}

    @property
    def user_id(self):
        """return a id of that user"""
        return self.__user_id

    def is_payed(self, bill: 'Bill') -> bool:
        """return True if user payed the bill"""
        return self.bills[bill]

    def __repr__(self):
        return self.name
    __str__ = __repr__


class Bill:
    """Bill model"""

    def __init__(self, topic: str):
        self.topic = topic
        self.__header: User = None
        self.need_to_pay: Set[User] = set()
        self.pub_date: datetime.datetime = datetime.datetime.now()

    @property
    def header(self) -> User:
        return self.__header

    @header.setter
    def header(self, user: User):
        if not isinstance(user, User):
            raise TypeError("header must be a User instance")
        self.__header = user

    def assign(self, *users: User) -> None:
        """assign bill to users"""
        for user in users:
            user.bills[self] = False

    def __repr__(self) -> str:
        return f'{self.topic}| HEADER={self.header.name if self.header else None} | NEED_TO_PAY={list(self.need_to_pay)}'
    __str__ = __repr__


if __name__ == '__main__':
    pass
