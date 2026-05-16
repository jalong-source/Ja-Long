# Chương trình Trắc Nghiệm Tiếng Anh
# Project: English Vocabulary Quiz
# Description: Program for learning English vocabulary with Vietnamese-English and English-Vietnamese quizzes

from datetime import datetime
import os

# Vocabulary database
VOCABULARY = {
    1: {"english": "Hello", "vietnamese": "Xin chào"},
    2: {"english": "Goodbye", "vietnamese": "Tạm biệt"},
    3: {"english": "Thank you", "vietnamese": "Cảm ơn"},
    4: {"english": "Please", "vietnamese": "Vui lòng"},
    5: {"english": "Sorry", "vietnamese": "Xin lỗi"},
    6: {"english": "Yes", "vietnamese": "Có"},
    7: {"english": "No", "vietnamese": "Không"},
    8: {"english": "Water", "vietnamese": "Nước"},
    9: {"english": "Food", "vietnamese": "Thực phẩm"},
    10: {"english": "Book", "vietnamese": "Sách"},
    11: {"english": "School", "vietnamese": "Trường học"},
    12: {"english": "Teacher", "vietnamese": "Giáo viên"},
    13: {"english": "Student", "vietnamese": "Học sinh"},
    14: {"english": "House", "vietnamese": "Nhà"},
    15: {"english": "Car", "vietnamese": "Ô tô"},
    16: {"english": "Money", "vietnamese": "Tiền"},
    17: {"english": "Time", "vietnamese": "Thời gian"},
    18: {"english": "Day", "vietnamese": "Ngày"},
    19: {"english": "Night", "vietnamese": "Đêm"},
    20: {"english": "Morning", "vietnamese": "Buổi sáng"},
}

def get_multiple_choice(correct_answer, all_items, mode="en_vi"):
    """
    Create multiple choice options with correct answer and 3 random wrong answers
    
    Args:
        correct_answer: The correct answer
        all_items: List of all possible answers
        mode: "en_vi" or "vi_en"
    
    Returns:
        tuple: (list of options, correct_index)
    """
    options = [correct_answer]
    
    # Get 3 wrong answers
    wrong_answers = [item for item in all_items if item != correct_answer]
    import random
    options.extend(random.sample(wrong_answers, 3))
    
    # Shuffle the options
    random.shuffle(options)
    correct_index = options.index(correct_answer)
    
    return options, correct_index

