# Testing Checklist & Quick Reference
## Chương trình Trắc Nghiệm Tiếng Anh - Test & Reference Guide

---

## ✅ Testing Checklist (Kiểm tra)

### A. Khởi động chương trình
- [ ] Chạy lệnh: `python Baocaocuoiky.py`
- [ ] Menu chính hiển thị đúng
- [ ] Có 4 lựa chọn: 1, 2, 3, 0

### B. Chế độ 1: Tiếng Việt → Tiếng Anh
- [ ] Chọn lựa chọn 1
- [ ] Hiển thị 10 câu hỏi
- [ ] Mỗi câu có 4 lựa chọn
- [ ] Nhập 1-4 được chấp nhận
- [ ] Hiển thị ✓ hoặc ✗ sau mỗi câu
- [ ] Sau 10 câu, hiển thị điểm số
- [ ] Danh sách câu sai được liệt kê

### C. Chế độ 2: Tiếng Anh → Tiếng Việt
- [ ] Chọn lựa chọn 2
- [ ] Hiển thị 10 câu hỏi
- [ ] Mỗi câu có 4 lựa chọn
- [ ] Nhập 1-4 được chấp nhận
- [ ] Hiển thị ✓ hoặc ✗ sau mỗi câu
- [ ] Sau 10 câu, hiển thị điểm số
- [ ] Danh sách câu sai được liệt kê

### D. Chế độ 3: Cả hai
- [ ] Chọn lựa chọn 3
- [ ] Chạy chế độ 1 trước
- [ ] Sau đó chạy chế độ 2
- [ ] Hiển thị tổng điểm 2 chế độ
- [ ] Hiển thị điểm phần trăm

### E. Lưu file kết quả
- [ ] File `ket_qua_quiz.txt` được tạo
- [ ] Chứa thời gian
- [ ] Chứa điểm số từng chế độ
- [ ] Chứa danh sách câu sai
- [ ] Chứa tổng điểm

### F. Tiếp tục / Thoát
- [ ] Nhập C → chạy lại từ đầu
- [ ] Nhập N → thoát chương trình
- [ ] Nhập Y → chạy lại từ đầu
- [ ] Nhập K → thoát chương trình
- [ ] Nhập CÓ → chạy lại từ đầu
- [ ] Nhập KHÔNG → thoát chương trình

### G. Xử lý lỗi
- [ ] Nhập chữ khi yêu cầu số → in lỗi "Vui lòng nhập một số hợp lệ!"
- [ ] Nhập số ngoài 1-4 → in lỗi "Vui lòng nhập số từ 1 đến 4!"
- [ ] Nhập sai khi chọn C/N → in lỗi yêu cầu nhập lại
- [ ] Chương trình không bị crash

### H. Tính năng bổ sung
- [ ] Các câu hỏi khác nhau mỗi lần chạy (random)
- [ ] Các lựa chọn được xáo trộn (random)
- [ ] File kết quả được append (thêm vào), không ghi đè
- [ ] Có thể chạy nhiều lần và xem lịch sử

---

## 🎓 Quick Reference - Từ vựng

### Group 1: Lời chào (Greetings)
```
Hello          → Xin chào
Goodbye        → Tạm biệt
Thank you      → Cảm ơn
Please         → Vui lòng
Sorry          → Xin lỗi
```

### Group 2: Câu trả lời (Responses)
```
Yes            → Có
No             → Không
```

### Group 3: Đồ vật (Objects)
```
Water          → Nước
Food           → Thực phẩm
Book           → Sách
House          → Nhà
Car            → Ô tô
Money          → Tiền
```

### Group 4: Địa điểm (Places)
```
School         → Trường học
```

### Group 5: Người (People)
```
Teacher        → Giáo viên
Student        → Học sinh
```

### Group 6: Thời gian (Time)
```
Time           → Thời gian
Day            → Ngày
Night          → Đêm
Morning        → Buổi sáng
```

---

## 🎮 Sample Test Run

### Input/Output Example:

