# Задание 5. С помощью конструкции try..catch, обработайте участки кода в которых могут
# возникнуть исключения
from datetime import datetime

def format_date(input_date):
    try:
        date_obj = datetime.strptime(input_date, '%d.%m.%Y')

        day_num = date_obj.day

        month_names = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
        }
        week_names = {
            'Monday': 'Понедельник',
            'Tuesday': 'Вторник',
            'Wednesday': 'Среда',
            'Thursday': 'Четверг',
            'Friday': 'Пятница',
            'Saturday': 'Суббота',
            'Sunday': 'Воскресенье'
        }
        rus_day_name = date_obj.strftime('%A')
        day_name = week_names.get(rus_day_name, rus_day_name)
        month_name = month_names[date_obj.month]
        year_num = date_obj.year
        day_name_capitalized = day_name.capitalize()

        return f"{day_name_capitalized}, {day_num} {month_name}, {year_num} год"
    except ValueError:
        return "Некорректный формат даты. Используйте формат DD.MM.YYYY"
print(format_date('01.09.2021'))
print(format_date('31.09.2021'))