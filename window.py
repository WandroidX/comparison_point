import tkinter as tk

root = tk.Tk()
root.title('Descargador De Música')

mensaje = tk.Label(root,text="""hola wandroid,
soy tu del futuro
yo soy tu padre""",justify=tk.RIGHT, fg='purple', font="Arial 30 italic")


mensaje.pack()
root.geometry('1000x600')
root.mainloop()
