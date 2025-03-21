import numpy as np
height = [1.73,1.68,1.71,1.77]
weight =[65.4,59.2,63.6,110]
np_height=np.array(height)
np_height
np_weight=np.array(weight)
np_weight
bmi = np_weight/np_height**2
print(bmi)