```
$ python Baocaocuoiky.py

============================================================
CHƯƠNG TRÌNH TRẮC NGHIỆM TIẾNG ANH
Học từ vựng tiếng Anh dễ dàng
============================================================

Vui lòng chọn chế độ:
1. Chỉ làm bài trắc nghiệm Tiếng Việt → Tiếng Anh
2. Chỉ làm bài trắc nghiệm Tiếng Anh → Tiếng Việt
3. Làm cả hai bài trắc nghiệm
0. Thoát chương trình

Nhập lựa chọn của bạn (0-3): 1

============================================================
CHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH
============================================================
Hướng dẫn: Bạn sẽ thấy một từ tiếng Việt, hãy chọn đáp án tiếng Anh đúng
Bạn cần trả lời đúng 10 câu hỏi

Câu 1/10: Nước là tiếng Anh gì?
  1. School
  2. Water
  3. Book
  4. Car

Chọn câu trả lời (1-4): 2
✓ Đúng!

Câu 2/10: Xin chào là tiếng Anh gì?
  1. Goodbye
  2. Hello
  3. Thank you
  4. Please

Chọn câu trả lời (1-4): 2
✓ Đúng!

[... tiếp tục với 8 câu khác ...]

============================================================
KẾT QUẢ TRẮC NGHIỆM
============================================================

CHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH
Điểm số: 10/10
Phần trăm: 100%

Tất cả câu trả lời đều chính xác!

============================================================

✓ Kết quả đã được lưu vào file: ket_qua_quiz.txt

Bạn muốn tiếp tục (C/N)? n
Cảm ơn đã sử dụng chương trình. Tạm biệt!
```

---

## 🔧 Troubleshooting

### Problem: "ModuleNotFoundError" hoặc "ImportError"
**Solution**: Chương trình chỉ dùng thư viện chuẩn, không cần cài gì thêm

### Problem: File kết quả không được lưu
**Solution**: Kiểm tra quyền thư mục, chắc chắn có quyền ghi file

### Problem: Các câu hỏi bị lặp lại
**Solution**: Đó là bình thường, random có thể chọn lặp từ 20 từ trong database

### Problem: Chương trình bị crash
**Solution**: 
1. Đảm bảo chạy đúng lệnh: `python Baocaocuoiky.py`
2. Kiểm tra Python version: `python --version` (cần 3.x)
3. Xóa file `.pyc` nếu có: `rm -rf __pycache__`

---

## 📊 Scoring System

| Điểm | Phần trăm | Xếp loại |
|------|----------|----------|
| 18-20 | 90-100% | Xuất sắc (Excellent) |
| 15-17 | 75-84% | Tốt (Good) |
| 12-14 | 60-69% | Khá (Satisfactory) |
| 10-11 | 50-59% | Trung bình (Average) |
| < 10 | < 50% | Yếu (Poor) |

---

## 📝 File Explanation

### Files in project:
1. **Baocaocuoiky.py** - Chương trình chính
2. **ket_qua_quiz.txt** - Kết quả (tự động tạo)
3. **README.md** - Tài liệu chính
4. **HUONG_DAN_CHI_TIET.md** - Hướng dẫn chi tiết
5. **TEST_GUIDE.md** - File này (hướng dẫn test)
6. **ket_qua_quiz_mau.txt** - Ví dụ kết quả

---

## 🚀 How to Deploy

### For demonstration:
```bash
cd /workspaces/Ja-Long
python Baocaocuoiky.py
```

### For grade submission:
1. Tất cả file trong thư mục Ja-Long
2. Chạy test theo checklist
3. Ghi lại kết quả
4. Nộp cùng báo cáo

---

## ✨ Features Summary

| Feature | Status | Details |
|---------|--------|---------|
| Vietnamese Quiz | ✅ | 10 questions, multiple choice |
| English Quiz | ✅ | 10 questions, multiple choice |
| Score Calculation | ✅ | 1 point per correct answer |
| Wrong Answers List | ✅ | Shows wrong answers with correct one |
| Save to File | ✅ | Appends results to ket_qua_quiz.txt |
| Error Handling | ✅ | Input validation |
| Continue/Exit | ✅ | User can repeat or exit |

---

*Document version: 1.0 - May 16, 2025*
*Group: 2*
