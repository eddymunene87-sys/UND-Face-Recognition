import customtkinter as ctk


class BasePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="nsew")