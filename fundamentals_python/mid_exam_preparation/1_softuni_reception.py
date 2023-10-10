import math

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
hour_counter = 0
efficiency_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while students_count > 0:
    students_count -= efficiency_per_hour
    hour_counter += 1
    if hour_counter % 4 == 0:
        hour_counter += 1

print(f"Time needed: {hour_counter}h.")