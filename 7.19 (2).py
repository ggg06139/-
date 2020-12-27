from tkinter import *

time_count = 0
b_working = False
min = sec = centisec = 0

def increase_time():
    global min, sec, centisec
    if b_working == True:
        label.after(10,increase_time)
        centisec += 1
        sec += (centisec // 100)
        centisec %= 100
        min += (sec // 60)
        sec %= 60
        display = '{0:02d}:{1:02d}:{2:02d}'.format(min,sec,centisec)
        label.config(text=display)
    else:
        display = '{0:02d}:{1:02d}:{2:02d}'.format(min,sec,centisec)
        label.config(text=display)
def start_time():
    global b_working
    b_working = True
    increase_time()

def stop_time():
    global b_working
    b_working = False

def reset_time():
    global min, sec, centisec
    min = sec = centisec = 0
    display = '{0:02d}:{1:02d}:{2:02d}'.format(min,sec,centisec)
    label.config(text = display)


window = Tk()
window.title('timer')

label = Label(window, text ='00:00:00', fg = 'black', font = 'Arial 120 bold')
label.pack()

button = Button(window, text = 'start', command = start_time)
button.pack()
button = Button(window, text = 'stop', command = stop_time)
button.pack()
button = Button(window, text = 'reset', command = reset_time)
button.pack()

window.mainloop()