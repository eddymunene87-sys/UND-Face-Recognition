import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Face Recognition System",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=30)

        self.register_btn = ctk.CTkButton(
            self,
            text="Register Person",
            width=250,
            height=45
        )

        self.register_btn.pack(pady=15)

        self.recognize_btn = ctk.CTkButton(
            self,
            text="Start Recognition",
            width=250,
            height=45
        )

        self.recognize_btn.pack(pady=15)

        self.settings_btn = ctk.CTkButton(
            self,
            text="Settings",
            width=250,
            height=45
        )

        self.settings_btn.pack(pady=15)

        self.exit_btn = ctk.CTkButton(
            self,
            text="Exit",
            fg_color="red",
            width=250,
            height=45
        )

        self.exit_btn.pack(pady=15)