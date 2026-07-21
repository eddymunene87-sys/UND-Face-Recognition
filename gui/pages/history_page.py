from gui.pages.base_page import BasePage
import customtkinter as ctk


class HistoryPage(BasePage):

    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text="History",
            font=("Arial", 30, "bold")
        ).pack(pady=30)