import tkinter as tk

def on_click(event):
    root.destroy()
    with open("somefile.py") as f:
        code = compile(f.read(), "/path/to/my/file.py", 'exec')
        exec(code, global_vars, local_vars)


root = tk.Tk()
button = tk.Button(root, text="Run")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button.bind("<Button-1>", on_click)
tk.mainloop()