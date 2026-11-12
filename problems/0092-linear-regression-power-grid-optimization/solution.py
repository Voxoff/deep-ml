import math
import numpy as np
PI = 3.14159

def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    # 2) Perform linear regression on the detrended data.
    # 3) Predict day 15's base consumption.
    # 4) Add the day 15 fluctuation back.
    # 5) Round, then add a 5% safety margin (rounded up).
    # 6) Return the final integer.
    norm = [el - fluctiation(idx+1) for idx, el in enumerate(consumption_data)]
    n = np.asarray(norm)
    days = np.asarray(list(range(1, len(n)+1)))
    days = np.vstack([days, np.ones(len(days))]).T
    w,b = np.linalg.lstsq(days, n)[0]
    target_day = 15
    target_consumption = 15 * w + b
    target_consumption += fluctiation(15)
    target_consumption = math.ceil(target_consumption)
    target_consumption = target_consumption * 1.05 
    return round(target_consumption)
    
def fluctiation(day):
    return 10 * math.sin(PI * day / 5)