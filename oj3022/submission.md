# submission.md

## 1. OJ Information

- OJ problem number: oj3022
- OJ problem title: [Temperature](https://ijudge.it.kmitl.ac.th/problems/3022/description)
- OJ submission ID: [542214](https://ijudge.it.kmitl.ac.th/submissions/558788/overview)
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 15-30 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: แปลงค่าอุณหภูมิ ให้เป็นไปตามทีโจทยืบอก
- Input: เลขอุณหภูมิ, ประเภทอุณหภูมิ 1, 2
- Output: อุณหภูมิแบบแปลงค่าหน่วยแล้ว

---

First plan:

```text
Step 1: รับค่าอุณหภูมิมา และ ประเภทหน่วย ที่ input มาและที่ต้องการแปลง
Step 2: แปลงหน่วยให้เป็นคำตอบ โดยใช้ If else เช็คหลายเงื่อนไข
Step 3: แสดงคำตอบเป็น ทศนิยม 2 ตำแหน่ง
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

แปลงค่าอุณหภูมิ input เป็น C ก่อนเพื่อให้ง่ายต่อการคำนวนและไม่ใช้ if else ซับซ้อนหลายอันเกินไป แล้วจึงค่อยไปแปลง
เป็นหน่วยที่ต้องการจะแปลงค่าเป็นหน่วยนั้นๆแบบ ทศนิยม 2 ตำแหน่ง

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `35.555555`
- Input 2: `C`
- Input 3: `K`
- Expected output: `308.71`
- Actual output: `308.71`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: ค่าหน่วยซ้ำกัน
- Input: `35.555555`
- Input 2: `K`
- Input 3: `K`
- Expected output: `35.56`
- Actual output: `35.56`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: ค่าติดลบ
- Input: `-6767.6767676767`
- Input 2: `K`
- Input 3: `F`
- Expected output: `-12641.49`
- Actual output: `-12641.49`
- Result: Passed

### Test Case 4

- เหตุผลที่เลือก: 0
- Input: `0`
- Input 2: `0`
- Input 3: `0`
- Expected output: ``
- Actual output: ``
- Result: Passed

---

## 6. ความช่วยเหลือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
 - ไม่ได้ถาม AI


---

## 7. What I Learned

คิดหาวิธีที่จะทำโจทย์ให้ง่ายขึ้น ลดการใช้งาน if else ใช้หลักการคิดทางคณิตให้มากขึ้น เพื่อให้ทำโจทย์ได้ง่ายๆ

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

