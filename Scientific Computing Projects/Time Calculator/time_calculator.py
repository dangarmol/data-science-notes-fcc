import math

# Note: AM to PM changes between 11:59 AM and 12:00 PM!

def add_time(start, duration, weekday = None):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    start_weekday_index = None

    if weekday:
        start_weekday_index = weekdays.index(weekday.lower())

    end_hour = None
    end_min = None

    time_24h = convert_to_24h(start)
    start_hour = int(time_24h.split(":")[0])
    start_min = int(time_24h.split(":")[1])

    duration_hour = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])

    if start_min + duration_min >= 60:
        start_hour += 1
        end_min = start_min + duration_min - 60
    else:
        end_min = start_min + duration_min

    end_hour = (start_hour + duration_hour) % 24
    days_carryover = math.trunc((start_hour + duration_hour) / 24)

    # .title() makes first letter uppercase
    new_time = convert_to_ampm(str(end_hour) + ":" + "%02d" % end_min)

    if weekday:
        weekday_text = ", " + weekdays[(start_weekday_index + days_carryover) % 7].title()
        new_time += weekday_text
    
    if days_carryover == 1:
        new_time += " (next day)"
    elif days_carryover > 1:
        carryover_text = " (" + str(days_carryover) + " days later)"
        new_time += carryover_text

    return new_time


def convert_to_24h(time):
    number = time.split()[0]
    is_pm = time.split()[1] == "PM"

    if is_pm and int(number.split(":")[0]) < 12:
        return str(int(number.split(":")[0]) + 12) + ":" + number.split(":")[1]
    elif not is_pm and int(number.split(":")[0]) == 12:
        return str(int(number.split(":")[0]) - 12) + ":" + number.split(":")[1]
    else:
        return number


def convert_to_ampm(time):
    if int(time.split(":")[0]) > 12:
        return str(int(time.split(":")[0]) - 12) + ":" + time.split(":")[1] + " PM"
    elif int(time.split(":")[0]) == 12:
        return time + " PM"
    elif int(time.split(":")[0]) == 0:
        return str(int(time.split(":")[0]) + 12) + ":" + time.split(":")[1] + " AM"
    else:
        return time + " AM"
