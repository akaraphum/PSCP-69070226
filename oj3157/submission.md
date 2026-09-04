# submission.md

## 1. OJ Information

- OJ problem number: oj3157
- OJ problem title: [LEARNING LOGS] เกมสะสมแต้ม
- OJ submission ID: 626565
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 5-10 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: คะแนนเริ่มต้นจาก 0 คะแนนเพิ่มหรือลด n รอบ ตามจำนวนลูป
- Input: จำนวนสำหรับ loop และ + -
- Output: คะแนนรวมสุดท้าย

---

First plan:

```text
Step 1: เริ่มต้นรับค่าจำนวนรอบสำหรับ loop
Step 2: รับค่า + หรือ - เพื่อคำนวณคะแนน
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

รับค่าสำหรับลูปเข้ามาแล้ว ในลูปจะรับค่า + หรือ - ถ้า + จะได้รับคะแนนเพิ่ม 10 คะแนน ถ้า - จะโดนหักไป 5 คะแนน และแสดงผลลัพธ์คะแนนสุดท้ายออกมา

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `6`
- Input(หลายบรรทัด) : `++--++`
- Expected output: `30`
- Actual output: `30`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: นอกจาก + -
- Input: `5`
- Input(หลายบรรทัด) : `+-*/(**)`
- Expected output: `5`
- Actual output: `5`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: loop 0
- Input: `0`
- Input: ``
- Expected output: `0`
- Actual output: `0`
- Result: Passed

---

## 6. ความช่วยเหลือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
 - ไม่ได้ถาม AI


---

## 7. What I Learned

-

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

