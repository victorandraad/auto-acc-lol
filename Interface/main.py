import tkinter as tk

app = tk.Tk()
app.geometry("400x300")
app.resizable(False, False)
app.title('[BETA] - OTP')

label = tk.Label(app, text='[BETA] - OTP BOT', font=('Arial', 16))
label.config()
label.pack()
app.config(bg='black')
app.mainloop()