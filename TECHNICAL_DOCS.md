# Technical Documentation
## Chương trình Trắc Nghiệm Tiếng Anh - Technical Reference

---

## 📐 Architecture Overview

```
┌─────────────────────────────────────────────┐
│         Main Program (main())               │
│  - Menu selection                           │
│  - Mode routing                             │
│  - Result aggregation                       │
└────────────┬────────────────────────────────┘
             │
      ┌──────┼──────┬──────┐
      │      │      │      │
      ▼      ▼      ▼      ▼
   Mode1   Mode2  Save   Display
   (Vi→En) (En→Vi) File   Results
```

---

## 🔍 Module Structure

```python
VOCABULARY           # Dictionary with 20 word pairs
├── Key: int (1-20)
└── Value: dict
    ├── "english": str
    └── "vietnamese": str

Functions:
├── main()                           # Entry point
├── mode_1_vietnamese_to_english()   # Mode 1 implementation
├── mode_2_english_to_vietnamese()   # Mode 2 implementation
├── get_multiple_choice()            # Generate options
├── display_results()                # Show results
└── save_results()                   # Save to file
```

---

## 📚 Data Structure

### VOCABULARY Dictionary

```python
VOCABULARY = {
    1: {"english": "Hello", "vietnamese": "Xin chào"},
    2: {"english": "Goodbye", "vietnamese": "Tạm biệt"},
    # ... 20 total entries
}
```

**Properties:**
- 20 word pairs
- Keys: 1-20 (int)
- Values: dict with "english" and "vietnamese" keys
- Expandable for more words

### Results Dictionary

```python
results = {
    'mode1_score': int,           # 0-10
    'mode1_wrong': [dict, ...],   # List of wrong answers
    'mode2_score': int,           # 0-10
    'mode2_wrong': [dict, ...]    # List of wrong answers
}
```

### Wrong Answer Item

```python
{
    'question': str,           # Vietnamese or English question
    'correct_answer': str,     # Correct answer
    'user_answer': str         # User's incorrect answer
}
```

---

## 🔧 Function Details

### 1. `main()`
**Purpose**: Program entry point and flow control

**Flow**:
1. Display main menu
2. Get user input (0-3)
3. Route to appropriate mode
4. Collect results
5. Display and save results
6. Ask to continue or exit

**Input**: User selection (0-3)
**Output**: Results printed to console and saved to file

---

### 2. `mode_1_vietnamese_to_english()`
**Purpose**: Run Vietnamese to English quiz

**Algorithm**:
1. Display mode header
2. Randomly select 10 questions from VOCABULARY
3. Loop 10 times:
   - Get Vietnamese word
   - Create multiple choice options
   - Display question with 4 options
   - Get user input (1-4)
   - Check answer
   - Record result (correct/wrong)
   - Display feedback
4. Return (score, wrong_answers_list)

**Return**: `tuple(int, list)`
- int: Score (0-10)
- list: Wrong answers with details

---

### 3. `mode_2_english_to_vietnamese()`
**Purpose**: Run English to Vietnamese quiz

**Algorithm**: Same as mode_1 but reversed:
1. Display mode header
2. Randomly select 10 questions
3. Loop 10 times:
   - Get English word
   - Create multiple choice options (Vietnamese)
   - Display question with 4 options
   - Get user input (1-4)
   - Check answer
   - Record result
   - Display feedback
4. Return (score, wrong_answers_list)

**Return**: `tuple(int, list)`

---

### 4. `get_multiple_choice(correct_answer, all_items, mode="en_vi")`
**Purpose**: Generate multiple choice options

**Algorithm**:
1. Start with correct answer
2. Filter out correct answer from all items
3. Randomly sample 3 wrong answers
4. Combine: [correct, wrong1, wrong2, wrong3]
5. Shuffle the list
6. Find index of correct answer
7. Return options and correct index

**Parameters**:
- `correct_answer` (str): The right answer
- `all_items` (list): All possible answers
- `mode` (str): Quiz mode (for future use)

**Return**: `tuple(list, int)`
- list: 4 options (shuffled)
- int: Index of correct answer (0-3)

---

### 5. `save_results(results, filename="ket_qua_quiz.txt")`
**Purpose**: Save results to file

**Algorithm**:
1. Get current timestamp
2. Open file in append mode ('a')
3. Write separator line
4. Write timestamp
5. Write Mode 1 results:
   - Score and percentage
   - List of wrong answers (if any)
6. Write separator
7. Write Mode 2 results:
   - Score and percentage
   - List of wrong answers (if any)
8. Write separator
9. Write total score
10. Close file

**Parameters**:
- `results` (dict): Results dictionary
- `filename` (str): Output filename (default: "ket_qua_quiz.txt")

**Output**: Appends to file, prints confirmation to console

---

### 6. `display_results(results)`
**Purpose**: Display results to console

**Algorithm**:
1. Print header
2. Print Mode 1 results with score, percentage
3. If wrong answers exist, list them
4. Print separator
5. Print Mode 2 results with score, percentage
6. If wrong answers exist, list them
7. Print separator
8. Print total score and percentage
9. Print footer

**Parameters**:
- `results` (dict): Results dictionary

**Output**: Formatted console output

---

## 🎯 Key Design Decisions

### 1. Random Selection
- Uses `random.shuffle()` to randomize questions
- Uses `random.sample()` to select wrong answers
- Ensures variety in each quiz session

