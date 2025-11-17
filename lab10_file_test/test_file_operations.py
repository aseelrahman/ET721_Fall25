"""
Aseel Rahman
OCT 15, 2025
Lab 9 file operation test
"""

import unittest
import os
from file_operations import email_read


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test
        self.filename = "test_file.txt"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        # test writing text to a file
        msg = "Aseel Rahman"
        with open(self.filename, "w") as f:
            f.write(msg)

        # verify file exist and content matches
        self.asserTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result, msg)

    def test_read_file(self):
        # test reading text from a file
        expected_content = "Read me!"
        with open(self.filename, "w") as file:
            f.write(expected_content)

        with open(self.filename, "r") as f:
            data = f.read()

        self.assertEqual(data, expected_content)

    def test_append_file(self):
        # test appending text to an existing file
        initial_content = "Line one"
        append_content = "\nLine two"

        with open(self.filename, "w") as f:
            f.write(initial_content)

        with open(self.filename, "a") as f:
            f.write(append_content)

        with open(self.filename, "r") as f:
            final_data = f.read()

        self.assertEqual(final_data, initial_content + append_content)

    # EXERCISE
    def test_d(self):
        with open(self.filename, "w") as f:
            f.write("john@gmail.com\n")
            f.write("mary@yahoo.com\n")
            f.write("ali@hotmail.com\n")
            f.write("sara@gmail.com\n")
        f.write("test@yahoo.com\n")

        count_gmail = email_read(self.filename, "@gmail")
        count_yahoo = email_read(self.filename, "@yahoo")
        count_hotmail = email_read(self.filename, "@hotmail")

        self.assertEqual(count_gmail, 2)
        self.assertEqual(count_yahoo, 2)
        self.assertEqual(count_hotmail, 1)


# run the unit tests automatically when the file is run
if __name__ == " __main__ ":
    unittest.main()
