import unittest

from functions.get_files_info import get_files_info


class GetFileInfoTests(unittest.TestCase):
    def test_calculator(self):
        result = get_files_info("calculator", ".")
        test = """ - main.py: file_size=576 bytes, is_dir=False
 - tests.py: file_size=1343 bytes, is_dir=False
 - pkg: file_size=92 bytes, is_dir=True
 - lorem.txt: file_size=28 bytes, is_dir=False"""
        self.assertEqual(result, test)

    def test_outside(self):
        result = get_files_info("calculator", "/bin")
        test = """Error: Cannot list "/bin" as it is outside the permitted working directory"""
        self.assertEqual(result, test)

    def test_outside2(self):
        result = get_files_info("calculator", "../")
        test = """Error: Cannot list "../" as it is outside the permitted working directory"""
        self.assertEqual(result, test)

    def test_calc_pkg(self):
        result = get_files_info("calculator", "pkg")
        test = """ - calculator.py: file_size=1739 bytes, is_dir=False
 - render.py: file_size=768 bytes, is_dir=False
 - __pycache__: file_size=96 bytes, is_dir=True
 - morelorem.txt: file_size=26 bytes, is_dir=False"""
        self.assertEqual(result, test)


if __name__ == "__main__":
    unittest.main()
