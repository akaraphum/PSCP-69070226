# submission.md

## 1. OJ Information

- OJ problem number: oj2996
- OJ problem title: [สลับตัวอักษร](https://ijudge.it.kmitl.ac.th/problems/2996/description)
- OJ submission ID: 542202
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 2-3 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: แปลงข้อความที่ได้รับมา
- Input: ข้อความ string
- Output: ข้อความ string แบบกลับด้านและเป็นตัวพิมพ์เล็ก

---

First plan:

```text
Step 1: รับข้อความ
Step 2: แสดงผลกลับด้านแบบตัวพิมพ์เล็กทั้งหมด
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

รับค่า text เข้ามาเป็น string แล้วทำการ print `text[::-1].lower()` เพื่อให้แสดงผลเป็นแบบกลับด้านและเป็นตัวพิมพ์เล็ก

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `icexerxd`
- Expected output: `dxrexeci`
- Actual output: `dxrexeci`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: มีตัวเลข
- Input: `1c3x0r`
- Expected output: `r0x3c1`
- Actual output: `r0x3c1`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: มีตัวอักษรพิเศษสลับพิมพ์เล็กพิมพ์ใหญ๋
- Input: `C4tchM3!fuC4n`
- Expected output: `n4cuf!3mhct4c`
- Actual output: `n4cuf!3mhct4c`
- Result: Passed

---

## 6. ความช่วยเหลือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
 - ไม่ได้ถาม AI

---

## 7. What I Learned

ได้ฝึกการแสดงผลแบบ ย้อนกลับ, เปลี่ยนค่าเป็นตัวพิมพ์เล็กโดยใช้ `.lower()`

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

