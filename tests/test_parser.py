import os
import unittest

from src.main import ShellGUI


class TestParser(unittest.TestCase):
    """Tests for command parsing."""

    def test_command_without_arguments(self):
        name, arguments = ShellGUI.parse_command(None, "ls")

        self.assertEqual(name, "ls")
        self.assertEqual(arguments, [])

    def test_command_with_arguments(self):
        name, arguments = ShellGUI.parse_command(
            None,
            "cd documents",
        )

        self.assertEqual(name, "cd")
        self.assertEqual(arguments, ["documents"])

    def test_multiple_arguments(self):
        name, arguments = ShellGUI.parse_command(
            None,
            "ls folder1 folder2",
        )

        self.assertEqual(name, "ls")
        self.assertEqual(arguments, ["folder1", "folder2"])

    def test_environment_variable_expansion(self):
        os.environ["TEST_VFS_PATH"] = "test_directory"

        name, arguments = ShellGUI.parse_command(
            None,
            "cd $TEST_VFS_PATH",
        )

        self.assertEqual(name, "cd")
        self.assertEqual(arguments, ["test_directory"])


if __name__ == "__main__":
    unittest.main()