import tkinter as tk

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

    def submit_command(self, event):
        """Read a command from the input field and display it."""
        command = self.command_entry.get()

        if command:
            self.output.insert(tk.END, f"> {command}\n")
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