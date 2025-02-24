from tkinter import Tk, Label
import time

class Clock:
    def __init__(self, master):
        self.master = master
        master.title("Clock")

        self.time_label = Label(master, font=("Helvetica", 28), fg="green", bg="black")
        self.time_label.pack(fill='both', expand=True)

        self.date_label = Label(master, font=("Helvetica", 10), fg="green", bg="black")
        self.date_label.pack(fill='both', expand=True)

        self.update_time()

        # Bind mouse events for dragging
        self.master.bind("<Button-1>", self.start_move)
        self.master.bind("<B1-Motion>", self.do_move)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.master.after(1000, self.update_time)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.master.winfo_pointerx() - self.x
        y = self.master.winfo_pointery() - self.y
        self.master.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = Tk()
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    clock = Clock(root)
    root.mainloop()