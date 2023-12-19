import datetime


def increase(value):
    increment_value = 1
    return value + increment_value


def get_years_from_today(year):
    return datetime.datetime.now().year - year


class Person:
    def __init__(self, first_name, last_name, date_of_birth, ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    # not unit testable
    # unit testable, when get_years_from_today is mocked
    @property
    def age(self):
        return get_years_from_today(self.date_of_birth)

    # unit testable
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
