"""
Q4.Write a Python program to extract year, month, date and time using Lambda. 

Sample Output: 

2020-01-15 09:03:32.744178 
2020 
1 
15 
09:03:32.744178 """

from datetime import datetime

extract_info = lambda dt_str: (
    datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").year,
    datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").month,
    datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").day,
    datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M:%S.%f")
)


input_datetime_str = "2020-01-15 09:03:32.744178"

year, month, day, time = extract_info(input_datetime_str)

print(f"Input Datetime: {input_datetime_str}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Time: {time}")
