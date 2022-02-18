import pandas as pd
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [n+1 for n in numbers]
print(new_list)


name = "Adrian"
letters = [letter for letter in name]
print(letters)


power = [2**n for n in range(10)]
print(power)

names = ["Adrian", "Bartek", "Cezary", "Dawid", "Ewa", "Fryderyk"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)


# dictionary comprehension
#new_dict ={new_key: new_value for item in list}
# new_dict= {new_key:new_value for (key, value) in dict.items() if test}

student_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for(
    student, score) in student_scores.items() if score > 60}
print(passed_students)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# (temp_c * 9/5) + 32 = temp_f

weather_f = {day: temp*9/5 + 32 for (day, temp) in weather_c.items()}

# looping a dictionary
# for (key, value) in weather_f.items():
#     print(key, value)


student_dict = {
    "name": ["Adrian", "Bartek", "Cezary", "Dawid", "Ewa", "Fryderyk"],
    "age": [20, 21, 22, 23, 24, 25],
}

student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# loop through data frame
for index, row in student_data_frame.iterrows():
    print(index, row["name"])
