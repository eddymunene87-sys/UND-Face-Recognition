from gui.pages.base_page import BasePage
import customtkinter as ctk


class SettingsPage(BasePage):

    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text="Settings",
            font=("Arial", 30, "bold")
        ).pack(pady=30)