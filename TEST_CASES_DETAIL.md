File `test_Baocaocuoiky.py` là bộ kiểm thử tự động cho project quiz tiếng Anh của bạn. Nó dùng thư viện `unittest` của Python để kiểm tra từng phần của chương trình như một đội “robot giám khảo” 🤖📋

# Tổng quan các TestClass

## 1. `TestVocabulary`

Kiểm tra dữ liệu từ vựng (`VOCABULARY`)

### Những gì class này kiểm tra:

* `VOCABULARY` có tồn tại không
* Có đúng 20 từ không
* Mỗi từ có đủ:

  * `english`
  * `vietnamese`
* Cấu trúc dữ liệu có đúng format không

### Ví dụ test:

```python
def test_vocabulary_has_20_words(self):
    self.assertEqual(len(quiz.VOCABULARY), 20)
```

👉 Ý nghĩa:
Nếu database không đủ 20 từ thì test sẽ fail.

---

## 2. `TestMultipleChoice`

Kiểm tra logic tạo câu hỏi trắc nghiệm.

### Những gì class này kiểm tra:

* Hàm `get_multiple_choice()` trả về `tuple`
* Có đúng 4 đáp án
* Đáp án đúng nằm trong options
* Không bị trùng đáp án

### Ví dụ:

```python
options, idx = quiz.get_multiple_choice('Hello', self.english_words)
```

👉 Kiểm tra:

* `options` có 4 phần tử
* `'Hello'` nằm trong danh sách

Nếu thiếu đáp án đúng thì quiz sẽ “hack não người chơi” 💀

---

## 3. `TestScoring`

Kiểm tra tính điểm.

### Những gì class này kiểm tra:

* Điểm phần trăm tính đúng
* Logic quy đổi điểm chính xác

### Ví dụ:

```python
self.assertEqual(8 * 10, 80)
```

👉 Nghĩa là:
8/10 câu đúng → 80%

---

## 4. `TestFileSaving`

Kiểm tra lưu kết quả ra file.

### Những gì class này kiểm tra:

* File có được tạo không
* Hàm `save_results()` hoạt động đúng
* Dữ liệu có ghi vào file không

### Ví dụ:

```python
self.assertTrue(os.path.exists(self.test_file))
```

👉 Nếu test pass:
File kết quả đã được tạo thành công.

---

## 5. `TestDisplayResults`

Kiểm tra hiển thị kết quả ra màn hình console.

### Những gì class này kiểm tra:

* Có in `"KẾT QUẢ"` không
* Output có đúng format không

### Kỹ thuật dùng:

```python
sys.stdout = StringIO()
```

Để “hứng” nội dung in ra màn hình rồi kiểm tra.

👉 Giống như đặt cái xô dưới vòi nước console 🚰

---

## 6. `TestDataIntegrity`

Kiểm tra toàn vẹn dữ liệu.

### Những gì class này kiểm tra:

* Không có từ tiếng Anh trùng
* Không có từ tiếng Việt trùng
* Không có chuỗi rỗng

### Ví dụ:

```python
self.assertEqual(len(english), len(set(english)))
```

👉 Nếu số lượng khác nhau:
Có từ bị duplicate.

---

## 7. `TestFunctions`

Kiểm tra các hàm chính có tồn tại và callable.

### Những gì class này kiểm tra:

* `get_multiple_choice`
* `mode_1_vietnamese_to_english`
* `mode_2_english_to_vietnamese`
* `save_results`
* `display_results`

### Ví dụ:

```python
self.assertTrue(callable(quiz.save_results))
```

👉 Đảm bảo hàm tồn tại và gọi được.

---

# Hàm `suite()`

```python
def suite():
```

Hàm này gom toàn bộ test class lại thành một “mega test bundle” 🎁

```python
test_suite.addTest(unittest.makeSuite(TestVocabulary))
```

👉 Nghĩa là:
Thêm toàn bộ test của class vào suite.

---

# Cách chạy test

## 1. Chạy tất cả test

```bash
python test_Baocaocuoiky.py
```

Hoặc:

```bash
python -m unittest test_Baocaocuoiky -v
```

`-v` = verbose mode
Hiển thị chi tiết từng test.

---

## 2. Chạy một TestClass cụ thể

### Ví dụ:

```bash
python -m unittest test_Baocaocuoiky.TestVocabulary -v
```

👉 Chỉ chạy test liên quan vocabulary.

---

## 3. Chạy một test method cụ thể

### Ví dụ:

```bash
python -m unittest test_Baocaocuoiky.TestVocabulary.test_vocabulary_has_20_words -v
```

👉 Chỉ chạy đúng 1 test duy nhất.

---

# Expected Output

Nếu mọi thứ OK:

```text
test_vocabulary_exists ... ok
test_returns_4_options ... ok
test_file_created ... ok

Ran 32 tests in 0.12s

OK
```

Nếu fail:

```text
FAIL: test_returns_4_options
AssertionError: 3 != 4
```

👉 Nghĩa là hàm chỉ trả về 3 đáp án thay vì 4.

---

# Ý nghĩa thực tế của bộ test này

Bộ test giúp:

* Phát hiện bug sớm
* Kiểm tra sau khi sửa code
* Đảm bảo không “fix chỗ này vỡ chỗ kia”
* Tự động kiểm tra thay vì test tay

Nó giống hệ thống báo động laser trong phim trộm két sắt 🎯
Code vừa lệch logic một chút là còi hú ngay.
