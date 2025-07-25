import tkinter as tk
from tkinter import messagebox

class OnlineExam:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Exam Portal")

        # Sample questions: List of dicts
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "Which language is used for web apps?",
                "options": ["Python", "JavaScript", "C++", "Java"],
                "answer": "JavaScript"
            },
            {
                "question": "What does CPU stand for?",
                "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"],
                "answer": "Central Processing Unit"
            }
        ]

        self.q_index = 0
        self.selected_answer = tk.StringVar()
        self.user_answers = [None] * len(self.questions)

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.lbl_question = tk.Label(self.root, text="", wraplength=400, font=("Arial", 14))
        self.lbl_question.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_answer, value="", font=("Arial", 12))
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.btn_prev = tk.Button(btn_frame, text="Previous", command=self.prev_question)
        self.btn_prev.grid(row=0, column=0, padx=10)

        self.btn_next = tk.Button(btn_frame, text="Next", command=self.next_question)
        self.btn_next.grid(row=0, column=1, padx=10)

        self.btn_submit = tk.Button(self.root, text="Submit Exam", command=self.submit_exam)
        self.btn_submit.pack(pady=10)

    def load_question(self):
        q = self.questions[self.q_index]
        self.lbl_question.config(text=f"Q{self.q_index+1}: {q['question']}")

        self.selected_answer.set(self.user_answers[self.q_index] if self.user_answers[self.q_index] else "")

        for i, option in enumerate(q['options']):
            self.radio_buttons[i].config(text=option, value=option)

        self.btn_prev.config(state=tk.NORMAL if self.q_index > 0 else tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL if self.q_index < len(self.questions)-1 else tk.DISABLED)

    def save_answer(self):
        self.user_answers[self.q_index] = self.selected_answer.get()

    def next_question(self):
        self.save_answer()
        if self.q_index < len(self.questions) - 1:
            self.q_index += 1
            self.load_question()

    def prev_question(self):
        self.save_answer()
        if self.q_index >_
