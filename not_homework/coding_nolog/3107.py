"""Bonus"""
job_type, age, salary = map(str, input().split())
age, salary = int(age), int(salary)
bonus = 0

if job_type == "M":
    bonus = 1500
    if age < 5:
        bonus += 0.06 * salary
    elif 5 <= age <= 10:
        bonus += 0.08 * salary
    else:
        bonus += 0.1 * salary
elif job_type == "B":
    bonus = 1000
    if age < 5:
        bonus += 0.05 * salary
    elif 5 <= age <= 10:
        bonus += 0.06 * salary
    else:
        bonus += 0.07 * salary
else:
    bonus = 500
    if age < 5:
        bonus += 0.04 * salary
    elif 5 <= age <= 10:
        bonus += 0.05 * salary
    else:
        bonus += 0.06 * salary

print(int(bonus))
