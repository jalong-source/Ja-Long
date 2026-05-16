# Chương trình Trắc Nghiệm Tiếng Anh - English Vocabulary Quiz Program

## 📚 Mô tả dự án (Project Description)

Đây là một chương trình học từ vựng tiếng Anh tương tác, cho phép người dùng làm bài trắc nghiệm theo hai hướng: 
- **Tiếng Việt → Tiếng Anh**: Xem câu hỏi bằng tiếng Việt, chọn đáp án tiếng Anh
- **Tiếng Anh → Tiếng Việt**: Xem câu hỏi bằng tiếng Anh, chọn đáp án tiếng Việt

This is an interactive English vocabulary learning program that allows users to take quizzes in two modes:
- **Vietnamese → English**: See questions in Vietnamese, choose English answers
- **English → Vietnamese**: See questions in English, choose Vietnamese answers

---

## ✨ Các chức năng (Features)

### 1. **Chỉ tiêu 1: Trắc nghiệm Tiếng Việt → Tiếng Anh**
   - Hiển thị 10 câu hỏi tiếng Việt
   - Người dùng chọn đáp án tiếng Anh từ 4 lựa chọn
   - Hiển thị kết quả ngay sau khi trả lời

### 2. **Chỉ tiêu 2: Trắc nghiệm Tiếng Anh → Tiếng Việt**
   - Hiển thị 10 câu hỏi tiếng Anh
   - Người dùng chọn đáp án tiếng Việt từ 4 lựa chọn
   - Hiển thị kết quả ngay sau khi trả lời

### 3. **Lưu kết quả vào file**
   - Lưu điểm số
   - Lưu các câu trả lời sai
   - Lưu thời gian làm bài
   - File: `ket_qua_quiz.txt`

### 4. **Tính năng bổ sung**
   - Chọn chỉ làm 1 bài trắc nghiệm hoặc cả 2
   - Hiển thị điểm số và phần trăm
   - Hiển thị chi tiết các câu trả lời sai
   - Có thể tiếp tục làm bài hoặc thoát chương trình

---

## 🎯 Yêu cầu chi tiết (Detailed Requirements)

### Người dùng trả lời:
- **10 câu hỏi** cho mỗi chỉ tiêu
- Mỗi câu trả lời đúng = **1 điểm**
- Tối đa điểm cho 1 chỉ tiêu = **10 điểm**

### Kết quả:
- Chương trình hiển thị điểm số
- Liệt kê các câu trả lời sai
- Lưu kết quả vào file `ket_qua_quiz.txt`
- Sau đó thoát chương trình (hoặc cho phép tiếp tục)

---

## 🚀 Cách sử dụng (How to Use)

### Chạy chương trình:
```bash
python Baocaocuoiky.py
```

### Các bước thực hiện:
1. Chạy chương trình
2. Chọn chế độ muốn làm:
   - **1**: Chỉ làm bài trắc nghiệm Tiếng Việt → Tiếng Anh
   - **2**: Chỉ làm bài trắc nghiệm Tiếng Anh → Tiếng Việt
   - **3**: Làm cả hai bài trắc nghiệm
   - **0**: Thoát chương trình
3. Trả lời các câu hỏi bằng cách nhập số từ 1-4
4. Xem kết quả sau khi hoàn thành
5. Kết quả sẽ được lưu vào file `ket_qua_quiz.txt`
6. Chọn tiếp tục hoặc thoát

---

## 📁 Cấu trúc thư mục (Directory Structure)

```
Ja-Long/
├── Baocaocuoiky.py          # Chương trình chính
├── ket_qua_quiz.txt         # File lưu kết quả (tự động tạo)
├── README.md                # Tài liệu này
└── ma-nguon-jalongschool    # Tài liệu bổ sung
```

---

## 💾 Kết quả lưu vào file (Saved Results Format)

