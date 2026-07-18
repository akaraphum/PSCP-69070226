# submission.md

## 1. OJ Information

- OJ problem number: oj3024
- OJ problem title: [SurprisingVote](https://ijudge.it.kmitl.ac.th/problems/3024/description)
- OJ submission ID: [542214](https://ijudge.it.kmitl.ac.th/submissions/558849/overview)
- OJ status: Passed

---

## 2. เวลาที่ใช้ในการทำโจทย์

- 15-30 minutes

---

## 3. ความเข้าใจในโจทย์

- สิ่งที่เข้าใจจากโจทย์: รับค่าคะแนนเข้ามาและหาว่า มีหน้าม้าอวยหรือไม่
- Input: คะแนนรวม, คะแนนสูงสุด (คะแนนเต็ม 10)
- Output: Surprise หรือไม่

---

First plan:

```text
Step 1: รับค่าคะแนนทั้งหมดและค่าคะแนนสูงสุด
Step 2: คำนวนหาคะแนนที่เหลือ
Step 3: เปรียบเทียบคะแนน ห่่างกันเกิน 2
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

รับค่าคะแนนทั้งหมดและสูงสุด และนำไปหาค่าอีกสองค่าที่เหลือ และค่าสุดท้าย โดยการนำ `(คะแนนรวม - คะแนนมากสุด) - คะแนนมากสุด` มาใช้ แต่ค่าอาจะเป็น < 0
เลยทำ if else มาเพื่อเข็คหาก น้อยกว่า 0 จริง คะแนนน้อยที่สุดจะเป็น 0 ไปเลย การคำนวนจะทำให้ได้ ค่าคะแนน ที่น้อยที่สุดออกมา เช่น รวม 29 คะแนนสูงสุดคือ 10
คะแนนอีกสองคนที่จะเป็นไปได้ก็คือ 10 9 เพราะหักออกไปแล้ว คะแนนอีกสองคนรวมกันจะเหลือ 29 - 10 = 19 และอีกสองคนคะแนนต้องไม่มากกว่าคนแรก คนสุดท้ายต้อง <= คนสอง

---

## 5. Test Cases

### Test Case 1

- เหตุผลที่เลือก: case ปกติ
- Input: `21`
- Input: `10`
- Expected output: `surprising`
- Actual output: `surprising`
- Result: Passed

### Test Case 2

- เหตุผลที่เลือก: คะแนนทุกคนเท่ากัน
- Input: `30`
- Input: `10`
- Expected output: `Not surprising`
- Actual output: `Not surprising`
- Result: Passed

### Test Case 3

- เหตุผลที่เลือก: เลขทศนิยม
- Input: `21.23456789`
- Input: `10.67`
- Expected output: `surprising`
- Actual output: `surprising`
- Result: Passed

---

## 6. ความช่วยเหลือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
 - ไม่ได้ถาม AI


---

## 7. What I Learned

การหาวิธีหาค่าอีก 2 คนที่เหลือ และหาค่าคนสุดท้ายเพื่อมาเปรียบเทียบ

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

