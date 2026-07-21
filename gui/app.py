import customtkinter as ctk

from gui.header import Header
from gui.sidebar import Sidebar
from gui.statusbar import StatusBar

from gui.pages.dashboard import Dashboard
from gui.pages.register_page import RegisterPage
from gui.pages.recognition_page import RecognitionPage
from gui.pages.history_page import HistoryPage
from gui.pages.settings_page import SettingsPage


class FaceRecognitionApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ----------------------------
        # Window Settings
        # ----------------------------
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.title("Face Recognition System")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        # ----------------------------
        # Configure Main Grid
        # ----------------------------
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ----------------------------
        # Header
        # ----------------------------
        self.header = Header(self)

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        # ----------------------------
        # Sidebar
        # ----------------------------
        self.sidebar = Sidebar(
            self,
            self.show_page
        )

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns"
        )

        # ----------------------------
        # Main Content Area
        # ----------------------------
        self.content_frame = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.content_frame.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        self.content_frame.grid_rowconfigure(
            0,
            weight=1
        )

        self.content_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # ----------------------------
        # Status Bar
        # ----------------------------
        self.status = StatusBar(self)

        self.status.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        # ----------------------------
        # Create All Pages
        # ----------------------------
        self.pages = {

            "dashboard":
                Dashboard(self.content_frame),

            "register":
                RegisterPage(self.content_frame),

            "recognition":
                RecognitionPage(self.content_frame),

            "history":
                HistoryPage(self.content_frame),

            "settings":
                SettingsPage(self.content_frame)

        }

        # Put every page in the same grid position
        for page in self.pages.values():

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        # Show Dashboard First
        self.show_page("dashboard")

    # ---------------------------------
    # Page Manager
    # ---------------------------------

    def show_page(self, page_name):

        page = self.pages.get(page_name)

        if page:

            page.tkraise()