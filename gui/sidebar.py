import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):
        super().__init__(
            parent,
            width=220,
            fg_color="#101820",
            corner_radius=0
        )

        self.grid_propagate(False)

        menu = [

            ("Dashboard", "dashboard"),
            ("Register Person", "register"),
            ("Recognition", "recognition"),
            ("History", "history"),
            ("Settings", "settings")

        ]

        for row, (text, page) in enumerate(menu):

            btn = ctk.CTkButton(
                self,
                text=text,
                anchor="w",
                command=lambda p=page: callback(p)
            )

            btn.grid(
                row=row,
                column=0,
                padx=15,
                pady=10,
                sticky="ew"
            )

        exit_btn = ctk.CTkButton(
            self,
            text="Exit",
            fg_color="red",
            command=parent.destroy
        )

        exit_btn.grid(
            row=10,
            column=0,
            padx=15,
            pady=30,
            sticky="ew"
        )