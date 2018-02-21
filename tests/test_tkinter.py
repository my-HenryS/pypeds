from unittest import TestCase
import tkinter as tk
from pypeds.gui.ui.Tkinter_UI import Tkinter_UI

class TestUI(TestCase):

    def test_ui(self):
        tkinter_ui=Tkinter_UI()
        tkinter_ui.top.mainloop()