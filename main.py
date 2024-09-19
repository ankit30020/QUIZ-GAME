from tkinter import *

question = {
    "1: Aryabhatta invented the number?                     [2 points]":
      ['0', '3', '5', '9'],
    "2: How many days are there in a week?                  [2 points]":
      ['6', '7', '8','9'],
    "3: 3561+9389                                           [2 points]":
      ['12960', '12678', '12243', '12950'],
    "4: How many hours are there in a day?                  [2 points]":
      ['24hr', '23hr', '25hr', '21hr'],
    "5: Name the national flower of India?                  [2 points]":
      ['Lotus', 'Lily', 'Hibiscus', 'Rose'],
    "6: Which gas do plants absorb during photosynthesis?   [2 points]":
      ['Carbon Dioxide', 'Nitrogen', 'Oxygen', 'None'],
    "7: Who is the Father of our Nation?                    [2 points]":
      ['Mahatma Gandhi', 'Dr. Rajendra Prasad', 'Dr. B. R. Ambedkar', 'Jawaharlal Nehru']
}


ans = ['0', '7', '12950', '24hr', 'Lotus', 'Carbon Dioxide', 'Mahatma Gandhi']

current_question = 0

def start_quiz():
    start_button.forget()
    next_button.pack()
    next_question()

def next_question():
    global current_question

    if current_question < len(question):
        if current_question > 0:
            check_ans()

        user_ans.set('None')
        c_question = list(question.keys())[current_question]

        
        clear_frame()

        
        Label(f1, text=f"Question  {c_question}", padx=15,
              font="calibre 12 normal").pack(anchor=NW)

        
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option, padx=28).pack(anchor=NW)
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        score = user_score.get()
        output = f"Your Score is {score} out of {len(question) * 2}"

        if score >= 10:
            output += "\nYou win the game!"
        else:
            output += "\nYou lose the game."

        Label(f1, text=output, font="calibre 25 bold").pack()

        Label(f1, text="Thanks for Participating",
              font="calibre 18 bold").pack()

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None':
        if temp_ans == ans[current_question - 1]:
            user_score.set(user_score.get() + 2)
        else:
            user_score.set(user_score.get() - 1)
    else:
        user_score.set(user_score.get() - 1)

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

if __name__ == "__main__":
    root = Tk()

    
    root.title("MY QUIZ APPLICATION")
    root.geometry("949x530")
    root.minsize(711, 398)

    user_ans = StringVar()
    user_ans.set('none')
    user_score = IntVar()
    user_score.set(0)

    Label(root, text="Quiz Game",
          font="calibre 40 bold",
          relief=SUNKEN, background="gold",
          padx=10, pady=9).pack()

    Label(root, text="", font="calibre 10 ").pack()

    game_info_label = Label(root, text="       SOME INFORMATION AND RULES ABOUT THE GAME ARE GIVEN BELOW:\n"
    "1. ALL questions are Multiple Choice.                                        \n"
    "2. There are 7 questions in total. [Score: 7 x 2 = 14]                   \n"
    "3. Right answer: 2 points / Wrong answer : -1 from the points.   \n"
    "4. Passing mark 11 or above 11/ less than 11 Fail.                      \n"
    "5. Each question carries 2 points.                                               \n"
    "6. Answering all the questions correctly to win the game.        \n",

                            font="calibre 10 bold")
    game_info_label.pack()

    start_button = Button(root,
                          text="Start Quiz",
                          command=start_quiz,
                          font="calibre 17 bold")
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Next Question",
                         command=next_question,
                         font="calibre 17 bold")

    root.mainloop()
