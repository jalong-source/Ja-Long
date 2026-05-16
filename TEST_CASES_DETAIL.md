# Test Case Documentation - Hướng Dẫn Kiểm Thử Chi Tiết

## Tổng quan (Overview)

File `test_Baocaocuoiky.py` chứa bộ kiểm thử toàn diện cho chương trình Trắc Nghiệm Tiếng Anh.

Sử dụng Python `unittest` framework để kiểm thử các chức năng chính:
- Database từ vựng
- Tạo câu hỏi trắc nghiệm
- Tính toán điểm số
- Lưu kết quả
- Xử lý lỗi nhập liệu

---

## Cách chạy Test

### 1. Chạy tất cả các test:
```bash
python test_Baocaocuoiky.py
```

### 2. Chạy một test class cụ thể:
```bash
python -m unittest test_Baocaocuoiky.TestVocabularyDatabase -v
```

### 3. Chạy một test method cụ thể:
```bash
python -m unittest test_Baocaocuoiky.TestVocabularyDatabase.test_vocabulary_has_20_words -v
```

### 4. Chạy với verbose output:
```bash
python -m unittest test_Baocaocuoiky -v
```

---

## Chi tiết các Test Class

### 1. TestVocabularyDatabase (7 tests)

**Mục đích**: Kiểm tra tính chính xác của cơ sở dữ liệu từ vựng

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_vocabulary_exists` | Kiểm tra vocabulary dictionary tồn tại | PASS |
| `test_vocabulary_has_20_words` | Kiểm tra có đúng 20 từ | 20 items |
| `test_vocabulary_structure` | Kiểm tra cấu trúc mỗi entry | Có 'english' và 'vietnamese' |
| `test_vocabulary_ids` | Kiểm tra ID từ 1-20 | IDs: 1, 2, ..., 20 |
| `test_vocabulary_english_words` | Kiểm tra có các từ Anh mẫu | 'Hello', 'Goodbye' có tồn tại |
| `test_vocabulary_vietnamese_words` | Kiểm tra có các từ Việt mẫu | 'Xin chào', 'Tạm biệt' có tồn tại |

**Ví dụ chạy:**
```bash
python -m unittest test_Baocaocuoiky.TestVocabularyDatabase.test_vocabulary_has_20_words -v
```

---

### 2. TestMultipleChoice (6 tests)

**Mục đích**: Kiểm tra logic tạo câu trắc nghiệm

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_multiple_choice_returns_tuple` | Kiểm tra hàm trả về tuple | Tuple(options, correct_index) |
| `test_multiple_choice_options_count` | Kiểm tra có đúng 4 lựa chọn | 4 options |
| `test_multiple_choice_correct_answer_included` | Kiểm tra đáp án đúng có trong danh sách | Correct answer in options |
| `test_multiple_choice_correct_index_valid` | Kiểm tra index đáp án đúng hợp lệ | Index: 0-3 |
| `test_multiple_choice_no_duplicates` | Kiểm tra không có lựa chọn trùng | 4 unique options |
| `test_multiple_choice_with_vietnamese` | Kiểm tra tạo câu hỏi tiếng Việt | 4 unique Vietnamese options |

**Ví dụ chạy:**
```bash
python -m unittest test_Baocaocuoiky.TestMultipleChoice -v
```

---

### 3. TestInputValidation (2 tests)

**Mục đích**: Kiểm tra xử lý đầu vào từ người dùng

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_invalid_then_valid_input` | Kiểm tra xử lý input sai rồi đúng | Chấp nhận input hợp lệ |
| `test_choice_validation` | Kiểm tra lựa chọn menu 0-3 | Valid choices: 0, 1, 2, 3 |

---

### 4. TestResultsCalculation (2 tests)

**Mục đích**: Kiểm tra tính toán điểm số

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_score_ranges` | Kiểm tra điểm số trong phạm vi | Score: 0-10 (mode), 0-20 (total) |
| `test_percentage_calculation` | Kiểm tra tính toán phần trăm | 8/10 = 80%, 17/20 = 85% |

---

### 5. TestFileSaving (4 tests)

**Mục đích**: Kiểm tra lưu kết quả vào file

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_save_results_creates_file` | Kiểm tra file được tạo | File exists |
| `test_save_results_file_content` | Kiểm tra nội dung file | Có THỜI GIAN, CHỈ TIÊU, Điểm số |
| `test_save_results_with_wrong_answers` | Kiểm tra lưu câu sai | File chứa câu hỏi, đáp án sai |
| `test_save_results_append_mode` | Kiểm tra append mode | File size tăng sau mỗi lần lưu |

**Ví dụ chạy:**
```bash
python -m unittest test_Baocaocuoiky.TestFileSaving -v
```

---

### 6. TestDisplayResults (2 tests)

**Mục đích**: Kiểm tra hiển thị kết quả trên màn hình

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_display_results_output` | Kiểm tra output trên console | Có KẾT QUẢ, CHỈ TIÊU 1, CHỈ TIÊU 2 |
| `test_display_results_with_wrong_answers` | Kiểm tra hiển thị câu sai | Output chứa câu trả lời sai |

---

### 7. TestIntegration (2 tests)

