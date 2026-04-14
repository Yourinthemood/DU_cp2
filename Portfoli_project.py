import tkinter as tk
import subprocess
import os
 

# Personal Portfolio - Main Application

 
class Portfolio:
    """Main portfolio window that displays all projects."""
 
    def __init__(self, root):
        """Set up the main window and all widgets."""
        self.root = root
        self.root.title("My Programming Portfolio")
        self.root.geometry("600x500")
 
        # Title Label
        title_label = tk.Label(root, text="My Programming Portfolio", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
 
        #Introduction Section
        intro_text = (
            "Welcome to my portfolio! Below are 4 projects I am proud of from this class.\n"
            "Click a project button to see its description.\n"
            "Click 'Run Project' to launch it."
        )
        intro_label = tk.Label(root, text=intro_text, justify="center", wraplength=550)
        intro_label.pack(pady=5)
 
        #Project Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
 
        # Project button names
        project_names = [
            "Pet Simulator",
            "Character Manager",
            "High Score Tracker",
            "Combat Game"
        ]
 
        # Create one button per project
        for i, name in enumerate(project_names):
            btn = tk.Button(
                btn_frame,
                text=name,
                width=20,
                command=lambda idx=i: self.show_project_info(idx)
            )
            btn.grid(row=0, column=i, padx=5)
 
        # Info Text Area
        self.info_text = tk.Text(root, height=12, width=70, state="disabled")
        self.info_text.pack(pady=10)
 
        # Run Project Button
        self.run_btn = tk.Button(root, text="Run Project", state="disabled", command=self.run_project)
        self.run_btn.pack(pady=5)
 
        # Track which project is selected
        self.selected_project = None
 
        # Project info and file paths
        self.projects = [
            {
                "name": "Pet Simulator",
                "description": (
                    "What it does:\n"
                    "  A virtual pet simulator where you can feed, play with, and take care of your pet.\n\n"
                    "What I learned:\n"
                    "  - How to use classes and objects to represent a pet's stats\n"
                    "  - How to update and display changing data in a GUI\n\n"
                    "Challenge I overcame:\n"
                    "  - Getting the pet's stats to update correctly after each action without crashing"
                ),
                "path": os.path.join("..", "DU_cp2", "bigcoolcode", "petsimulator", "main.py")
            },
            {
                "name": "Character Manager",
                "description": (
                    "What it does:\n"
                    "  Lets you create, view, and manage RPG-style characters with different stats.\n\n"
                    "What I learned:\n"
                    "  - How to store and retrieve data using dictionaries and lists\n"
                    "  - How to build a GUI that updates based on user input\n\n"
                    "Challenge I overcame:\n"
                    "  - Making sure character data saved and loaded correctly between sessions"
                ),
                "path": os.path.join("..", "DU_cp2", "UPDATED_CHR_MNGR", "main.py")
            },
            {
                "name": "High Score Tracker",
                "description": (
                    "What it does:\n"
                    "  Tracks and displays high scores for a game, saving the top scores.\n\n"
                    "What I learned:\n"
                    "  - How to read and write data to files to save scores\n"
                    "  - How to sort and display a leaderboard\n\n"
                    "Challenge I overcame:\n"
                    "  - Handling file errors when the score file didn't exist yet"
                ),
                "path": os.path.join("..", "DU_CP1", "projects", "ohmygosh.PY")
            },
            {
                "name": "Combat Game",
                "description": (
                    "What it does:\n"
                    "  A turn-based combat game where the player fights enemies using different moves.\n\n"
                    "What I learned:\n"
                    "  - How to use loops and conditionals to control game flow\n"
                    "  - How to design a simple combat system with attack and defense logic\n\n"
                    "Challenge I overcame:\n"
                    "  - Balancing the enemy difficulty so the game was fun but not too easy"
                ),
                "path": os.path.join("..", "DU_CP1", "combat game", "main.py")
            }
        ]
 
    def show_project_info(self, project_index):
        """Display the description for the selected project."""
        self.selected_project = project_index
        project = self.projects[project_index]
 
        # Enable text box, clear it, insert new info, then disable again
        self.info_text.config(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, f"  {project['name']}\n")
        self.info_text.insert(tk.END, "=" * 50 + "\n")
        self.info_text.insert(tk.END, project["description"])
        self.info_text.config(state="disabled")
 
        # Enable the run button now that a project is selected
        self.run_btn.config(state="normal")
 
    def run_project(self):
        """Launch the selected project using subprocess."""
        if self.selected_project is None:
            return
 
        project = self.projects[self.selected_project]
        file_path = project["path"]
 
        # Check if the file exists before trying to run it
        if os.path.exists(file_path):
            subprocess.Popen(["python", file_path])
        else:
            # Show error in the text box if file not found
            self.info_text.config(state="normal")
            self.info_text.delete("1.0", tk.END)
            self.info_text.insert(
                tk.END,
                f"Error: Could not find file at:\n{file_path}\n\n"
                "Please make sure all project folders are in the correct location."
            )
            self.info_text.config(state="disabled")
 
 

# Run the stuff

root = tk.Tk()
app = Portfolio(root)
root.mainloop()
 
