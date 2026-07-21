import customtkinter as ctk
import time


class StatusBar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            height=35,
            corner_radius=0,
            fg_color="#182430"
        )

        self.label = ctk.CTkLabel(
            self,
            text=""
        )

        self.label.pack(
            side="left",
            padx=20
        )

        self.update_time()

    def update_time(self):

        current = time.strftime("%H:%M:%S")

        self.label.configure(
            text=f"Camera Ready      {current}"
        )

        self.after(
            1000,
            self.update_time
        )