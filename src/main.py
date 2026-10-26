import tkinter as tk
import os

VFS_NAME = "MyVFS"

class ShellGUI:
    """Graphical interface for the shell emulator."""

    def __init__(self, root):
        """Initialize the shell emulator interface."""
        self.root = root

        self.output = tk.Text(root)
        self.output.pack(fill=tk.BOTH, expand=True)

        self.command_entry = tk.Entry(root)
        self.command_entry.pack(fill=tk.X)
        self.command_entry.bind("<Return>", self.submit_command)
        self.command_entry.focus()

    def parse_command(self, command):
        """Split user input into a command name and arguments."""
        parts = command.split()
        parts = [os.path.expandvars(part) for part in parts]
        
        command_name = parts[0]
        arguments = parts[1:]

        return command_name, arguments

    def execute_command(self, command_name, arguments):
        """Execute a parsed command."""
        if command_name == "ls":
            self.output.insert(tk.END, f"ls: {arguments}\n")

        elif command_name == "cd":
            if len(arguments) != 1:
                self.output.insert(
                    tk.END,
                    "Error: cd requires exactly one argument\n",
                )
            else:
                self.output.insert(tk.END, f"cd: {arguments}\n")

        elif command_name == "exit":
            if arguments:
                self.output.insert(
                    tk.END,
                    "Error: exit does not accept arguments\n",
                )
            else:
                self.root.destroy()
                return False

        else:
            self.output.insert(
                tk.END,
                f"Error: unknown command: {command_name}\n",
            )

        return True

    def submit_command(self, event):
        """Read a command from the input field and display it."""
        command = self.command_entry.get()

        if command:
            self.output.insert(tk.END, f"> {command}\n")
            command_name, arguments = self.parse_command(command)
            should_continue = self.execute_command(command_name, arguments)
        if should_continue:
            self.command_entry.delete(0, tk.END)

def main():
    """Create and run the shell emulator."""
    root = tk.Tk()
    root.title(f"Shell Emulator - {VFS_NAME}")
    root.geometry("800x500")

    ShellGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()