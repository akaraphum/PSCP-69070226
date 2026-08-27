"""Bonus"""

job_type, age, salary = input().upper().split()

age = int(age)
salary = int(salary)

bonus = 0

if job_type == "M":
    bonus = 1500

    if age <= 5:
        bonus += 0.06 * salary
    elif age <= 10:
        bonus += 0.08 * salary
    else:
        bonus += 0.10 * salary

elif job_type == "B":
    bonus = 1000

    if age <= 5:
        bonus += 0.05 * salary
    elif age <= 10:
        bonus += 0.06 * salary
    else:
        bonus += 0.07 * salary

elif job_type == "G":
    bonus = 500

    if age <= 5:
        bonus += 0.04 * salary
    elif age <= 10:
        bonus += 0.05 * salary
    else:
        bonus += 0.06 * salary

if bonus == int(bonus):
    print(int(bonus))
else:
    print(bonus)
