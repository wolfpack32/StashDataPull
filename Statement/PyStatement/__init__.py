# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:26:35 2022

@author: rtilgner
"""

from .formatting import PyStatement
from .gui import GUI
__all__ = ["PyStatement"]

window = GUI()
window.mainloop()