import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("500x400")

        # Sample quiz questions: list of dicts
        self.questions = [
            {
                "question": "What is the capital of Italy?",
                "options": ["Rome", "Milan", "Naples", "Florence"],
                "answer": "Rome"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is 5 + 7?",
                "options": ["10", "11", "12", "13"],
                "answer": "12"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
                "answer": "William Shakespeare"
            }
        ]

        self.q_index = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.lbl_question = tk.Label(self.root, text="", font=("Arial", 16), wraplength=450)
        self.lbl_question.pack(pady=30)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_answer, value="", font=("Arial", 14))
            rb.pack(anchor='w', padx=50, pady=5)
            self.radio_buttons.append(rb)

        self.btn_next = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 14))
        self.btn_next.pack(pady=20)

    def load_question(self):
        q = self.questions[self.q_index]
        self.lbl_question.config(text=f"Q{self.q_index + 1}: {q['question']}")
        self.selected_answer.set(None)

        for i, option in enumerate(q['options']):
            self.radio_buttons[i].config(text=option, value=option)

    def next_question(self):
        selected = self.selected_answer.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an answer before proceeding.")
            return

        # Check answer
        if selected == self.questions[self.q_index]['answer']:
            self.score += 1

        self.q_index += 1
        if self.q_index == len(self.questions):
            messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {len(self.questions)}")
            self.root.destroy()
        else:
            self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