def mode_1_vietnamese_to_english():
    """
    Mode 1: Vietnamese to English
    Shows Vietnamese question, user chooses English answer
    """
    print("\n" + "="*60)
    print("CHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH")
    print("="*60)
    print("Hướng dẫn: Bạn sẽ thấy một từ tiếng Việt, hãy chọn đáp án tiếng Anh đúng")
    print("Bạn cần trả lời đúng 10 câu hỏi\n")
    
    import random
    questions = list(VOCABULARY.keys())
    random.shuffle(questions)
    questions = questions[:10]  # Take first 10 questions
    
    score = 0
    wrong_answers = []
    
    for question_num, word_id in enumerate(questions, 1):
        word = VOCABULARY[word_id]
        vietnamese = word["vietnamese"]
        english = word["english"]
        
        # Get all english answers
        all_english = [VOCABULARY[i]["english"] for i in VOCABULARY.keys()]
        
        # Create multiple choice
        options, correct_index = get_multiple_choice(english, all_english)
        
        print(f"Câu {question_num}/10: {vietnamese} là tiếng Anh gì?")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                user_answer = int(input("Chọn câu trả lời (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Vui lòng nhập số từ 1 đến 4!")
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")
        
        user_answer_index = user_answer - 1
        
        if user_answer_index == correct_index:
            print("✓ Đúng!\n")
            score += 1
        else:
            print(f"✗ Sai! Đáp án đúng là: {english}\n")
            wrong_answers.append({
                "question": vietnamese,
                "correct_answer": english,
                "user_answer": options[user_answer_index]
            })
    
    return score, wrong_answers

def mode_2_english_to_vietnamese():
    """
    Mode 2: English to Vietnamese
    Shows English question, user chooses Vietnamese answer
    """
    print("\n" + "="*60)
    print("CHỈ TIÊU 2: TRẮC NGHIỆM TIẾNG ANH → TIẾNG VIỆT")
    print("="*60)
    print("Hướng dẫn: Bạn sẽ thấy một từ tiếng Anh, hãy chọn đáp án tiếng Việt đúng")
    print("Bạn cần trả lời đúng 10 câu hỏi\n")
    
    import random
    questions = list(VOCABULARY.keys())
    random.shuffle(questions)
    questions = questions[:10]  # Take first 10 questions
    
    score = 0
    wrong_answers = []
    
    for question_num, word_id in enumerate(questions, 1):
        word = VOCABULARY[word_id]
        vietnamese = word["vietnamese"]
        english = word["english"]
        
        # Get all vietnamese answers
        all_vietnamese = [VOCABULARY[i]["vietnamese"] for i in VOCABULARY.keys()]
        
        # Create multiple choice
        options, correct_index = get_multiple_choice(vietnamese, all_vietnamese)
        
        print(f"Câu {question_num}/10: {english} là tiếng Việt gì?")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                user_answer = int(input("Chọn câu trả lời (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Vui lòng nhập số từ 1 đến 4!")
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")
        
        user_answer_index = user_answer - 1
        
        if user_answer_index == correct_index:
            print("✓ Đúng!\n")
            score += 1
        else:
            print(f"✗ Sai! Đáp án đúng là: {vietnamese}\n")
            wrong_answers.append({
                "question": english,
                "correct_answer": vietnamese,
                "user_answer": options[user_answer_index]
            })
    
    return score, wrong_answers

def save_results(results, filename="ket_qua_quiz.txt"):
    """
    Save quiz results to a text file
    
    Args:
        results: Dictionary containing quiz results
        filename: Output filename
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, 'a', encoding='utf-8') as file:
        file.write("\n" + "="*70 + "\n")
        file.write(f"THỜI GIAN: {timestamp}\n")
        file.write("="*70 + "\n\n")
        
        # Mode 1 Results
        file.write("CHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH\n")
        file.write(f"Điểm số: {results['mode1_score']}/10\n")
        file.write(f"Phần trăm: {results['mode1_score']*10}%\n")
        
        if results['mode1_wrong']:
            file.write("\nCác câu trả lời sai:\n")
            for i, item in enumerate(results['mode1_wrong'], 1):
                file.write(f"  {i}. Câu hỏi: {item['question']}\n")
                file.write(f"     Đáp án đúng: {item['correct_answer']}\n")
                file.write(f"     Đáp án của bạn: {item['user_answer']}\n")
        else:
            file.write("\nTất cả câu trả lời đều chính xác!\n")
        
        file.write("\n" + "-"*70 + "\n\n")
        
        # Mode 2 Results
        file.write("CHỈ TIÊU 2: TRẮC NGHIỆM TIẾNG ANH → TIẾNG VIỆT\n")
        file.write(f"Điểm số: {results['mode2_score']}/10\n")
        file.write(f"Phần trăm: {results['mode2_score']*10}%\n")
        
        if results['mode2_wrong']:
            file.write("\nCác câu trả lời sai:\n")
            for i, item in enumerate(results['mode2_wrong'], 1):
                file.write(f"  {i}. Câu hỏi: {item['question']}\n")
                file.write(f"     Đáp án đúng: {item['correct_answer']}\n")
                file.write(f"     Đáp án của bạn: {item['user_answer']}\n")
        else:
            file.write("\nTất cả câu trả lời đều chính xác!\n")
        
        file.write("\n" + "-"*70 + "\n")
        
        # Total score
        total_score = results['mode1_score'] + results['mode2_score']
        file.write(f"\nTổng điểm: {total_score}/20\n")
        file.write(f"Tổng phần trăm: {total_score*5}%\n")
        file.write("="*70 + "\n\n")
    
    print(f"\n✓ Kết quả đã được lưu vào file: {filename}")

def display_results(results):
    """
    Display quiz results to console
    """
    print("\n" + "="*60)
    print("KẾT QUẢ TRẮC NGHIỆM")
    print("="*60)
    
    # Mode 1 Results
    print("\nCHỈ TIÊU 1: TRẮC NGHIỆM TIẾNG VIỆT → TIẾNG ANH")
    print(f"Điểm số: {results['mode1_score']}/10")
    print(f"Phần trăm: {results['mode1_score']*10}%")
    
    if results['mode1_wrong']:
        print("\nCác câu trả lời sai:")
        for i, item in enumerate(results['mode1_wrong'], 1):
            print(f"  {i}. {item['question']}")
            print(f"     Đáp án đúng: {item['correct_answer']}")
            print(f"     Đáp án của bạn: {item['user_answer']}")
    
    print("\n" + "-"*60)
    
    # Mode 2 Results
    print("\nCHỈ TIÊU 2: TRẮC NGHIỆM TIẾNG ANH → TIẾNG VIỆT")
    print(f"Điểm số: {results['mode2_score']}/10")
    print(f"Phần trăm: {results['mode2_score']*10}%")
    
    if results['mode2_wrong']:
        print("\nCác câu trả lời sai:")
        for i, item in enumerate(results['mode2_wrong'], 1):
            print(f"  {i}. {item['question']}")
            print(f"     Đáp án đúng: {item['correct_answer']}")
            print(f"     Đáp án của bạn: {item['user_answer']}")
    
    print("\n" + "-"*60)
    
    # Total score
    total_score = results['mode1_score'] + results['mode2_score']
    print(f"\nTổng điểm: {total_score}/20")
    print(f"Tổng phần trăm: {total_score*5}%")
    print("="*60 + "\n")

def main():
    """
    Main program function
    """
    print("\n" + "="*60)
    print("CHƯƠNG TRÌNH TRẮC NGHIỆM TIẾNG ANH")
    print("Học từ vựng tiếng Anh dễ dàng")
    print("="*60)
    
    print("\nVui lòng chọn chế độ:")
    print("1. Chỉ làm bài trắc nghiệm Tiếng Việt → Tiếng Anh")
    print("2. Chỉ làm bài trắc nghiệm Tiếng Anh → Tiếng Việt")
    print("3. Làm cả hai bài trắc nghiệm")
    print("0. Thoát chương trình")
    
    while True:
        try:
            choice = int(input("\nNhập lựa chọn của bạn (0-3): "))
            if 0 <= choice <= 3:
                break
            else:
                print("Vui lòng nhập số từ 0 đến 3!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")
    
    results = {
        'mode1_score': 0,
        'mode1_wrong': [],
        'mode2_score': 0,
        'mode2_wrong': []
    }
    
    if choice == 0:
        print("\nCảm ơn đã sử dụng chương trình. Tạm biệt!")
        return
    
    elif choice == 1:
        results['mode1_score'], results['mode1_wrong'] = mode_1_vietnamese_to_english()
    
    elif choice == 2:
        results['mode2_score'], results['mode2_wrong'] = mode_2_english_to_vietnamese()
    
    elif choice == 3:
        results['mode1_score'], results['mode1_wrong'] = mode_1_vietnamese_to_english()
        results['mode2_score'], results['mode2_wrong'] = mode_2_english_to_vietnamese()
    
    # Display results
    display_results(results)
    
    # Save results to file
    save_results(results)
    
    # Ask if user wants to continue
    while True:
        again = input("Bạn muốn tiếp tục (C/N)? ").strip().upper()
        if again in ['C', 'Y', 'CÓ']:
            main()
            break
        elif again in ['N', 'K', 'KHÔNG']:
            print("Cảm ơn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Vui lòng nhập C (Có) hoặc N (Không)")

if __name__ == "__main__":
    main()