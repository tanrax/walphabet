#!/usr/bin/python3
import pathlib
import pygubu
import tkinter as tk
from tkinter import filedialog
import subprocess

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main_window.ui"


class MainWindowApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("main_window", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def open_dialog(self):
        filenames = filedialog.askopenfilename(
            title="Select a Font files",
            filetypes=(("TTF files", "*.ttf"), ("OTF files", "*.otf"), ("All files", "*.*")),
            multiple=True,
        )
        self.transform_fonts(filenames)

    def transform_fonts(self, filenames):
        progress_bar = self.mainwindow.nametowidget("!progressbar")
        for index, filename in enumerate(filenames):
            args = ("./bin/linux/woff2_compress", filename)
            popen = subprocess.Popen(args, stdout=subprocess.PIPE)
            popen.wait()
            # Show progress bar
            progress_bar.place(x=0)
            # Update progress bar
            progress_bar["value"] = index * 100 / len(filenames)
            self.mainwindow.update()
        # Reset progress bar
        progress_bar["value"] = 0
        progress_bar.place(x=-200)
        self.mainwindow.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindowApp(root)
    root.title("Walphabet")
    root.resizable(False, False)
    app.run()
