from datetime import datetime, timedelta
from collections import defaultdict



def get_birthdays_per_week(users):
    birthdays = defaultdict(list)
    current_weekday = datetime.now().weekday()
    next_monday = datetime.now() + timedelta(days=(7 - current_weekday))
    next_sunday = next_monday + timedelta(days=6)
    
    for user in users:
        birthday = user['birthday'].replace(year=datetime.now().year)
        if next_monday <= birthday <= next_sunday:
            weekday = birthday.weekday()
            if weekday in [5, 6]:
                weekday = 0
            birthdays[weekday].append(user['name'])
    
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    for i in range(5):
        if birthdays[i]:
            print(f"{weekdays[i]}: {', '.join(birthdays[i])}")

users = [
    {'name': 'Steve', 'birthday': datetime(1990, 7, 31)},
    {'name': 'Tom', 'birthday': datetime(1992, 7, 31)},
    {'name': 'Jerry', 'birthday': datetime(1994, 8, 4)},
    {'name': 'Viktor', 'birthday': datetime(1996, 8, 4)}
]

get_birthdays_per_week(users)