File `ket_qua_quiz.txt` chứa:
```
======================================================================
THỜI GIAN: 2025-05-16 10:30:45
======================================================================

CHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH
Điểm số: 8/10
Phần trăm: 80%

Các câu trả lời sai:
  1. Câu hỏi: Nước
     Đáp án đúng: Water
     Đáp án của bạn: Book

----------------------------------------------------------------------

CHỈ TIÊU 2: TRẮC NGHIỆM TIẾNG ANH → TIẾNG VIỆT
Điểm số: 9/10
Phần trăm: 90%

Các câu trả lời sai:
  1. Câu hỏi: School
     Đáp án đúng: Trường học
     Đáp án của bạn: Nhà

----------------------------------------------------------------------

Tổng điểm: 17/20
Tổng phần trăm: 85%
======================================================================
```

---

## 📚 Từ vựng trong chương trình (Vocabulary Database)

Chương trình hiện có 20 từ vựng:

| # | Tiếng Anh | Tiếng Việt |
|---|-----------|-----------|
| 1 | Hello | Xin chào |
| 2 | Goodbye | Tạm biệt |
| 3 | Thank you | Cảm ơn |
| 4 | Please | Vui lòng |
| 5 | Sorry | Xin lỗi |
| 6 | Yes | Có |
| 7 | No | Không |
| 8 | Water | Nước |
| 9 | Food | Thực phẩm |
| 10 | Book | Sách |
| 11 | School | Trường học |
| 12 | Teacher | Giáo viên |
| 13 | Student | Học sinh |
| 14 | House | Nhà |
| 15 | Car | Ô tô |
| 16 | Money | Tiền |
| 17 | Time | Thời gian |
| 18 | Day | Ngày |
| 19 | Night | Đêm |
| 20 | Morning | Buổi sáng |

---

## 🔧 Các hàm chính (Main Functions)

### `mode_1_vietnamese_to_english()`
- Thực hiện bài trắc nghiệm Tiếng Việt → Tiếng Anh
- Trả về: (điểm số, danh sách câu trả lời sai)

### `mode_2_english_to_vietnamese()`
- Thực hiện bài trắc nghiệm Tiếng Anh → Tiếng Việt
- Trả về: (điểm số, danh sách câu trả lời sai)

### `get_multiple_choice()`
- Tạo các lựa chọn trắc nghiệm
- Trả về: (danh sách 4 lựa chọn, chỉ số đáp án đúng)

### `save_results()`
- Lưu kết quả vào file text
- Thêm vào cuối file (append mode)

### `display_results()`
- Hiển thị kết quả lên màn hình

### `main()`
- Hàm chính điều khiển chương trình

---

## 📋 Yêu cầu hệ thống (System Requirements)

- Python 3.x
- Hệ điều hành: Windows, macOS, Linux
- Không cần thư viện bên ngoài (chỉ dùng thư viện chuẩn)

---

## 👥 Nhóm dự án (Project Group)

**Số nhóm:** 2 (Group 2)

---

## 📝 Ghi chú (Notes)

- Mỗi lần chạy chương trình, kết quả sẽ được **append** vào file `ket_qua_quiz.txt`
- Các câu hỏi được chọn **ngẫu nhiên** từ từ điển
- Các lựa chọn trắc nghiệm cũng được **xáo trộn ngẫu nhiên**
- Người dùng có thể chạy nhiều lần và xem lịch sử kết quả

---

## ✅ Hoàn thành các yêu cầu (Completed Requirements)

- ✅ Chức năng 1: Trắc nghiệm Tiếng Việt
- ✅ Chức năng 2: Trắc nghiệm Tiếng Anh
- ✅ Chức năng 3: Ghi kết quả điểm số vào file
- ✅ 10 câu hỏi cho mỗi chỉ tiêu
- ✅ Tính điểm (1 điểm/câu đúng)
- ✅ Hiển thị điểm và câu trả lời sai
- ✅ Thoát chương trình sau khi hoàn thành

---

*Dự án môn Kỹ thuật Lập trình - Programming Techniques Course Project*
