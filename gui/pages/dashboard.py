import customtkinter as ctk

from gui.pages.base_page import BasePage


class Dashboard(BasePage):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=25)

        preview = ctk.CTkFrame(
            self,
            width=750,
            height=500
        )

        preview.pack(pady=20)

        preview.pack_propagate(False)

        label = ctk.CTkLabel(
            preview,
            text="Camera Preview"
        )

        label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )