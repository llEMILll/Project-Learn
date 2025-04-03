import datetime, bday_messages

today=datetime.date.today()
next_birthday=datetime.date(2025,10,4)
days_away = next_birthday - today

if today == next_birthday:
    mensaje=bday_messages.random_message
else:
    print(f'My next birthday is {days_away} days away!')
