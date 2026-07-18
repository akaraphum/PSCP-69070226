# submission.md

## 1. OJ Information

- OJ problem number: oj3011
- OJ problem title: [Colors](https://ijudge.it.kmitl.ac.th/problems/3011/description)
- OJ submission ID: 542377
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 25-45 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: รับค่าสีสองสี
- Input: ข้อความ string 2 ข้อความ
- Output: ข้อความ string แสดงผลของสีที่ผสมแล้ว

---

First plan:

```text
Step 1: รับค่าสี 2 สี
Step 2: แปลงเป็น Cap (ตัวอักษรแรกพิมพ์ใใหญ่เพื่อเช็คให้ตรงกับค่าใน Dict)
Step 3: เช็คกับ Dictionary
Step 4: แสดงผล
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

เช็คค่าสีทั้งสองสีโดยการใช้ dictionary เพื่อมาเก็บค่าสีสำหรับการผสม และ ตอนแสดงผลลัพธ์ ถ้าไม่ตรงตามเงื่อนไขในนั้นจะแสดง Error
ส่วนถ้าเป็นสีเดียวกันแต่อยู่ใน Red Yellow Blue จะแสดงชื่อสีนั้นออกมา

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `Red`
- Input2: `Blue`
- Expected output: `Violet`
- Actual output: `Violet`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: ค่าซ้ำกัน
- Input: `Red`
- Input2: `Red`
- Expected output: `Red`
- Actual output: `Red`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: สลับพิมพ์เล็กพิมพ์ใหญ๋
- Input: `BlUe`
- Input2: `YElloW`
- Expected output: `Green`
- Actual output: `Green`
- Result: Passed

### Test Case 4

- เหตุผลที่เลือก: สีนอกเหนือจาก Red Green Blue และมีตัวเลข อักษรอื่นๆปน
- Input: `B1ack1nB1acK`
- Input2: `@CDC`
- Expected output: `Error`
- Actual output: `Error`
- Result: Passed

---

## 6. ความช่วยเหลือ

 - เพื่อนแนะนำให้ใช้ Dictionary แทนการใช้ if else
 - ไม่ได้ถาม AI

---

## 7. What I Learned

ฝึกการใช้งาน Dictionary ฝึกทักษะการแก้ปัญหาง่ายๆที่เราอาจมองข้าม
ตอนแรกเขียนด้วย `Dictionary` พบว่า ไม่ผ่าน testcase เลยลองแก้ไข แต่ก็ยังไม่ได้จนลอง
กลับใช้ใช้งาน `If else` แบบเดิม แต่ก็ยังไม่ได้อยู่ดี สรุปแล้วตอนท้ายพบว่า
`elif color2 == color1 and color1 in {"Red", "Green", "Blue"}` ในส่วนของ `{"Red", "Green", "Blue"}`
เช็คค่าผิดจะต้องเป็น `{"Red", "Yellow", "Blue"}` จึงทำให้ผ่านข้อนี้ได้

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

