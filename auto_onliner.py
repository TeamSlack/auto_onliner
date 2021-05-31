import pyautogui as pag
import tkinter as tk

def auto_move():
    timer = radVal.get()*1000
    pag.press('a')    
    app.after(timer,auto_move)
    
def stop(app):
    #gets all running 'after' schedules
    ongoing_sched = app.tk.call('after','info')
    #cancel ongoing 'after' schedule
    if ongoing_sched != "":
        app.after_cancel(ongoing_sched)

def on_closing(app):
    #gets all running 'after' schedules
    ongoing_sched = app.tk.call('after','info')
    #cancel ongoing 'after' schedule
    if ongoing_sched != "":
        app.after_cancel(ongoing_sched)
    app.quit()
    app.destroy()
    
def quit(event):
    #gets all running 'after' schedules
    ongoing_sched = app.tk.call('after','info')
    #cancel ongoing 'after' schedule
    if ongoing_sched != "":
        app.after_cancel(ongoing_sched)
    app.quit()

app = tk.Tk()
app.title('Auto-onliner')
app.resizable(0,0)

radVal = tk.IntVar()
radVal.set(1)

instlbl = tk.Label(app, text='Instruction: \nPress \'STOP~\' button to stop\nNote: Default speed is 1s',justify='left')
instlbl.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)

settingFrme = tk.LabelFrame(app, text='Set timer')
settingFrme.grid(row=1, rowspan=3, column=0, padx=10, pady=2)

onesec_rad = tk.Radiobutton(settingFrme, text='1 second', width = 10, height=1, variable=radVal, value=1)
onesec_rad.grid(row=0, column=0, padx=10,pady=2)

fivesec_rad = tk.Radiobutton(settingFrme, text='5 second', width = 10, height=1, variable=radVal, value=5)
fivesec_rad.grid(row=1, column=0, padx=10,pady=2)

tensec_rad = tk.Radiobutton(settingFrme, text='10 second', width = 10, height=1, variable=radVal, value=10)
tensec_rad.grid(row=2, column=0, padx=10,pady=2)

startButton = tk.Button(app, text='Start!', width=10, height=2, command=auto_move)
startButton.grid(row=1, column=1, padx=20, pady=2, sticky=tk.S)

stopButton = tk.Button(app, text='Stop~', width=10, height=2, command=lambda: stop(app))
stopButton.grid(row=2, column=1, padx=20, pady=2, sticky=tk.S)

app.bind('<Control-c>',quit)

app.protocol('WM_DELETE_WINDOW',lambda: on_closing(app))

app.mainloop()
