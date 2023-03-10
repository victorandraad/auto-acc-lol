import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x250")
# app.resizable(False, False)

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=10, fill="both", expand=True)

app.mainloop()