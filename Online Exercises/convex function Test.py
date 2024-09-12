import numpy as np
import pandas as pd

def run (random, /, *args, strict=False, **kwargs):
    """
    This function is used to run the model
    """
    ts=pd.Series(random(*args, **kwargs))
    A, B=np.log(ts.mean()), np.log(ts).mean()
    return A, B, A>B or not strict and np.abs(A-B)<1e-9

size=1000
strict=False

print(run(np.random.normal, size=size, loc=0, scale=1, strict=strict)[-1])
