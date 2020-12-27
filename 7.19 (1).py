from tkinter import *
min = sec = centisec = 0

def increase_time():
    global min, sec, centisec
    label.after(10, increase_time)
    centisec += 1
    sec += (centisec // 100)
    centisec %= 100
    min += (sec // 60)
    sec %= 60
    display = '{0:02d}:{1:02d}:{2:02d}'.format(min, sec, centisec)
    label.config(text=display)

window = Tk()
window.title('timer')

label = Label(window, text ='00:00:00', fg = 'black', font = 'Arial 120 bold')
label.pack()

button = Button(window, text = 'start', command = increase_time)
button.pack()

window.mainloop()