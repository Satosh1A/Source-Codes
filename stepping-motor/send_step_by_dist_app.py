import serial
import time
import tkinter as tk
from tkinter import ttk
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ステッピングモーターの制御")
        self.geometry("700x600")
        self.create_widgets()
        self.arduino = serial.Serial('COM5', 115200)
        self.distance = ""
        self.microstep_mode = "1"

    def create_widgets(self):
        ttk.Label(self, text='マイクロステップモードを選択してください', font=('Times New Roman', 20)).pack()
        self.selected_value = tk.StringVar(value="1")
        modes = [("1: フルステップ", "1"), ("2: ハーフステップ", "2"), ("4: 1/4ステップ", "4"), 
                 ("8: 1/8ステップ", "8"), ("16: 1/16ステップ", "16")]
        for mode, value in modes:
            tk.Radiobutton(self, text=mode, variable=self.selected_value, value=value, font=("Times New Roman", 16)).pack()
        ttk.Label(self, text='動かしたい距離を入力してください(単位:μm)', font=('Times New Roman', 20)).pack()
        self.entry = tk.Entry(self, bd=10)
        self.entry.pack()
        tk.Button(self, text="動かす", command=self.on_button_click, font=('Times New Roman', 20)).pack()

    def on_button_click(self):
        self.distance = self.entry.get()
        self.microstep_mode = self.selected_value.get()
        self.start_motor_control()

    def start_motor_control(self):
        if self.distance.isdigit() or (self.distance.startswith('-') and self.distance[1:].isdigit()):
            steps = int(int(self.distance)*int(self.microstep_mode)/25)
            threading.Thread(target=self.send_steps, args=(self.microstep_mode, steps)).start()

    def send_steps(self, microstep_mode, steps):
            a = str(microstep_mode) + " " + str(steps)
            self.arduino.write(bytes(a, 'ascii'))

    def on_closing(self):
        self.arduino.close()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
