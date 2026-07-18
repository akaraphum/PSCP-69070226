# submission.md

## 1. OJ Information

- OJ problem number: oj3017
- OJ problem title: [Bill](https://ijudge.it.kmitl.ac.th/problems/3017/description)
- OJ submission ID: 542214
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 10-15 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: ให้รวมราคาสุดท้าย จากราคาอาหารปกติ
- Input: ราคาอาหาร (แบบไม่ีรวม service, vat)
- Output: ราคาทั้งหมดแบบรวม service, vat

---

First plan:

```text
Step 1: รับค่าจำนวนเต็ม
Step 2: ถ้าต่ำกว่า 50 หรือ มากกว่า 1000 ให้เป็นค่านั้น
Step 3: บวก VAT 7%
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

ใช้ if else สำหรับเช็คค่า service เนื่องจาก service จะคิดขั้นต่ำที่ 50 แต่ไม่เกิน 1000 จึงต้องทำการใช้ if else เพื่อบวกค่า service ก่อน
ขั้นตอนสุดท้าย print ราคาทั้งหมด โดยนำ 0.07 มาคูณกับจำนวนราคาอาหาร + service เพื่อทำการติด vat 7% เพื่อแสดงผลสุดท้ายออกมา
ใช้ `:.2f` เพื่อแสดง ทศนิยม 2 ตำแหน่ง

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `1500`
- Expected output: `1765.50`
- Actual output: `1765.50`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: ราคาที่ค่า service จะน้อยกว่า 50
- Input: `100`
- Expected output: `160.50`
- Actual output: `160.50`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: ราคาที่ค่า service จะมากกว่า 1000
- Input: `98650000`
- Expected output: `105556570.00`
- Actual output: `105556570.00`
- Result: Passed

---

## 6. ความช่วยเหลือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
 - ไม่ได้ถาม AI


---

## 7. What I Learned

ใช้ if else และใช้หลักการคูณเพื่อหา % สำหรับคำนวนเรื่อง Bill

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

