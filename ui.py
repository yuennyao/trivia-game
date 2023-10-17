from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"


class QuizInterface:
    #pass in quiz_brain object with a data type QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #self. turns it into a property which can be accessed anywhere in the class
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.check_marks = Label(text="Score=0", fg=WHITE, bg=THEME_COLOR)
        self.check_marks.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.ques_text = self.canvas.create_text(150, 125, width=280, text="quest", fill=THEME_COLOR, font=("arial", 12, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_photo = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_photo, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_photo = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_photo, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        #Anything after this line will not be executed in the interface
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.check_marks.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)






