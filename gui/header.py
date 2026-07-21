import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            height=70,
            corner_radius=0,
            fg_color="#182430"
        )

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            self,
            text="🧠 Face Recognition System",
            font=("Arial", 24, "bold")
        )

        title.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        user = ctk.CTkLabel(
            self,
            text="Administrator",
            font=("Arial", 15)
        )

        user.grid(row=0, column=1, padx=20)