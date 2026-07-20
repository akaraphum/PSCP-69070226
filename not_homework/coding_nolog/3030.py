"""จะเป็นให้ได้เลย"""
import math
pushups_target = int(input())
situps_target = int(input())
wakeup_target = int(input())
running_target = int(input())

pushups = int(input())
situps = int(input())
#โดนเกรียน
running = int(input())
wakeup = int(input()) #ล้อหลอก


pushups = pushups_target / pushups
situps = situps_target / situps
wakeup = wakeup_target / wakeup
running = running_target / running

print(f"{math.ceil(max(pushups, situps, wakeup, running))}")
