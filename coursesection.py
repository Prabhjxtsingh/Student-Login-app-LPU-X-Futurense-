import tkinter as tk
from tkinter import messagebox
import subprocess

def open_pdf(pdf_file):
    try:
        # Open the PDF file with the default PDF viewer
        subprocess.Popen(["start", pdf_file], shell=True)
    except FileNotFoundError:
        messagebox.showerror("Error", "No default application found to open PDF files.")

def create_dashboard(username, c_name):
    root = tk.Tk()
    root.title("Course Dashboard")
    root.geometry("1200x800")
    
    # Creating the main frame
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Navbar
    navbar = tk.Frame(main_frame, bg="grey", height=50)
    navbar.pack(side=tk.TOP, fill=tk.X)
    
    # Navbar content
    tk.Label(navbar, text=f"{c_name}", bg="grey", fg="white", font=("Helvetica", 16)).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Label(navbar, text=f"{username}", bg="grey", fg="white", font=("Helvetica", 16)).pack(side=tk.RIGHT, padx=10, pady=10)
    
    # Right sidebar for completion progress, announcements, leaderboard (20-30% of the window)
    right_sidebar = tk.Frame(main_frame, bg="white", width=300, bd=1, relief="solid")
    right_sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
    
    # Completion progress
    progress_frame = tk.Frame(right_sidebar, bg="white", bd=1, relief="solid")
    progress_frame.pack(fill=tk.X, padx=10, pady=10)
    
    tk.Label(progress_frame, text="Completion Progress", bg="white", font=("Helvetica", 14)).pack(anchor=tk.W, padx=5, pady=5)
    
    progress = [
        "Completed: Feedback-2",
        "Completed",
        "Completed",
        "Completed",
        "Completed"
    ]
    
    for item in progress:
        tk.Label(progress_frame, text=item, bg="#f0f0f0", fg="green", width=40, anchor="w", padx=5, pady=10).pack(fill=tk.X, pady=2)
    
    # Announcements
    announcement_frame = tk.Frame(right_sidebar, bg="white", bd=1, relief="solid")
    announcement_frame.pack(fill=tk.X, padx=10, pady=10)
    
    tk.Label(announcement_frame, text="Announcements", bg="white", font=("Helvetica", 14)).pack(anchor=tk.W, padx=5, pady=5)
    tk.Label(announcement_frame, text="Welcome to the Course!", bg="#f0f0f0", width=40, anchor="w", padx=5, pady=10).pack(fill=tk.X, pady=2)
    
    # Leaderboard
    leaderboard_frame = tk.Frame(right_sidebar, bg="white", bd=1, relief="solid")
    leaderboard_frame.pack(fill=tk.X, padx=10, pady=10)
    
    tk.Label(leaderboard_frame, text="Leader Board", bg="white", font=("Helvetica", 14)).pack(anchor=tk.W, padx=5, pady=5)
    
    leaderboard = [
        ("Bindu Vamsi Guntupalli", 286),
        ("Aditya Matha", 284),
        ("Muskan_", 282),
        ("S. Yaswanth Sai", 282),
        ("Kushagra Keshri", 280),
    ]
    
    for name, score in leaderboard:
        tk.Label(leaderboard_frame, text=f"{name}: {score}", bg="#f0f0f0", width=40, anchor="w", padx=5, pady=10).pack(fill=tk.X, pady=2)
    
    # Left sidebar for course sections (70-80% of the window)
    left_sidebar = tk.Frame(main_frame, bg="white", width=900, bd=1, relief="solid")
    left_sidebar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Define sections with their corresponding PDF files
    sections = [
        {"name": "Course Syllabus", "file": "D:/pdf/1.pdf"},
        {"name": "Zoom Online Sessions", "file": "C:/Users/Dell/Desktop/download2.pdf"},
        {"name": "Learning Space", "file": "C:/Users/Dell/Desktop/download3.pdf"},
        {"name": "Reference Materials", "file": "C:/Users/Dell/Desktop/download4.pdf"},
        {"name": "Lab Work", "file": "C:/Users/Dell/Desktop/download5.pdf"},
        {"name": "Assignments", "file": "C:/Users/Dell/Desktop/download6.pdf"},
        {"name": "Discussion Forum", "file": "C:/Users/Dell/Desktop/download7.pdf"}
    ]
    
    # Create buttons for each section
    for section in sections:
        btn = tk.Button(left_sidebar, text=section["name"], bg="#f0f0f0", bd=0, anchor="w", padx=10, pady=15, font=("Helvetica", 12),
                        command=lambda file=section["file"]: open_pdf(file))
        btn.pack(fill=tk.X, pady=5)

# # Create the main application window

# create_dashboard(root)

# # Start the Tkinter event loop
# root.mainloop()
