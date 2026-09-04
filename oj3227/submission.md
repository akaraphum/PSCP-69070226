# submission.md

## 1. OJ Information

- OJ problem number: oj3227
- OJ problem title: ไพ่ 44 ใบ
- OJ submission ID:  630955
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 5-10 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: รับค่ามาแค่ค่าเดียว แล้วเช็คว่าเป็นอะไร
- Input: รับค่า เลขหรือตัว และประเภทของไพ่
- Output: ชื่อไร่ใบนั้นแบบเต็มๆ

---

First plan:

```text
Step 1: รับค่าของไพ่ใบนั้นๆ
Step 2: ใช้ string slicing สำหรับเช็คว่า เป็นไพ่อะไร
Step 3: แสดงผลชื่อเต์ฺมของไพ่ใบนั้นๆ
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

เช็ค string ดีๆ ว่าสองตัวแรกเป็นค่าเดียวกันไหม เช่น 10D แต่เลขอื่นๆจะมีแค่ 2 ตัว เช่น AD และโดยส่วนใหญ่จะมีแค่ 2 ตัว แล้วแสดงผลชื่อเต็ฒออกมาโดยใช้ if else

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `10D`
- Expected output: `10 of diamonds`
- Actual output: `10 of diamonds`
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

