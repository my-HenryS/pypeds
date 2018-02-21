import tkinter as tk

class Tkinter_UI():
    def __init__(self):
        self.setup()

    def btnStopClicked(label):
        label.config(text="the simulation is stopped")

    def btnRunClicked(label):
        label.config(text="the simulation is running")

    def btnPauseClicked(label):
        label.config(text="the simulation is pause")

    def setup(self):

        self.top = tk.Tk()

        self.top.title("Tkinter_UI")

        self.top.geometry("1000x800")

        self.label = tk.Label(self.top, text="the simulation is stopped", height=5, width=20, fg="blue")

        self.label.pack()

        self.canvas=tk.Canvas(self.top,bg="white",height=500,width=1000)

        self.canvas.pack()

        self.btn1 = tk.Button(self.top, text="Start", command=self.btnRunClicked)

        self.btn1.pack(padx=5,pady=10,ipadx=100,ipady=10)

        self.btn2 = tk.Button(self.top, text="Stop", command=self.btnStopClicked)

        self.btn2.pack(padx=5,pady=10,ipadx=100,ipady=10)

        self.btn3 = tk.Button(self.top, text="Pause", command=self.btnPauseClicked)

        self.btn3.pack(padx=5,pady=10,ipadx=100,ipady=10)
