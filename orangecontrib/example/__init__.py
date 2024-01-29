import numpy as np
from orangewidget.utils.signals import summarize, PartialSummary

@summarize.register
def summarize_ndarray(a:np.ndarray):
    return PartialSummary(f"{a.shape[0]}x{a.shape[1]}", f"Image of size {a.shape[0]}x{a.shape[1]}")