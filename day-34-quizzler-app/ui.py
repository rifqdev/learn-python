from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="hello world", fill="black", font=("Arial", 20, "italic"), width=200)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false_button)
        self.false_btn.grid(row=2, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true_button)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(self.canvas, bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else: 
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions")
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")

    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(self.canvas, bg="green")
        else:
            self.canvas.config(self.canvas, bg="red")
        self.window.after(1000, func=self.get_next_question)
        