from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    Timer.config(text="Timer", fg=PINK)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec  = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN * 60

    # if 1,3,5,7
    if reps==1 or reps==3 or reps==5 or reps==7:
        Timer.config(text="Working", fg=PINK)
        count_down(work_sec)

    #if 8 reps
    elif reps == 8:
        Timer.config(text="Long Break",  fg=RED)
        count_down(long_break_sec)

    #if 2,4,6
    elif reps == 2 or reps==4 or reps ==6: 
        Timer.config(text="Short Break", fg=GREEN)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

Timer = Label(text="Timer", font=(FONT_NAME,"50"), bg=YELLOW, fg=GREEN)
Timer.grid(column=1,row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightbackground=YELLOW)
img = PhotoImage(file = "tomato.png")
canvas.create_image(102,112,image=img)
timer_text = canvas.create_text(102,130,text="00:00",fill="white",font=("FONT_NAME",35,"bold"))
canvas.grid(column=1, row=1)


start = Button(text="Start", font=(FONT_NAME,"10"),highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)


Seen = Label(text="✔", font=(FONT_NAME,"10", "bold"), bg=YELLOW, fg=GREEN)
Seen.grid(column=1,row=3)

reset = Button(text="Reset",  font=(FONT_NAME,"10"),highlightthickness=0, command=reset)
reset.grid(column=2, row=2)



window.mainloop()