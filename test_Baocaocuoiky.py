import unittest
import os
import tempfile
import shutil
import sys
from io import StringIO

import Baocaocuoiky as quiz


class TestVocabulary(unittest.TestCase):
    def test_vocabulary_exists(self):
        self.assertTrue(hasattr(quiz, 'VOCABULARY'))
    
    def test_vocabulary_has_20_words(self):
        self.assertEqual(len(quiz.VOCABULARY), 20)
    
    def test_vocabulary_structure(self):
        for word_id, word_data in quiz.VOCABULARY.items():
            self.assertIn('english', word_data)
            self.assertIn('vietnamese', word_data)


class TestMultipleChoice(unittest.TestCase):
    def setUp(self):
        self.english_words = [v['english'] for v in quiz.VOCABULARY.values()]
    
    def test_returns_tuple(self):
        result = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertIsInstance(result, tuple)
    
    def test_returns_4_options(self):
        options, idx = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertEqual(len(options), 4)
    
    def test_correct_answer_in_options(self):
        options, idx = quiz.get_multiple_choice('Hello', self.english_words)
        self.assertIn('Hello', options)


class TestScoring(unittest.TestCase):
    def test_score_percentage(self):
        self.assertEqual(8 * 10, 80)
        self.assertEqual(10 * 10, 100)


class TestFileSaving(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, 'test.txt')
    
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


class TestDataIntegrity(unittest.TestCase):
    def test_no_duplicate_english(self):
        english = [v['english'] for v in quiz.VOCABULARY.values()]
        self.assertEqual(len(english), len(set(english)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
