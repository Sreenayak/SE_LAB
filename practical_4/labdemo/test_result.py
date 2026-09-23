import unittest
from result import get_result

TEST_DATA = [
    ("TC01", 0, "Fail"),
    ("TC02", 39, "Fail"),
    ("TC03", 40, "Pass"),
    ("TC04", 41, "Pass"),
    ("TC05", 75, "Pass"),
    ("TC06", 100, "Pass"),
    ("TC07", -1, "Invalid"),
    ("TC08", 101, "Invalid"),
]
class TestStudentResult(unittest.TestCase):
    def test_marks_from_table(self):
        for case_id, marks, expected in TEST_DATA:
            with self.subTest(case_id=case_id, marks=marks):
                actual = get_result(marks)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
