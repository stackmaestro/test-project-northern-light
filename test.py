import unittest
import os
from difference import compare_files

class TestCompareFiles(unittest.TestCase):

    def test_compare_files(self):

        with open('test_file1.txt', 'w') as f1, open('test_file2.txt', 'w') as f2:
            f1.write('line1\nline2\nline3\n')
            f2.write('line2\nline3\nline4\n')

        compare_files('test_file1.txt', 'test_file2.txt', 'test_output1.txt', 'test_output2.txt')

        with open('test_output1.txt', 'r') as out1, open('test_output2.txt', 'r') as out2:
            output1 = out1.read().strip()
            output2 = out2.read().strip()

        self.assertEqual(output1, 'line1')
        self.assertEqual(output2, 'line4')

        os.remove('test_file1.txt')
        os.remove('test_file2.txt')
        os.remove('test_output1.txt')
        os.remove('test_output2.txt')

if __name__ == '__main__':
    unittest.main()

