import customtkinter as ctk
from tkinter import messagebox


class TodoApp():
    def __init__(self):
        # Initialize the main window
        self.root = ctk.CTk()
        self.root.title("Todo App")
        self.root.geometry("1080x720")


        # Set the appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Store our todo items - each item is aa dictionary with text and frame reference
        self.todo_items = []

        # Create the main interface
        self.create_widgets()


    def create_widgets(self):
        # Create a label for the title of the todo app
        title_label = ctk.CTkLabel(
        self.root,
        text="My Todo List",
        font=ctk.CTkFont("Linux Biolinum G", size=25, weight="bold")
        )
        title_label.pack(pady=20)

        # Input frame for adding new todos
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(pady=10, padx=20, fill="x")

        # Entry widget for new todo text
        self.todo_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter a new todo...",
            font=ctk.CTkFont(size=15)
        )
        self.todo_entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)


        # Add button
        add_button = ctk.CTkButton(
            input_frame,
            text="Add Todo",
            command=self.add_todo,
            width=100
        )
        add_button.pack(side="right", padx=(5, 10), pady=10)

        # Scrollable rame for todo items
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.root,
            label_text="Todo Items"
        )
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Bind Enter key to add todo
        self.todo_entry.bind("<Return>", lambda event: self.add_todo())


    def add_todo(self):
        """Add a new todo items to the list"""
        todo_text = self.todo_entry.get().strip()

        # Validadte input - don't add empty todos
        todo_text = self.todo_entry.get().strip()

        # Validate input - don't add empty todos
        if not todo_text:
            messagebox.showwarning("Empty Todo, Please enter some text for your todo!")
            return
        
        # Create a frame for this specific todo item
        todo_frame = ctk.CTkFrame(self.scrollable_frame)
        todo_frame.pack(fill="x", padx=10, pady=5)

        # Create the todo text label
        todo_label = ctk.CTkLabel(
            todo_frame,
            text=todo_text,
            font=ctk.CTkFont(size=14),
            anchor="w" # Align text to the left
        )
        todo_label.pack(side="left", fill="x", expand=True, padx=(15, 10), pady=10)

        # Create the delete button for this speficic todo
        # This is the key part - we use lambda to capture the current todo_frame
        delete_button = ctk.CTkButton(
            todo_frame,
            text="Delete",
            command=lambda frame=todo_frame: self.delete_todo(frame),
            width=80,
            height=30,
            fg_color="red",
            hover_color="darkred"
        )
        delete_button.pack(side="right", padx=(10, 15), pady=10)

        # Store the todo item information
        todo_item = {
            'text': todo_text,
            'frame': todo_frame,
            'label': todo_label,
            'delete_button': delete_button
        }
        self.todo_items.append(todo_item)

        # Clear the entry field for the next todo
        self.todo_entry.delete(0, 'end')

        # Optional: Show confirmation
        print(f"Added todo: {todo_text}")


    def delete_todo(self, todo_frame):
        """Delete a specific todo item"""
        # Ask for confirmation before deleting
        result = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this todo? "
        )
        if result:
            # Find the todo item in our list
            todo_to_remove = None
            for todo_item in self.todo_items:
                if todo_item['frame'] == todo_frame:
                    todo_to_remove = todo_item
                    break

            if todo_to_remove:
                # Remove the visual frame from the interface
                todo_frame.destroy()

                # Remove the item from our data structure
                self.todo_items.remove(todo_to_remove)

                # Optional: Show confirmation
                print(f"Deleted todo: {todo_to_remove['text']}")
            else:
                # This shouldn't happen, but good to handle just in case
                print("Error: Todo item not found in list")

    
    def get_all_todos(self):
        """"Helper method to get all current todo texts"""
        return [item['text'] for item in self.todo_items]
    

    def clear_all_todos(self):
        """Method to clear all todos"""
        if not self.todo_items:
            messagebox.showinfo("No Todos", "There are no todos to clear!")
            return
        
        result = messagebox.askyesno(
            "Clear All",
            f"Are you sure you want to delete all {len(self.todo_items)} todos?"
        )

        if result:
            for todo_item in self.todo_items:
                todo_item['frame'].destroy()

            self.todo_items.clear()
            print("All todos cleared!")


    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()