# Hướng dẫn sử dụng chi tiết (Detailed User Guide)
## Chương trình Trắc Nghiệm Tiếng Anh - English Vocabulary Quiz

---

## 🎓 Hướng dẫn cho sinh viên (Student Guide)

### I. Cài đặt và chạy chương trình

#### 1. Yêu cầu:
- Máy tính có cài đặt Python 3.x
- Windows, macOS, hoặc Linux

#### 2. Cách chạy:
```bash
python Baocaocuoiky.py
```

Hoặc trên Windows:
```bash
python.exe Baocaocuoiky.py
```

---

### II. Giao diện chương trình

#### Menu chính:
```
============================================================
CHƯƠNG TRÌNH TRẮC NGHIỆM TIẾNG ANH
Học từ vựng tiếng Anh dễ dàng
============================================================

Vui lòng chọn chế độ:
1. Chỉ làm bài trắc nghiệm Tiếng Việt → Tiếng Anh
2. Chỉ làm bài trắc nghiệm Tiếng Anh → Tiếng Việt
3. Làm cả hai bài trắc nghiệm
0. Thoát chương trình

Nhập lựa chọn của bạn (0-3):
```

---

### III. Các bước làm bài

#### Bước 1: Chọn chế độ trắc nghiệm
- Nhập **1** nếu muốn làm từ Tiếng Việt sang Tiếng Anh
- Nhập **2** nếu muốn làm từ Tiếng Anh sang Tiếng Việt
- Nhập **3** nếu muốn làm cả 2
- Nhập **0** để thoát

#### Bước 2: Trả lời câu hỏi
```
Câu 1/10: Xin chào là tiếng Anh gì?
  1. Water
  2. Hello
  3. Goodbye
  4. Thank you

Chọn câu trả lời (1-4): 
```
- Nhập số từ **1 đến 4** để chọn đáp án
- Chương trình sẽ hiển thị kết quả ngay lập tức

#### Bước 3: Xem kết quả
- Sau 10 câu hỏi, chương trình hiển thị:
  - Điểm số: X/10
  - Phần trăm: X%
  - Chi tiết các câu trả lời sai

#### Bước 4: Lựa chọn tiếp theo
```
Bạn muốn tiếp tục (C/N)? 
```
- Nhập **C** hoặc **Y** hoặc **CÓ** để làm bài tiếp
- Nhập **N** hoặc **K** hoặc **KHÔNG** để thoát

---

### IV. Ví dụ thực tế (Real Example)

```
============================================================
CHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH
============================================================

Câu 1/10: Nước là tiếng Anh gì?
  1. House
  2. Water
  3. School
  4. Thank you

Chọn câu trả lời (1-4): 2
✓ Đúng!

Câu 2/10: Sách là tiếng Anh gì?
  1. Teacher
  2. Car
  3. Book
  4. Money

Chọn câu trả lời (1-4): 3
✓ Đúng!

... (tiếp tục 8 câu nữa)

============================================================
KẾT QUẢ TRẮC NGHIỆM
============================================================

CHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH
Điểm số: 9/10
Phần trăm: 90%

Các câu trả lời sai:
  1. Nước
     Đáp án đúng: Water
     Đáp án của bạn: House

... (kết quả các chỉ tiêu khác nếu có)

Tổng điểm: 19/20
Tổng phần trăm: 95%

✓ Kết quả đã được lưu vào file: ket_qua_quiz.txt
```

---

### V. File kết quả

Mỗi lần chạy xong, kết quả sẽ được lưu trong file **`ket_qua_quiz.txt`**

#### Nội dung file:
- Thời gian làm bài
- Điểm số từng chỉ tiêu
- Phần trăm
- Chi tiết các câu trả lời sai (câu hỏi, đáp án đúng, đáp án của bạn)
- Tổng điểm

#### Xem file kết quả:
```bash
# Trên Linux/macOS:
cat ket_qua_quiz.txt

# Trên Windows:
type ket_qua_quiz.txt

# Hoặc dùng bất kỳ trình soạn thảo nào
```

---

### VI. Từ vựng trong chương trình

Chương trình có 20 từ vựng cơ bản:

1. Hello - Xin chào
2. Goodbye - Tạm biệt
3. Thank you - Cảm ơn
4. Please - Vui lòng
5. Sorry - Xin lỗi
6. Yes - Có
7. No - Không
8. Water - Nước
9. Food - Thực phẩm
10. Book - Sách
11. School - Trường học
12. Teacher - Giáo viên
13. Student - Học sinh
14. House - Nhà
15. Car - Ô tô
16. Money - Tiền
17. Time - Thời gian
18. Day - Ngày
19. Night - Đêm
20. Morning - Buổi sáng

---

### VII. Các lưu ý quan trọng

✅ **Nên làm:**
- Ghi nhớ từ vựng trước khi làm bài
- Kiểm tra các câu trả lời sai để học lại
- Thử làm nhiều lần để cải thiện điểm

❌ **Không nên:**
- Đoán bừa mà không học
- Nhập số không trong khoảng 1-4 (chương trình sẽ yêu cầu nhập lại)
- Xóa file `ket_qua_quiz.txt` nếu muốn giữ lịch sử

---

### VIII. Xử lý lỗi

#### Lỗi: "Vui lòng nhập một số hợp lệ!"
- **Nguyên nhân**: Bạn nhập không phải là số
- **Giải quyết**: Nhập số từ 1-4

#### Lỗi: "Vui lòng nhập số từ 1 đến 4!"
- **Nguyên nhân**: Bạn nhập số ngoài khoảng 1-4
- **Giải quyết**: Nhập lại số trong khoảng 1-4

#### Lỗi: "Vui lòng nhập C (Có) hoặc N (Không)"
- **Nguyên nhân**: Nhập sai khi chọn tiếp tục
- **Giải quyết**: Nhập C để tiếp tục hoặc N để thoát

---

### IX. Cải thiện điểm

**Cách 1: Ghi nhớ từ vựng**
- In danh sách từ vựng ra
- Học trước khi làm bài

**Cách 2: Làm lại nhiều lần**
- Mỗi lần làm sẽ có 10 câu ngẫu nhiên
- Kinh nghiệm sẽ giúp bạn nhớ lâu hơn

**Cách 3: Phân tích câu sai**
- Xem file `ket_qua_quiz.txt`
- Ghi nhớ các từ mình trả lời sai
- Làm bài tiếp theo sẽ cảnh báo

---

### X. Các biến thể có thể thêm (Optional Enhancements)

Có thể mở rộng chương trình với:
1. **Thêm nhiều từ vựng**: Chỉnh sửa dictionary `VOCABULARY`
2. **Theo dõi tiến độ**: Thêm thống kê tổng điểm
3. **Độ khó**: Thêm các mức độ khó khác nhau
4. **Âm thanh**: Thêm phát âm tiếng Anh
5. **Giao diện đồ họa**: Dùng thư viện tkinter hoặc PyQt

---

## 📞 Hỗ trợ (Support)

Nếu gặp vấn đề:
1. Kiểm tra python có được cài đặt: `python --version`
2. Kiểm tra file `Baocaocuoiky.py` có tồn tại
3. Đảm bảo thư mục có quyền ghi file (để lưu kết quả)

---

*Dự án môn Kỹ thuật Lập trình - Nhóm 2*
