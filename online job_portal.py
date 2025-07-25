import tkinter as tk
from tkinter import messagebox, simpledialog

class JobPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Job Portal")

        # Sample job data: list of dicts
        self.jobs = [
            {"title": "Software Engineer", "company": "TechCorp", "location": "New York"},
            {"title": "Data Analyst", "company": "DataCo", "location": "San Francisco"},
            {"title": "Web Developer", "company": "WebWorks", "location": "Remote"},
        ]

        self.filtered_jobs = self.jobs.copy()

        self.create_widgets()
        self.load_jobs()

    def create_widgets(self):
        # Search box
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10, fill='x')

        tk.Label(search_frame, text="Search jobs:").pack(side='left', padx=5)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side='left', fill='x', expand=True)
        self.search_entry.bind('<KeyRelease>', self.search_jobs)

        # Job list
        self.listbox = tk.Listbox(self.root, width=60, height=15)
        self.listbox.pack(pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.show_job_details)

        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.btn_add_job = tk.Button(btn_frame, text="Add Job", command=self.add_job)
        self.btn_add_job.grid(row=0, column=0, padx=10)

        self.btn_apply = tk.Button(btn_frame, text="Apply for Job", command=self.apply_job)
        self.btn_apply.grid(row=0, column=1, padx=10)

        # Job details display
        self.details_text = tk.Text(self.root, height=6, width=60)
        self.details_text.pack(pady=10)
        self.details_text.config(state='disabled')

    def load_jobs(self):
        self.listbox.delete(0, tk.END)
        for job in self.filtered_jobs:
            self.listbox.insert(tk.END, f"{job['title']} at {job['company']}")

    def search_jobs(self, event=None):
        query = self.search_var.get().lower()
        self.filtered_jobs = [job for job in self.jobs if query in job['title'].lower() or query in job['company'].lower()]
        self.load_jobs()
        self.details_text.config(state='normal')
        self.details_text.delete('1.0', tk.END)
        self.details_text.config(state='disabled')

    def show_job_details(self, event=None):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            job = self.filtered_jobs[index]
            details = f"Job Title: {job['title']}\nCompany: {job['company']}\nLocation: {job['location']}"
            self.details_text.config(state='normal')
            self.details_text.delete('1.0', tk.END)
            self.details_text.insert(tk.END, details)
            self.details_text.config(state='disabled')

    def add_job(self):
        title = simpledialog.askstring("Add Job", "Job Title:")
        if not title:
            return
        company = simpledialog.askstring("Add Job", "Company Name:")
        if not company:
            return
        location = simpledialog.askstring("Add Job", "Location:")
        if not location:
            return

        new_job = {"title": title, "company": company, "location": location}
        self.jobs.append(new_job)
        self.search_jobs()
        messagebox.showinfo("Success", "Job added successfully!")

    def apply_job(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a job to apply for.")
            return

        index = selection[0]
        job = self.filtered_jobs[index]

        name = simpledialog.askstring("Apply for Job", "Your Full Name:")
        if not name:
            return
        email = simpledialog.askstring("Apply for Job", "Your Email:")
        if not email:
            return
        resume = simpledialog.askstring("Apply for Job", "Paste your resume text here:")
        if not resume:
            return

        # In a real app, you'd save this data or send it somewhere
        messagebox.showinfo("Application Submitted",
                            f"Thank you {name} for applying to {job['title']} at {job['company']}.\nWe will contact you at {email}.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x600")
    app = JobPortal(root)
    root.mainloop()
