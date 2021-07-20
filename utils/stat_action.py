from datetime import datetime
import calendar


def generate_day_iterator(day):
    dict_days = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    keys = ['date_from', 'date_to']
    convert_list = str(datetime.date(datetime.now())).split('-')
    convert_list[2] = int(convert_list[2]) - dict_days[day]
    if convert_list[2] == 0:
        convert_list[1] = int(convert_list[1]) - 1
        day_count = calendar.monthrange(int(convert_list[0]), int(convert_list[1]))[1]
        convert_list[2] == day_count
        if convert_list[1] <= 9:
            convert_list[1] = '0'+str(convert_list[1])
    elif convert_list[2] < 0:
        convert_list[1] = int(convert_list[1]) - 1
        day_count = calendar.monthrange(int(convert_list[0]), int(convert_list[1]))[1]
        convert_list[2] = convert_list[2] + day_count
        if convert_list[1] <= 9:
            convert_list[1] = '0'+str(convert_list[1])

    days = ['-'.join([str(elem) for elem in convert_list]), datetime.now()]
    days[0] = datetime.strptime(days[0][2:], '%y-%m-%d')
    return {keys[i]: days[i] for i in range(len(keys))}


def get_week_dict():
    day = datetime.today().strftime('%A')
    return generate_day_iterator(day)


def get_month_dict():
    keys = ['date_from', 'date_to']
    convert_list = str(datetime.date(datetime.now())).split('-')
    convert_list[2] = '01'
    days = ['-'.join([str(elem) for elem in convert_list]), datetime.now()]
    days[0] = datetime.strptime(days[0][2:], '%y-%m-%d')
    return {keys[i]: days[i] for i in range(len(keys))}
