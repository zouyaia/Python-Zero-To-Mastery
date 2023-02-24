from datetime import datetime

Weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
m, d, y = map(int, input().split())
print(Weekdays[datetime(y,m,d).weekday()])