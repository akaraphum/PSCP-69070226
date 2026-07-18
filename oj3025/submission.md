# submission.md

## 1. OJ Information

- OJ problem number: oj3025
- OJ problem title: [Season](https://ijudge.it.kmitl.ac.th/problems/3025/description)
- OJ submission ID: [542214](https://ijudge.it.kmitl.ac.th/submissions/550308/overview)
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 30-60 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: บอกฤดูจากเดือนและวันที่ให้มา
- Input: เดือนและวัน
- Output: ฤดูกาลนั้นๆ

---

First plan:

```text
Step 1: รับค่าเดือนและวัน
Step 2: ifelse เพื่อหาฤดูกาล
Step 3: ถ้าเป็นวันที่ > 21 แล้ว 3 หารลงตัวจะเป็นฤดูกาลต่อไป
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

สร้างตัวแปร season มาก่อน แล้วจึงไปเช็คค่า หากเดือนนั้นๆเป็นวันที่ > 21 แล้ว 3 หารลงตัวจะเป็นฤดูกาลต่อไป
แต่หากเดือนนั้นๆ เป็นเดือนสุดท้าย (เดือน 12) จะวนกลับมาเป็น winter เพราะต้องกลับมาเดือนที่ 1 ใหม่

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `3`
- Input: `22`
- Expected output: `spring`
- Actual output: `spring`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: เดือนสุดท้าย เดิือน 12
- Input: `12`
- Input: `22`
- Expected output: `winter`
- Actual output: `winter`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: ใส่เดือนเกินจากปกติและวันที่เกินจากปกติ
- Input: `1,659,856,265`
- Input: `32`
- Expected output: ` `
- Actual output: ` `
- Result: Not Passed

---

## 6. ความช่วยเหลือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
 - ไม่ได้ถาม AI


---

## 7. What I Learned

ใช้ string ในการเก็บข้อมูล หากเกินรอบเดือน 12 เดือนวนกลับมาที่เดือน 1 ใหม่

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

