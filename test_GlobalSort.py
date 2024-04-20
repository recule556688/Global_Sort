import unittest
import shutil
from pathlib import Path
from src.utils import sort_files
from src.language import os_language


class TestSortFiles(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = Path("test_dir")
        self.test_dir.mkdir(exist_ok=True)

        # Create a test file in the directory
        self.test_file_txt = self.test_dir / "test_file.txt"
        self.test_file_txt.touch()
        self.test_file_mp3 = self.test_dir / "test_file.mp3"
        self.test_file_mp3.touch()

        # Define a simple extension map for testing
        self.extensions = {".txt": "Text Files", ".mp3": "Music"}

    def tearDown(self):
        # Clean up the test directory after each test
        shutil.rmtree(self.test_dir)

    def test_sort_files_existing_extension(self):
        # Call the function with the test directory and extension map
        sort_files(self.test_dir, self.extensions, True, True)

        # Check that the file has been moved to the correct directory
        self.assertTrue(
            (self.test_dir / "Text Files" / "test_file.txt").exists(),
            "File not found in the expected directory",
        )
        self.assertTrue(
            (self.test_dir / "Music" / "test_file.mp3").exists(),
            "File not found in the expected directory",
        )

    def test_sort_files_non_existing_extension(self):
        # Call the function with the test directory and extension map
        sort_files(self.test_dir, self.extensions, True, True)

        # Check that the file has been moved to the 'Divers' directory
        self.assertFalse(
            (self.test_dir / "Divers" / "test_file.txt").exists(),
            "File found in the 'Divers' directory",
        )
        self.assertFalse(
            (self.test_dir / "Divers" / "test_file.mp3").exists(),
            "File found in the 'Divers' directory",
        )

    def test_sort_files_no_create_dir(self):
        # Call the function with the test directory and extension map, but with create_dir set to False
        sort_files(self.test_dir, self.extensions, False, False)

        # Check that the file has not been moved
        self.assertTrue(
            self.test_file_txt.exists(),
            "File was moved despite create_dir being False",
        )
        self.assertTrue(
            self.test_file_mp3.exists(),
            "File was moved despite create_dir being False",
        )

    def test_sort_files_empty_directory(self):
        # Create an empty directory for this test
        empty_dir = self.test_dir / "empty_dir"
        empty_dir.mkdir()

        # Call the function with the empty directory and extension map
        sort_files(empty_dir, self.extensions, True, True)

        # Check that no new directories have been created
        self.assertEqual(
            len(list(empty_dir.iterdir())),
            0,
            "New directories were created in an empty directory",
        )

    def test_system_language_detection(self):
        # Call the function to get the system language
        lang = os_language

        # Check that the language is not None or empty
        self.assertIsNotNone(
            lang,
            "System language detection failed",
        )
        self.assertNotEqual(
            lang,
            "",
            "System language detection failed",
        )

    def test_sort_files_nonexistent_directory(self):
        # Define a path to a non-existent directory
        non_existent_dir = self.test_dir / "non_existent_dir"

        # Call the function with the non-existent directory and check the return value
        sorted_flag, sorted_folders = sort_files(
            non_existent_dir, self.extensions, True, True
        )

        # Assert that sorted_flag is False and sorted_folders is an empty set
        self.assertFalse(sorted_flag)
        self.assertEqual(sorted_folders, set())


if __name__ == "__main__":
    unittest.main()