**Mục đích**: Kiểm tra tích hợp các module

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_vocabulary_english_to_vietnamese_matching` | Kiểm tra song ánh Anh-Việt | 20 from English = 20 from Vietnamese |
| `test_multiple_choice_generation_flow` | Kiểm tra flow tạo câu hỏi | Options, correct_index hợp lệ |

---

### 8. TestEdgeCases (3 tests)

**Mục đích**: Kiểm tra các trường hợp biên

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_perfect_score` | Kiểm tra điểm tuyệt đối | Score: 20/20, 100% |
| `test_zero_score` | Kiểm tra điểm không | Score: 0/20, 0% |
| `test_mixed_score` | Kiểm tra các điểm khác nhau | Scores: 0-10 valid |

---

### 9. TestDataIntegrity (3 tests)

**Mục đích**: Kiểm tra toàn vẹn dữ liệu

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_vocabulary_no_empty_strings` | Kiểm tra không có string rỗng | Tất cả từ không rỗng |
| `test_vocabulary_unique_english_words` | Kiểm tra từ Anh duy nhất | 20 unique English words |
| `test_vocabulary_unique_vietnamese_words` | Kiểm tra từ Việt duy nhất | 20 unique Vietnamese words |

---

### 10. TestScoring (2 tests)

**Mục đích**: Kiểm tra hệ thống tính điểm

| Test | Mô tả | Expected Result |
|------|-------|-----------------|
| `test_score_percentage_calculation` | Kiểm tra chuyển đổi % | 5 points = 50%, 10 points = 100% |
| `test_total_score_calculation` | Kiểm tra tính tổng điểm | 8+9=17, 17*5=85% |

---

## Tổng số Test Cases

```
TestVocabularyDatabase:      7 tests
TestMultipleChoice:           6 tests
TestInputValidation:          2 tests
TestResultsCalculation:       2 tests
TestFileSaving:               4 tests
TestDisplayResults:           2 tests
TestIntegration:              2 tests
TestEdgeCases:                3 tests
TestDataIntegrity:            3 tests
TestScoring:                  2 tests
────────────────────────────────────
TỔNG CỘNG:                   33 tests
```

---

## Expected Output Khi Chạy Tất Cả Tests

```
======================================================================
ENGLISH VOCABULARY QUIZ - TEST SUITE
======================================================================

Running all test cases...

test_vocabulary_exists (test_Baocaocuoiky.TestVocabularyDatabase) ... ok
test_vocabulary_has_20_words (test_Baocaocuoiky.TestVocabularyDatabase) ... ok
...
[Tất cả 33 test sẽ được chạy]
...

======================================================================
TEST SUMMARY
======================================================================
Tests run: 33
Successes: 33
Failures: 0
Errors: 0
======================================================================
```

---

## Các Test Case Cụ Thể - Ví Dụ Chi Tiết

### Example 1: Test Vocabulary
```python
def test_vocabulary_has_20_words(self):
    """Test that vocabulary contains 20 words"""
    self.assertEqual(len(self.vocabulary), 20)
```

**Chạy:**
```bash
python -m unittest test_Baocaocuoiky.TestVocabularyDatabase.test_vocabulary_has_20_words -v
```

**Output nếu thành công:**
```
test_vocabulary_has_20_words (...TestVocabularyDatabase) ... ok
```

---

### Example 2: Test Multiple Choice
```python
def test_multiple_choice_options_count(self):
    """Test that multiple choice returns 4 options"""
    correct_answer = "Hello"
    all_items = [v["english"] for v in self.vocabulary.values()]
    options, correct_index = quiz_program.get_multiple_choice(correct_answer, all_items)
    self.assertEqual(len(options), 4)
```

**Chạy:**
```bash
python -m unittest test_Baocaocuoiky.TestMultipleChoice.test_multiple_choice_options_count -v
```

---

### Example 3: Test File Saving
```python
def test_save_results_creates_file(self):
    """Test that save_results creates a file"""
    test_results = {
        'mode1_score': 8,
        'mode1_wrong': [],
        'mode2_score': 9,
        'mode2_wrong': []
    }
    quiz_program.save_results(test_results, self.test_file)
    self.assertTrue(os.path.exists(self.test_file))
```

**Chạy:**
```bash
python -m unittest test_Baocaocuoiky.TestFileSaving.test_save_results_creates_file -v
```

---

## Troubleshooting Test Issues

### Issue 1: "ModuleNotFoundError: No module named 'Baocaocuoiky'"
**Giải pháp**: Đảm bảo file `test_Baocaocuoiky.py` và `Baocaocuoiky.py` cùng thư mục

### Issue 2: "test file not found"
**Giải pháp**: File test tự động tạo và xóa, không cần lo

### Issue 3: "Test fails with AttributeError"
**Giải pháp**: Kiểm tra hàm trong `Baocaocuoiky.py` tồn tại và có đúng tên

### Issue 4: File test lại sinh ra sau khi chạy
**Giải pháp**: Đó là bình thường, file test sẽ được xóa sau khi test kết thúc

---

## Coverage Report

Để tạo coverage report:

```bash
pip install coverage
coverage run -m unittest test_Baocaocuoiky
coverage report -m
```

---

## Kết luận

Bộ test này kiểm tra:
- ✅ Toàn vẹn dữ liệu từ vựng
- ✅ Logic tạo câu trắc nghiệm
- ✅ Tính toán điểm số chính xác
- ✅ Lưu và hiển thị kết quả
- ✅ Xử lý lỗi nhập liệu
- ✅ Trường hợp biên (edge cases)
- ✅ Tích hợp module

---

*Test Suite Version: 1.0*
*Created: May 16, 2026*
*For: Ja-Long English Vocabulary Quiz Project*
