from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
# 1. Empty list fail
    if len(users) == 0:
        return {}

# 2. Base preparing for work def
    start_day = date.today()
    interval_before = timedelta(days=2)
    interval_after = timedelta(days=6)

# 3. Preparing Users to dict
    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_this_year = birthday.replace(year=start_day.year)
        birthday_next_year = birthday.replace(year=start_day.year + 1)

# 4. Working with FIRST dict. All birthdays [from 2 days to TODAY] and [from TODAY to 6 days]
# 4.1. This year
        if (start_day - interval_before) <= birthday_this_year <= (start_day + interval_after):
# 4.1.1. All Saturdays and Sundays will be Monday
            if birthday_this_year.weekday() == 5:
                per_day = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                per_day = birthday_this_year + timedelta(days=1)
            else:
                per_day = birthday_this_year
# 4.1.2. Deleting all days before TODAY
            if start_day <= per_day <= (start_day + interval_after):
                birthdays_per_week[per_day.strftime('%A')].append(name)
            else:
                pass
        else:
            pass

# 4.2. Next year if we have this situation
        if (start_day - interval_before) <= birthday_next_year <= (start_day + interval_after):
# 4.2.1. All Saturdays and Sundays will be Monday
            if birthday_next_year.weekday() == 5:
                per_day = birthday_next_year + timedelta(days=2)
            elif birthday_next_year.weekday() == 6:
                per_day = birthday_next_year + timedelta(days=1)
            else:
                per_day = birthday_next_year
# 4.2.2. Deleting all days before TODAY
            if start_day <= per_day <= (start_day + interval_after):
                birthdays_per_week[per_day.strftime('%A')].append(name)
            else:
                pass
        else:
            pass
 
#  5. Creating dict for showing
    users_check = {}
    for key, value in birthdays_per_week.items():
        users_check[key] = value

    return users_check


if __name__ == "__main__":
    users = [
        {"name": "Adam", "birthday": datetime(1955, 12, 23).date()}, 
        {"name": "Bonny", "birthday": datetime(1970, 12, 22).date()}, 
        {"name": "Cici", "birthday": datetime(1970, 12, 21).date()}, 
        {"name": "David", "birthday": datetime(1970, 12, 25).date()}, 
        {"name": "Elon", "birthday": datetime(1970, 12, 27).date()}, 
        {"name": "Frank", "birthday": datetime(1970, 12, 30).date()}, 
        {"name": "Garry", "birthday": datetime(1970, 1, 6).date()}, 
        {"name": "Kevin", "birthday": datetime(1970, 1, 3).date()}, 
        {"name": "Mona", "birthday": datetime(1966, 1, 2).date()}, 
        {"name": "Richard", "birthday": datetime(1970, 1, 1).date()}, 
        ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")