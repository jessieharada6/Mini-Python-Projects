# DICTIONARY COMPREHENSION
# SYNTAX:
# new_dict = {new_key:new_val for item in list}
# new_dict = {new_key:new_val  for (key, val) in dict.items()}
# new_dict = {new_key:new_val  for (key, val) in dict.items() if test}

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {name: random.randint(1, 100) for name in names}

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

#  count
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# .split() by default any whitespace is a separator
count_dict = {char: len(char) for char in sentence.split()}

# convert temperature
# (0°C × 9/5) + 32 = F
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}

# Loop through a pandas dataframe
# 1. loop through dictionary
student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score": [56, 75, 98]
}
# iterate dictionary
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# panda inbuilt loop, loop through rows of a data frame
# index: 0, 1, 2
# row: each row
for (index, row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == "Lily":
        print(row.score)
