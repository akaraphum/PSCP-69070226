# submission.md

## 1. OJ Information

- OJ problem number: oj3232
- OJ problem title: กบน้อยกระโดด
- OJ submission ID: 633762
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 5-10 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: เช็คว่ากระโดดไปถึงจุด โดยต้องกระโดดไปทั้งหมดกี่ครั้ง และในแต่ละครั้ง ระยะจะสั้นลงทีละ 2 เมตร
- Input: รับค่า กบกระโดดได้กี่เมตรต่อครั้ง และเป้าหมาย
- Output: จำนวนก้าวที่ใช้ในการไปถึงเป้าหมาย

---

First plan:

```text
Step 1: รับค่า ระจะของการกระโดดแต่ละครั้ง และ จุดเป้าหมาย set start ไว้ที่ 1 STEP ปัจจุบัน เท่ากับ X
Step 2: ถ้าเกิดว่าระยะของการกระโดดมากกกว่าหรือเท่ากับระยะของเป้าหมายอยู่แล้ว ให้ทำการ print 1 ออกมาเลย
Step 3: loop ไปเรื่อยๆ เพื่อเช็๕ว่าถึงเป้าหมายในกี่กืาว หรือว่าไม่ถึง
```

---

## 4. วิธีสุดท้ายที่ใช้จริง
set start ไว้ที่ 1 และค่า STEPNOW = X และเข้า loop เมื่อเช้า loop แล้ว 
เมื่อค่า X มีมากกว่า 0 ก้าวจะลดลงไป 2 ก็คือ x -= 2
และนำไปบวกเข้า STEPNOW และ start += 1 แต่ถ้าค่า X น้อยกว่าหรือเท่ากับ 0 จะแสดงผล -1 ออกมาทันที
และสุดท้ายจะเช็คว่า STEPNOW มีค่ามากกว่าหรือเท่ากับเป้าหมายหรือยัง ถ้าถึงแล้วจะทำการ print จำนวน start(จำนวนก้าวทั้งหมด) ออกมาทันที

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `6 10`
- Expected output: `2`
- Actual output: `2`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: จำนวนก้าวมากกว่าเป้าหมาย
- Input: `156120651 165`
- Expected output: `1`
- Actual output: `1`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: เลขเยอะๆ
- Input: `51919819D`
- Expected output: `51 of `
- Actual output: `51 of `
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

