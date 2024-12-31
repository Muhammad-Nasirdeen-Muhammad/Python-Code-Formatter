import time
import tkinter as tk
from tkinter import filedialog


try:
    import autopep8

    def wait(secs=1):
        time.sleep(secs)
    class GUI:
        filepath = ""
        formatted_code = ""

        def __init__(self):
            self.is_content= False
            self.window = tk.Tk()
            self.label = tk.Label(
                self.window, text="Python code Formatter", font=("Segoe ui symbol", 18))
            self.window.geometry("500x550")
            self.label.pack(padx=10, pady=10)
            self.button = tk.Button(
                self.window, text="Add file", command=self.add_file)
            self.button.pack(pady=20, side=tk.BOTTOM)

            self.body = tk.Canvas(self.window)
            self.body.pack(padx=1)
            self.window.mainloop()

        def add_file(self):
            if self.is_content:
                self.sample_label.destroy()
                self.button.destroy()
                self.content_display.destroy()

            self.filepath = filedialog.askopenfile(
                title="Select a Python File to Format",
                filetypes=(("Python Files", "*.py"), ("All Files", "*.*"))
            )
            if self.filepath:
                self.py_file = open(self.filepath.name, "r+")
                filepath = self.filepath.name
                self.py_file_content = self.py_file.read()
                self.formattedCode = autopep8.fix_code(self.py_file_content)
                formatted_code = self.formattedCode
                self.sample_label = tk.Label(
                    self.body, text="Preview Code...", font=("Arial", 12))
                self.sample_label.pack()
                self.content_display = tk.Label(self.body, height=20,
                                                text=f"{self.py_file_content[0:400]}", font=("Segoe UI Symbol", 9))
                self.content_display.pack()
                self.button = tk.Button(
                    self.window, text="Format Code", command=self.clicked)
                self.button.pack()
                self.is_content = True
        def clicked(self):
            OpenFile = open(self.filepath.name, "w")
            OpenFile.write(f"{self.formattedCode}")
            self.content_display.destroy()
            self.sample_label.destroy()
            self.button.destroy()

            self.mod = tk.Label(self.body, text="Modifying...", font=("Arial", 15))
            self.mod.pack()
            wait()
            self.mod.destroy()
            self.done = tk.Label(self.body, text="Done", font=("Arial", 17))
            self.done.pack()

            #self.done.destroy()
            OpenFile.close()

except ImportError:
    print("""You don't have the required module to run this program.
     pip install autopep8 to run""")
GUI()
