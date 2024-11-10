import unittest
from math_quiz import generate_random_integer, generate_random_operator, create_problem
class TestMathGame(unittest.TestCase):
    """Unit tests for math quiz functions."""
    def test_generate_random_integer(self):
        """Test that generate_random_integer returns a number within the range.
        Args:
            self: instance of the test class.
        Asserts:
            Each generated integer is within the range [min_val, max_val].
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"{rand_num} is out of range")

    def test_generate_random_operator(self):
        """Test that generate_random_operator returns expected operators.
        Args:
            self:  instance of the test class.
        Asserts:
             generated operator is allowed operators ('+', '-', '*').
        """
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = generate_random_operator()
            self.assertIn(operator, operators, f"Unexpected operator {operator}")

    def test_create_problem(self):
        """Test that create_problem returns the correct problem string and answer.
        Args:
            self: instance of the test class.
        Asserts:
             returned problem string and answer match the expected values for each test case.
        """
        test_cases = [
            (9, 8, '+', '9 + 8', 17),
            (8, 1, '-', '8 - 1', 7),
            (9, 2, '*', '9 * 2', 18),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Expected problem '{expected_problem}', got '{problem}'")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer}, got {answer}")
if __name__ == "__main__":
    unittest.main()
