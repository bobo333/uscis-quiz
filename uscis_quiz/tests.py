from unittest.mock import patch
import unittest
import quiz


class QuizTest(unittest.TestCase):

    def test_get_input_from_get_command(self):
        user_input = ['Test Input',]
        expected_input = 'Test Input'
        with patch('builtins.input', side_effect=user_input):
            stacks = quiz.get_command()
        self.assertEqual(stacks, expected_input)


if __name__ == "__main__":
     unittest.main()
