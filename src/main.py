import tkinter as tk

VFS_NAME = "MyVFS"

def main():
    """Create and run the shell emulator window"""
    root = tk.Tk()
    root.title(f"Shell Emulator - {VFS_NAME}")
    root.geometry("800x500")

    root.mainloop()

if __name__ == "__main__":
    main()