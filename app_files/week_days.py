from pandas import Timestamp

class Day(object):
    def __init__(self, response, day_index):
        self.today_data = response['days'][day_index]
        self.date = self.today_data['datetime']
        self.name = Timestamp(self.date).day_name()
        self.temp = self.today_data['temp']
        self.max_today = self.today_data['tempmax']
        self.min_today = self.today_data['tempmin']
        self.humidity = self.today_data['humidity']
        self.conditions = self.today_data['conditions']


class Week(Day):
    def __init__(self, response):
        self.day1 = Day(response, 0)
        self.day2 = Day(response, 1)
        self.day3 = Day(response, 2)
        self.day4 = Day(response, 3)
        self.day5 = Day(response, 4)
        self.day6 = Day(response, 5)
        self.day7 = Day(response, 6)
        self.all_days = [self.day1, self.day2, self.day3, self.day4, self.day5, self.day6, self.day7]


