import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from itertools import cycle
import pyfiles.backend2 as be
import pyfiles.coursesection as cs

class EntryWithPlaceholder(tk.Entry):
    
    def __init__(self,  master=None,  placeholder="",  *args,   **kwargs):
    
        super().__init__(master, *args, **kwargs)
    
        self.placeholder = placeholder
        self.placeholder_color =  "grey"
        self.default_fg_color =  self["fg"]
        self.user =  []
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self.put_placeholder()

   
    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

   
    def _on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

    
    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)


class LoginApp:
    def __init__(self, root, bg_image_path, form_image_path):
        self.root = root
        self.root.title("FutureNse Login")
        self.root.geometry("1366x768")  # Full screen size

        # Create main frames for layout
        self.left_frame = tk.Frame(root, width=683, height=768)  # Half width for left frame
        self.left_frame.pack(side='left', fill='both', expand=True)
        self.right_frame = tk.Frame(root, width=683, height=768, bg='white')  # Half width for right frame
        self.right_frame.pack(side='right', fill='both', expand=True)

        # Load and display background image
        self.bg_image = self.load_image(bg_image_path, (683, 768))

        self.canvas = tk.Canvas(self.left_frame, width=683, height=768)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')

        # Load and display form image
        self.form_image = self.load_image(form_image_path, (409, 146))

        # Create login form in the right frame
        self.create_login_form()

        # Bind close event of the main window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        print("Protocol for WM_DELETE_WINDOW is set")
        
    def load_image(self, path, size):
        if os.path.exists(path):
            image = Image.open(path)
            image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        else:
            print(f"Image not found: {path}")
            return None

    def create_login_form(self):
        form_frame = tk.Frame(self.right_frame, bg='white', padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Add form image
        image_label = tk.Label(form_frame, image=self.form_image, bg='white')
        image_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username field
        username_label = tk.Label(form_frame, text="Username", font=("Helvetica", 12), bg='white')
        username_label.grid(row=1, column=0, sticky='w', pady=(20, 5))

        username_frame = tk.Frame(form_frame, bg='white')
        username_frame.grid(row=2, column=0, sticky='w')

        # Username entry
        self.username_entry = EntryWithPlaceholder(username_frame, placeholder="Username", width=30, font=("Helvetica", 12), bd=1)
        self.username_entry.grid(row=0, column=0, sticky="ew")

        # Password field
        password_label = tk.Label(form_frame, text="Password", font=("Helvetica", 12), bg='white')
        password_label.grid(row=3, column=0, sticky='w', pady=(20, 5))

        password_frame = tk.Frame(form_frame, bg='white')
        password_frame.grid(row=4, column=0, sticky='w')

        # Password entry
        self.password_entry = EntryWithPlaceholder(password_frame, placeholder="Password", width=30, font=("Helvetica", 12), show="*", bd=1)
        self.password_entry.grid(row=0, column=0, sticky="ew")
        # Login button
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="black", foreground="black")
        login_button = ttk.Button(form_frame, text="Log in", style="TButton", command=self.check_credentials)
        login_button.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)  # Increase button width

        # Forgotten username or password
        forgotten_label = tk.Label(form_frame, text="Forgotten your username or password?", font=("Helvetica", 10), fg="blue", bg='white')
        forgotten_label.grid(row=7, column=0, columnspan=2, pady=5, sticky='w')

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        l = be.login(username)
        self.user = list(l)
        if l:
            if password == l[2]:
                messagebox.showinfo("Success", "Login Successful!")
                self.show_loading_page()
            else:
                messagebox.showerror("Error", "Invalid password.")
        else:
            messagebox.showerror("Error", "Invalid username.")

    def show_loading_page(self):
        # Destroy the main window
        self.root.destroy()

        # Create a new window for the loading page
        loading_window = tk.Tk()
        loading_window.title("Loading")
        loading_window.geometry("1366x768")
        loading_window.configure(bg='white')

        # Display loading animation
        loading_frame = tk.Frame(loading_window, bg='white')
        loading_frame.place(relx=0.5, rely=0.5, anchor='center')

        loading_label = tk.Label(loading_frame, text="Logging in...", font=("Helvetica", 16), bg='white')
        loading_label.pack(pady=20)

        # Infinity symbol animation
        spinner = cycle(['|', '/', '-', '\\'])
        spinner_label = tk.Label(loading_frame, text="", font=("Helvetica", 24), bg='white')
        spinner_label.pack()

        def animate():
            spinner_label.config(text=next(spinner))
            loading_window.after(50, animate)

        animate()

        # Warning message
        warning_label = tk.Label(loading_frame, text="Please do not close the window until we redirect to your new window", font=("Helvetica", 12), fg='grey', bg='white')
        warning_label.pack(pady=20)

        # Show the loading page for 3 seconds before transitioning to the dashboard
        loading_window.after(2500, lambda: self.show_dashboard(loading_window))

    def show_dashboard(self, loading_window):
        loading_window.destroy()

        #getting student info
        information = be.info(self.user[1])
        # Create a new window for the dashboard
        dashboard_window = tk.Tk()
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("1366x768")
        dashboard_window.configure(bg='#F7F9F2')

        # Create top frame for user info and navigation
        top_frame = tk.Frame(dashboard_window, bg='#F5F5F5', height=100)
        top_frame.pack(fill='x')

        # Random text on left side of navigation bar
        random_text_label = tk.Label(top_frame, text="Welcome to Futurense!", font=("Helvetica", 16), bg='#F5F5F5')
        random_text_label.pack(side='left', padx=20)

        # User profile image placeholder
        user_image_path = r""  # Replace with actual path
        user_image = self.load_image(user_image_path, (50, 50))
        user_image_label = tk.Label(top_frame, image=user_image, bg='#F5F5F5')
        user_image_label.image = user_image  # Keep a reference
        user_image_label.pack(side='right', padx=20)
        
        bell_icon = tk.Label(top_frame, text="🔔", font=("Arial", 24), cursor="hand2", bg='#F5F5F5')
        bell_icon.pack(side='right', padx=20)
        bell_icon.bind("<Button-1>", lambda e: self.notifications())

        # User name label
        user_name_label = tk.Label(top_frame, text=information[1], font=("Helvetica", 16), bg='#F5F5F5')
        user_name_label.pack(side='right')

        # Dashboard content frame
        content_frame = tk.Frame(dashboard_window, bg='white')
        content_frame.pack(fill='both', expand=True)

        # Left portion for courses section
        left_courses_frame = tk.Frame(content_frame, bg='white', width=683, padx=20, pady=20)
        left_courses_frame.pack(side='left', fill='both', expand=True)

        courses = be.coursenroll(self.user[1])
        i = 0
        while True:
            
            for j in range(2):
                course_frame = tk.Frame(left_courses_frame, bg='white', bd=1, relief='solid', width=500, height=500)
                course_frame.grid(row=i, column=j, padx=75, pady=50, sticky="nsew")

                cd = be.coursedetail(courses.pop())
                print(courses)
                

                course_image_path = fr"{cd[3]}"
                course_cover_image = self.load_image(course_image_path, (300, 150))
                if course_cover_image:
                    course_cover_label = tk.Label(course_frame, image=course_cover_image, bg='white')
                    course_cover_label.image = course_cover_image  # Keep a reference
                    course_cover_label.pack(pady=(0, 5))
                
                # Course title label
                course_title_label = tk.Label(course_frame, text=f"{cd[1]}", font=("Helvetica", 12), bg='white')
                course_title_label.pack()

                # Get started button
                get_started_button = tk.Button(course_frame, text="Get started", command=lambda cd=cd: cs.create_dashboard(information[1],cd[1]))
                get_started_button.pack(pady=(5, 0))
                if len(courses) == 0:
                    break
            i += 1
            if len(courses) == 0:
                break

        # Right portion for profile information, events, and navigation
        right_profile_frame = tk.Frame(content_frame, bg='grey', width=250)
        right_profile_frame.pack(side='right', fill='y')

        # Profile information section
        profile_frame = tk.Frame(right_profile_frame, bg='grey', bd=1, relief='solid')
        profile_frame.pack(padx=10, pady=10, fill='both', expand=True)

        profile_label = tk.Label(profile_frame, text="Profile Information", font=("Helvetica", 12), bg='grey', fg='white')
        profile_label.pack(pady=10)

        profile_info = {
            "Name": information[1],
            "Semester": information[4],
            "Year": information[3],
            "Course": information[2],
            "Roll No.": information[5],
            "Registration Number": information[7]
        }

        for key, value in profile_info.items():
            info_label = tk.Label(profile_frame, text=f"{key}: {value}", font=("Helvetica", 10), bg='grey', fg='white')
            info_label.pack(anchor='w', padx=10, pady=5)

        # Upcoming events section
        events_frame = tk.Frame(right_profile_frame, bg='grey', bd=1, relief='solid')
        events_frame.pack(padx=10, pady=10, fill='both', expand=True)

        events_label = tk.Label(events_frame, text="Upcoming events", font=("Helvetica", 12), bg='grey', fg='white')
        events_label.pack()

        # Placeholder for events content
        events_content = tk.Label(events_frame, text="No upcoming events", font=("Helvetica", 10), bg='grey', fg='white')
        events_content.pack(pady=10)

        # Navigation buttons
        buttons_frame = tk.Frame(right_profile_frame, bg='grey')
        buttons_frame.pack(pady=20, fill='both', expand=True)

        logout_button = ttk.Button(buttons_frame, text="Logout", style="TButton", command=lambda: self.back_to_login(dashboard_window))
        logout_button.pack(pady=10)

        back_to_login_button = ttk.Button(buttons_frame, text="Back to Login Page", style="TButton", command=lambda: self.back_to_login(dashboard_window))
        back_to_login_button.pack(pady=10)

        grade_button = ttk.Button(buttons_frame, text="Grade", style="TButton", command=self.grades)
        grade_button.pack(pady=10)

    def notifications(self):
        self.notification_popup = tk.Toplevel()
        self.notification_popup.title("Notifications")
        self.notification_popup.geometry("500x350")
        self.notification_popup.configure(bg='white')

        # Create a canvas widget
        canvas = tk.Canvas(self.notification_popup)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add a vertical scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.notification_popup, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas
        frame = tk.Frame(canvas)
        
        # Add the new frame to a window in the canvas
        canvas.create_window((0, 0), window=frame, anchor="nw")
        print(self.user[1])
        mess = be.get_message(self.user[1])
        if mess == []:
            notification_label = tk.Label(canvas, text="You have no notifications!", bg='white')
            notification_label.pack(pady=20)
        for i in mess:
            self.add_notification(frame, f"Teacher ID: {i[2]}",f"Student ID: {i[1]}", f"{i[3]}", f"Message ID: {i[0]}")
            print("message" )

    def add_notification(self, parent, teacher_id, student_id, message, message_id):
        # Notification Frame
        notification_frame = tk.Frame(parent, bg='lightgrey', bd=2, relief=tk.SOLID)
        notification_frame.pack(padx=10, pady=10, fill=tk.X)
        
        # Top Frame for IDs
        top_frame = tk.Frame(notification_frame, bg='lightgrey')
        top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Labels for Teacher ID and Student ID
        teacher_id_label = tk.Label(top_frame, text=teacher_id, bg='lightgrey', anchor='w')
        teacher_id_label.pack(side=tk.LEFT)
        
        student_id_label = tk.Label(top_frame, text=student_id, bg='lightgrey', anchor='w')
        student_id_label.pack(side=tk.LEFT, padx=(10, 0))

        message_id_label = tk.Label(top_frame, text=message_id, bg='lightgrey', anchor='w')
        message_id_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Message Label
        message_label = tk.Label(notification_frame, text=message, bg='lightgrey', anchor='w', justify=tk.LEFT, wraplength=280)
        message_label.pack(padx=5, pady=10)
    
    def grades(self):
        gwin= tk.Toplevel()
        gwin.title('Grade Page')
        gwin.geometry('500x400')

        headers = ['Course Name', 'Grade']
        for i, header in enumerate(headers):
            header_label = tk.Label(gwin, text=header, font=('Helvetica', 12, 'bold'))
            header_label.grid(row=0, column=i, padx=10, pady=10)

        g = be.fetch_grades(self.user[1])
        grades = []
        for i in g:
            print(i)
            grade = i[3]
            n = be.coursedetail(i[2])
            print(n)
            name = n[1]
            grades.append((name, grade))
        
        # Populate table with grades
        for row_idx, grade in enumerate(grades, start=1):
            course_name_label = tk.Label(gwin, text=grade[0], font=('Helvetica', 12))
            course_name_label.grid(row=row_idx, column=0, padx=10, pady=5)
        
            grade_label = tk.Label(gwin, text=grade[1], font=('Helvetica', 12))
            grade_label.grid(row=row_idx, column=1, padx=10, pady=5)
    
    def on_closing(self):
        # Called when the main window is closing
        print("Closing main window...")
        try:
            if self.notification_popup is not None and self.notification_popup.winfo_exists():
                print("Destroying new window...")
                self.notification_popup.destroy()
        except:
            self.root.destroy()
    
    def back_to_login(self, current_window):
        current_window.destroy()
        root = tk.Tk()
        app = LoginApp(root, bg_image_path, form_image_path)
        root.mainloop()


if __name__ == "__main__":
    # Provide the correct paths to your images
    bg_image_path = r"images/main.png"  # Correct the file path
    form_image_path = r"images/c6.jpeg"  # Provide the correct path to the form image

    root = tk.Tk()
    app = LoginApp(root, bg_image_path, form_image_path)
    root.mainloop()