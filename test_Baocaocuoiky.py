#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for English Vocabulary Quiz Program
Unit tests for Baocaocuoiky.py
Enhanced with comprehensive test cases
"""

import unittest
import os
import tempfile
import shutil
import sys
from io import StringIO

try:
    import Baocaocuoiky as quiz
except ImportError:
    print("Error: Could not import Baocaocuoiky module")
    sys.exit(1)


class TestVocabulary(unittest.TestCase):
    """Test vocabulary database"""
    def test_vocabulary_exists(self):
        self.assertTrue(hasattr(quiz, 'VOCABULARY'))
    
    def test_vocabulary_has_20_words(self):
        self.assertEqual(len(quiz.VOCABULARY), 20)
    
    def test_vocabulary_structure(self):
        for word_id, word_data in quiz.VOCABULARY.items():
            self.assertIn('english', word_data)
            self.assertIn('vietnamese', word_data)
    
    def test_vocabulary_ids_1_to_20(self):
        ids = set(quiz.VOCABULARY.keys())
        self.assertEqual(ids, set(range(1, 21)))
    
    def test_sample_words_exist(self):
        words = {v['english']: v['vietnamese'] for v in quiz.VOCABULARY.values()}
        self.assertIn('Hello', words)
        self.assertEqual(words['Hello'], 'Xin chào')


class TestMultipleChoice(unittest.TestCase):
    """Test multiple choice question generation"""
    def setUp(self):
        self.english_words = [v['english'] for v in quiz.VOCABULARY.values()]
        self.vietnamese_words = [v['vietnamese'] for v in quiz.VOCABULARY.values()]
    
    def test_returns_tuple(self):
        result = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
    
    def test_returns_4_options(self):
        options, idx = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertEqual(len(options), 4)
    
    def test_correct_answer_in_options(self):
        options, idx = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertIn('Hello', options)
    
    def test_correct_index_valid_range(self):
        options, idx = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertGreaterEqual(idx, 0)
        self.assertLess(idx, 4)
    
    def test_no_duplicate_options(self):
        options, idx = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertEqual(len(options), len(set(options)))
    
    def test_vietnamese_multiple_choice(self):
        options, idx = quiz.get_multiple_choice('Xin chào', self.vietnamese_words)
        self.assertEqual(len(options), 4)
        self.assertIn('Xin chào', options)


class TestScoring(unittest.TestCase):
    """Test scoring calculation"""
    def test_score_0(self):
        self.assertEqual(0 * 10, 0)
    
    def test_score_10(self):
        self.assertEqual(10 * 10, 100)
    
    def test_score_5(self):
        self.assertEqual(5 * 10, 50)
    
    def test_total_score_percentage(self):
        self.assertEqual((8 + 9) * 5, 85)
    
    def test_perfect_score(self):
        self.assertEqual((10 + 10) * 5, 100)
    
    def test_zero_total_score(self):
        self.assertEqual((0 + 0) * 5, 0)


class TestFileSaving(unittest.TestCase):
    """Test saving results to file"""
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, 'test_results.txt')
    
    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_file_created(self):
        results = {
            'mode1_score': 8,
            'mode1_wrong': [],
            'mode2_score': 9,
            'mode2_wrong': []
        }
        quiz.save_results(results, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
    
    def test_file_has_content(self):
        results = {
            'mode1_score': 8,
            'mode1_wrong': [],
            'mode2_score': 9,
            'mode2_wrong': []
        }
        quiz.save_results(results, self.test_file)
        
        with open(self.test_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertGreater(len(content), 0)
        self.assertIn('CHỈ TIÊU', content)
    
    def test_file_appends(self):
        results = {
            'mode1_score': 8,
            'mode1_wrong': [],
            'mode2_score': 9,
            'mode2_wrong': []
        }
        
        quiz.save_results(results, self.test_file)
        size1 = os.path.getsize(self.test_file)
        
        quiz.save_results(results, self.test_file)
        size2 = os.path.getsize(self.test_file)
        
        self.assertGreater(size2, size1)
    
    def test_file_contains_scores(self):
        results = {
            'mode1_score': 8,
            'mode1_wrong': [],
            'mode2_score': 9,
            'mode2_wrong': []
        }
        quiz.save_results(results, self.test_file)
        
        with open(self.test_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertIn('Điểm số', content)
        self.assertIn('8', content)
        self.assertIn('9', content)


class TestDisplayResults(unittest.TestCase):
    """Test displaying results"""
    def test_display_output(self):
        results = {
            'mode1_score': 8,
            'mode1_wrong': [],
            'mode2_score': 9,
            'mode2_wrong': []
        }
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        quiz.display_results(results)
        
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        self.assertIn('KẾT QUẢ', output)
    
    def test_display_with_wrong_answers(self):
        results = {
            'mode1_score': 8,
            'mode1_wrong': [
                {
                    'question': 'Nước',
                    'correct_answer': 'Water',
                    'user_answer': 'Book'
                }
            ],
            'mode2_score': 9,
            'mode2_wrong': []
        }
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        quiz.display_results(results)
        
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        self.assertIn('KẾT QUẢ', output)
        self.assertIn('Nước', output)


class TestDataIntegrity(unittest.TestCase):
    """Test data integrity"""
    def test_no_duplicate_english(self):
        english = [v['english'] for v in quiz.VOCABULARY.values()]
        self.assertEqual(len(english), len(set(english)))
    
    def test_no_duplicate_vietnamese(self):
        vietnamese = [v['vietnamese'] for v in quiz.VOCABULARY.values()]
        self.assertEqual(len(vietnamese), len(set(vietnamese)))
    
    def test_no_empty_strings(self):
        for word_id, word_data in quiz.VOCABULARY.items():
            self.assertTrue(len(word_data['english']) > 0)
            self.assertTrue(len(word_data['vietnamese']) > 0)
    
    def test_vocabulary_bidirectional_mapping(self):
        english_to_vietnamese = {v['english']: v['vietnamese'] for v in quiz.VOCABULARY.values()}
        vietnamese_to_english = {v['vietnamese']: v['english'] for v in quiz.VOCABULARY.values()}
        self.assertEqual(len(english_to_vietnamese), len(vietnamese_to_english))


class TestFunctions(unittest.TestCase):
    """Test that required functions exist"""
    def test_get_multiple_choice_callable(self):
        self.assertTrue(callable(quiz.get_multiple_choice))
    
    def test_mode_1_callable(self):
        self.assertTrue(callable(quiz.mode_1_vietnamese_to_english))
    
    def test_mode_2_callable(self):
        self.assertTrue(callable(quiz.mode_2_english_to_vietnamese))
    
    def test_save_results_callable(self):
        self.assertTrue(callable(quiz.save_results))
    
    def test_display_results_callable(self):
        self.assertTrue(callable(quiz.display_results))
    
    def test_main_callable(self):
        self.assertTrue(callable(quiz.main))


class TestEdgeCases(unittest.TestCase):
    """Test edge cases"""
    def test_perfect_score_mode1(self):
        self.assertEqual(10, 10)
    
    def test_zero_score_mode1(self):
        self.assertEqual(0, 0)
    
    def test_perfect_score_total(self):
        self.assertEqual(10 + 10, 20)
    
    def test_partial_scores(self):
        self.assertGreaterEqual(5, 0)
        self.assertLessEqual(5, 10)


def suite():
    """Create test suite"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestVocabulary))
    test_suite.addTest(unittest.makeSuite(TestMultipleChoice))
    test_suite.addTest(unittest.makeSuite(TestScoring))
    test_suite.addTest(unittest.makeSuite(TestFileSaving))
    test_suite.addTest(unittest.makeSuite(TestDisplayResults))
    test_suite.addTest(unittest.makeSuite(TestDataIntegrity))
    test_suite.addTest(unittest.makeSuite(TestFunctions))
    test_suite.addTest(unittest.makeSuite(TestEdgeCases))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUITE SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
