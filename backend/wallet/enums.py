from enum import Enum


class AccountType(Enum):
    deposit = 'deposit'
    credit = 'credit'
    savings = 'savings'
    checking = 'checking'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_value(cls, member):
        return cls[member].value
