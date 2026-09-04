# submission.md

## 1. OJ Information

- OJ problem number: oj3160
- OJ problem title: [LEARNING LOGS] หาจำนวนเฉพาะ
- OJ submission ID: 630711
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 10-15 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: เขียนโปรแกรมเพื่อหาจำนวนเฉพาะ prime number
- Input: ตัวเลขเริ่มต้นและสุดท้าย
- Output: เลขที่เป็น prime number กับ จำนวนรวมทั้งหมดของ จำนวนเฉพาะ

---

First plan:

```text
Step 1: รับค่าเลขเริ่มต้นและสุดท้าย
Step 2: หาค่า prime 
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

ใช้ for loop เพื่อเช็คค่าไปเริ่ยๆ โดยไล่จากเลขเริ่มต้นไปเลขท้าย และนำเลขนั้นๆ ไปเข้า loop สำหรับเช็ตอีกทีว่าเป้น prime number หรือไม่

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `1 10`
- Expected output: `2 3 5 7\nTotal primes: 4`
- Actual output: `2 3 5 7\nTotal primes: 4`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: case ปกติ
- Input: `32 36`
- Expected output: `Total primes: 0`
- Actual output: `Total primes: 0`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: เลขหลังน่อยกว่าหน้า
- Input: `100 -500`
- Expected output: `Total primes: 0`
- Actual output: `Total primes: 0`
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

