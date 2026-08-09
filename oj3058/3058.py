"""BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())

use_big = min(goal // 5, b) #ที่ต้อวใข้ ที่มี
# print(use_big)

rem_goal = goal - (use_big * 5)
# print(rem_goal)

if a >= rem_goal:
    print(rem_goal)
else:
    print(-1)
