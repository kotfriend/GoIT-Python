from datetime import date
from collections import defaultdict

birthday_per_day = defaultdict(list)

def get_birthdays_per_week(users):

    if len(users) == 0:
        return {}

    today = date.today()

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=date.today().year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=date.today().year + 1)

        if (birthday_this_year - today).days < 7:
            if birthday_this_year.strftime('%A') == 'Sunday':
                birthday_per_day['Monday'].append(name)
            elif birthday_this_year.strftime('%A') == 'Saturday':
                birthday_per_day['Monday'].append(name)
            else:
                birthday_per_day[birthday_this_year.strftime('%A')].append(name)

    users = {}
    for key, value in birthday_per_day.items():
        users[key] = value
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": date(1976, 1, 1)},
        {"name": "Bill Gates", "birthday": date(1955, 12, 30)}, 
        {"name": "Elon Musk", "birthday": date(1966, 12, 29)}, 
        {"name": "Madonna", "birthday": date(1970, 12, 30)}, 
        {"name": "Bill Murrey", "birthday": date(1970, 12, 31)}, 
        {"name": "Jeff Frisker", "birthday": date(1970, 1, 2)}, 
        {"name": "Elen Glister", "birthday": date(1970, 1, 4)}, 
        {"name": "Viven Pfafer", "birthday": date(1970, 1, 4)},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")