### 2. Multiple Choice Format
- Always 4 options (1 correct, 3 wrong)
- Options are shuffled
- Index of correct answer is tracked separately

### 3. File Append Mode
- Uses 'a' (append) instead of 'w' (write)
- Preserves quiz history
- Allows tracking progress over time

### 4. Error Handling
- Input validation for menu selection
- Input validation for answer selection (1-4)
- Try-except for int conversion
- While loops for retry on invalid input

### 5. User Experience
- Shows immediate feedback (✓/✗)
- Shows correct answer if wrong
- Displays questions with clear numbering
- Uses Vietnamese language for all prompts

---

## 📊 Flow Diagrams

### Main Flow
```
Start
  ↓
Show Menu
  ↓
Get User Choice
  ├─ 0 → Exit
  ├─ 1 → Mode 1
  ├─ 2 → Mode 2
  └─ 3 → Mode 1 + Mode 2
  ↓
Run Quiz(es)
  ↓
Display Results
  ↓
Save to File
  ↓
Ask Continue?
  ├─ Yes → Back to Menu
  └─ No → Exit
```

### Quiz Flow (Mode 1/2)
```
Start Quiz
  ↓
For i = 1 to 10:
  ├─ Select random word
  ├─ Create multiple choice
  ├─ Display question
  ├─ Get user input
  ├─ Validate input (1-4)
  ├─ Check answer
  ├─ Show feedback (✓/✗)
  ├─ If wrong, record details
  └─ Continue
  ↓
Calculate score
  ↓
Return (score, wrong_list)
```

---

## 🧪 Testing Strategy

### Unit Tests (Manual)
1. **Test input validation**
   - Invalid menu selection
   - Non-integer input
   - Out-of-range answers

2. **Test scoring**
   - All correct answers = 10/10
   - All wrong answers = 0/10
   - Mixed = various scores

3. **Test multiple choice**
   - Correct answer always present
   - 4 distinct options
   - Options are different each run

4. **Test file output**
   - File created if not exists
   - Results appended (not overwritten)
   - Format is readable
   - Timestamp recorded

### Integration Tests
1. Full quiz flow (menu → quiz → results → file)
2. Multiple sessions (results accumulate)
3. Both modes combined
4. Continue/exit functionality

---

## 🚀 Performance Considerations

**Time Complexity**:
- Per question: O(1) for all operations
- Per quiz: O(n) where n=10
- File I/O: O(1) per session

**Space Complexity**:
- VOCABULARY: O(20) = O(1)
- Results: O(wrong_count) ≤ O(10)
- Total: O(1) space

**Optimization Notes**:
- Random operations are efficient
- File I/O uses buffering
- No unnecessary loops or recursion

---

## 📝 Code Quality

**Best Practices Used**:
- ✅ Function decomposition (DRY principle)
- ✅ Clear variable names
- ✅ Input validation
- ✅ Error handling
- ✅ Comments and docstrings
- ✅ Consistent formatting
- ✅ UTF-8 encoding support

**PEP 8 Compliance**:
- ✅ Function naming (snake_case)
- ✅ Line length < 100 characters
- ✅ Whitespace conventions
- ✅ Docstring format

---

## 🔒 Security Considerations

**Input Validation**:
- User input restricted to expected values
- Integer parsing with try-except
- Filename validation for file operations

**File Handling**:
- Uses encoding='utf-8' for proper Vietnamese support
- Append mode prevents accidental data loss
- No eval() or exec() used

---

## 🌍 Internationalization (i18n)

**Current**:
- All prompts in Vietnamese
- UTF-8 encoding throughout
- Vietnamese characters fully supported

**Future Enhancement**:
- Move strings to i18n dictionary
- Support multiple languages
- Locale-based formatting

---

## 📚 Extension Points

### Easy to Add:
1. **More vocabulary**: Add entries to VOCABULARY dict
2. **Difficulty levels**: Add parameter to filter words
3. **Different question types**: New functions similar to mode_1/mode_2
4. **Statistics**: Add tracking in results
5. **GUI interface**: Replace console I/O with tkinter

### Moderate Complexity:
1. **Database backend**: Replace dict with SQLite
2. **User accounts**: Track individual progress
3. **Web interface**: Convert to Flask/Django
4. **Spaced repetition**: Algorithm for learning optimization

---

## 🐛 Known Limitations

1. **Limited vocabulary**: Only 20 words (easily expandable)
2. **No word categories**: All mixed together
3. **No pronunciation**: No audio support
4. **No word images**: Text only
5. **No progress tracking**: Per-user stats not stored
6. **No difficulty levels**: All words treated equally

---

## 📖 References

**Python Modules Used**:
- `datetime`: For timestamp
- `os`: For file operations
- `random`: For randomization

**Version Requirements**:
- Python 3.x (tested on 3.6+)
- No external dependencies

---

## 👨‍💻 Developer Notes

### To modify vocabulary:
```python
VOCABULARY = {
    # Add new entries:
    21: {"english": "NewWord", "vietnamese": "TừMới"},
    # ...
}
```

### To add new quiz mode:
```python
def mode_3_mixed_quiz():
    # Implementation
    pass

# Add to main() switch statement
```

### To change scoring:
```python
# Change in mode functions:
# score += 2  # Instead of += 1
```

---

*Technical Documentation v1.0*
*Group 2 - Programming Techniques Course*
