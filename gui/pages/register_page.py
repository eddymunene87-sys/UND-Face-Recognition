import threading
import customtkinter as ctk
from tkinter import messagebox

from utils.register import FaceRegistrar
from utils.encoder import FaceEncoder


class RegisterPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Register New Person",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=20)

        self.name_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Enter Full Name"
        )

        self.name_entry.pack(pady=20)

        self.progress = ctk.CTkProgressBar(
            self,
            width=350
        )

        self.progress.pack(pady=20)

        self.progress.set(0)

        self.status = ctk.CTkLabel(
            self,
            text="Waiting..."
        )

        self.status.pack()

        self.register_btn = ctk.CTkButton(
            self,
            text="Start Registration",
            command=self.start_registration
        )

        self.register_btn.pack(pady=30)

    def start_registration(self):

        name = self.name_entry.get().strip()

        if not name:

            messagebox.showwarning(
                "Missing Name",
                "Please enter the person's name."
            )

            return

        self.register_btn.configure(state="disabled")

        thread = threading.Thread(
            target=self.register,
            args=(name,),
            daemon=True
        )

        thread.start()

    def register(self, name):

        try:

            self.status.configure(
                text="Capturing Images..."
            )

            self.progress.set(0.25)

            registrar = FaceRegistrar()

            registrar.register_person(name)

            self.status.configure(
                text="Generating Encodings..."
            )

            self.progress.set(0.75)

            encoder = FaceEncoder()

            encoder.encode_faces()

            self.progress.set(1)

            self.status.configure(
                text="Registration Completed"
            )

            messagebox.showinfo(
                "Success",
                f"{name} registered successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Registration Failed",
                str(e)
            )

        finally:

            self.register_btn.configure(
                state="normal"
            )

            self.progress.set(0)