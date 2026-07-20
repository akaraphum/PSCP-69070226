# submission.md

## 1. OJ Information

- OJ problem number: oj3031
- OJ problem title: [Ink](https://ijudge.it.kmitl.ac.th/problems/3031/description)
- OJ submission ID: [559497](https://ijudge.it.kmitl.ac.th/submissions/559497/overview)
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 15-30 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: หาเวลาในการที่หมึกจะแผ่ขยายไปจนถึงบ้านคน
- Input: แผ่ขยายตารางหน่วยต่อวิ จำนวนบ้านทีต้องการความชว่ยเหลือ และ ข้อมูลพิกัดบ้านแต่ละหลัง x,y
- Output: เวลาที่น้ำหมึกจะไปถึง

---

First plan:

```text
Step 1: รับค่า ข้อมูลทั้งหมด
Step 2: คำนวนเวลาที่จะไปถึงบ้านแต่ละหลัง
Step 3: แสดงผลเวลา โดยปัดขึ้นทั้งหมดหากเป็น .xx
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

รับค่าข้อมูลจำนวนบ้าน ข้อมูลบ้านแต่ละหลัง คำนวณเวลาที่จะไปถึงบ้านนั้นๆ `(house[0] ** 2) + (house[1] ** 2)` และแสดงผลเป็นแบบเวลาวินาที เป็น (int)

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input:
```
50 4
0 0
0 1
30 30
0 60
```
- Expected output:
```
0
1
114
227
```
- Actual output:
```
0
1
114
227
```
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: ขยาย 0 บ้าน 10 หลัง
- Input:
```
0 10
0 0
1 0
0 1
30 30
0 60
60 0
60 60
85 85
20 25
26 65
```
- Expected output:
```
0
0
0
0
0
0
0
0
0
0
```
- Actual output:
```
0
0
0
0
0
0
0
0
0
0
```
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: เริ่มต้นด้วย 0 0
- Input:
```
0 0
```
- Expected output:
```

```
- Actual output:
```

```
- Result: Passed

---

## 6. ความช่วยเหลือ

 - เพื่อนบอกเกี่ยวกับสูตร `R*R = (house[0] ** 2) + (house[1] ** 2)` ในการหาพื้นที่ระยะห่างจากบ้าน


---

## 7. What I Learned

ต้องรู้สูตรในการคำนวณ

## 8. คำรับรองของนักศึกษา

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |

