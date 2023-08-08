import unittest
import test_cap

class Testcap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = test_cap.cap_text(text)
        self.assertEqual(result, 'Python')
    
    def text_multiply_word(self):
        text = 'learning python'
        result = test_cap.cap_text(text)
        self.assertEqual(result, 'Learning Python')
    
if __name__ == '__main__':
    unittest.main()