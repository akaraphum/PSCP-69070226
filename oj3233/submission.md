# submission.md

## 1. OJ Information

- OJ problem number: oj3233
- OJ problem title: สลากกินแบ่ง
- OJ submission ID: 633931
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 5-10 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: ทำระบบตรวจสลากกินแบ่ง และแสดงผลเงินรางวัลที่จะได้รับ
- Input: ผลของสลาก และสลากกินแบ่งที่ซื้อ
- Output: จำนวนเงินที่จะได้รับรางวัล

---

First plan:

```text
Step 1: รับค่า สลากกิน ผลมและใบที่ซื้อแบ่งเข้ามา
Step 2: ใช้ string slicing เช็คทีละตัวและแสดงผลเงินรางวัล
```

---

## 4. วิธีสุดท้ายที่ใช้จริง
รับค่าผลของสลากและสลากที่ซื้อ และเช็คความเข้ากันตามเงื่อนไขของโจทย์และทำการแสดงผลลัพธ์ออกมาเป็นจำนวนเงินรางวัลที่จะได้

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `A 12345`
- Input2: `A 12345`
- Expected output: `1000000`
- Actual output: `1000000`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: case ปกติ
- Input: `A 12345`
- Input2: `A 12345`
- Expected output: `0`
- Actual output: `0`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: case เลขเกิน
- Input: `A 12345555`
- Input2: `B 55554666`
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

