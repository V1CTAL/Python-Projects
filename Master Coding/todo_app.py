import customtkinter as ctk
from tkinter import messagebox


# --- Core Functions ---

def add_todo():
    """Adds a new todo item to the scrollable frame."""
    todo_text = todo_entry.get().strip()

    if not todo_text:
        messagebox.showwarning("Warning", "Please enter some text for your todo!")
        return
    
    # Create a frame for this specific todo item
    todo_frame = ctk.CTkFrame(scrollable_frame)
    todo_frame.pack(fill="x", padx=10, pady=5)

    # Create the todo text label
    todo_label = ctk.CTkLabel(
        todo_frame,
        text=todo_text,
        font=ctk.CTkFont("Euphemia", size=14),
        anchor="w"
    )
    todo_label.pack(side="left", fill="x", expand=True, padx=(15, 10), pady=10)

    # Create the delete button, passing the frame directly to the delete function
    delete_button = ctk.CTkButton(
        todo_frame,
        text="Delete",
        command=lambda frame=todo_frame: delete_todo(frame), # Simplified command
        width=80,
        height=30,
        fg_color="red",
        hover_color="darkred"
    )
    delete_button.pack(side="right", padx=(10, 15), pady=10)

    # Clear the entry field
    todo_entry.delete(0, 'end')


def delete_todo(frame_to_delete):
    """Deletes a specific todo frame after confirmation"""
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete todo?"):
        frame_to_delete.destroy()
    

def clear_all_todos():
    """Clears all todo items from the scrollable frame."""
    # Get all child widgets (the todo_frame) in the scrollable frame
    all_todo_frames = scrollable_frame.winfo_children()

    if not all_todo_frames:
        messagebox.showinfo("No Todos", "There are no todos to clear!")
        return
    
    if messagebox.askyesno("Clear All", f"Are you sure you want to delete all {len(all_todo_frames)} todos?"):
        for frame in all_todo_frames:
            frame.destroy()

    
# --- Main Application the main window

# 1. Initialize the main window
root = ctk.CTk()
root.title("Simple Todo App")
root.geometry("1080x720")

# 2. Set Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# 3. Create the main widgets
title_label = ctk.CTkLabel(root, text="My Todo List", font=ctk.CTkFont("Euphemia", size=25, weight="bold"))
title_label.pack(pady=20)

input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=20, fill="x")

todo_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter a new todo...", font=ctk.CTkFont(size=15))
todo_entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

add_button = ctk.CTkButton(input_frame, text="Add Todo", command=add_todo, width=100)
add_button.pack(side="right", padx=(5, 10), pady=10)

clear_button = ctk.CTkButton(input_frame, text="Clear All", command=clear_all_todos, width=100)
clear_button.pack(side="right", padx=(5, 10), pady=10)

scrollable_frame = ctk.CTkScrollableFrame(root, label_text="Todo Items")
scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

# 4. Bind the ENter key
todo_entry.bind("<Return>", lambda event: add_todo())

# 5. Start the application
root.mainloop()
