import tkinter as tk  # Import the tkinter module
from tkinter.filedialog import askopenfilename, asksaveasfilename  # Import specific functions from tkinter.filedialog

# Function to open a file for editing
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])  # Open a file dialog to select a file
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)  # Clear the text widget
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()  # Read the contents of the file
        txt_edit.insert(tk.END, text)  # Insert the text into the text widget
    window.title(f"Simple Text Editor - {filepath}")  # Update the window title with the file path

# Function to save the current file as a new file
def save_file():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])  # Open a file dialog to specify a save location
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)  # Get the text from the text widget
        output_file.write(text)  # Write the text to the specified file
    window.title(f"Simple Text Editor - {filepath}")  # Update the window title with the file path

# Function to fix the text by capitalizing characters after a period and two spaces
def fix_text():
    text = txt_edit.get("1.0", tk.END)  # Get the text from the text widget
    new_text = ""
    for i in range(len(text)):
        if text[i-2:i+1] == ".  ":  # Check if the characters match the pattern ".  "
            new_text += text[i].upper()  # Capitalize the character after the period and two spaces
        else:
            new_text += text[i]
    txt_edit.delete("1.0", tk.END)  # Clear the text widget
    txt_edit.insert(tk.END, new_text)  # Insert the modified text into the text widget

# Create the main window
window = tk.Tk()
window.title("Simple text editor")  # Set the window title

# Configure the layout of the window
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Create the text editing widget and buttons
txt_edit = tk.Text(window)  # Text widget for editing text
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)  # Frame to hold the buttons
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)  # Open button
btn_save = tk.Button(frm_buttons, text="Save as...", command=save_file)  # Save button
btn_fix = tk.Button(frm_buttons, text="Fix", command=fix_text)  # Fix button

# Arrange buttons in the frame
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_fix.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

# Add the frame and text widget to the window
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Start the main event loop
window.mainloop()
