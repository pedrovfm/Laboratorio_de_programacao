import numpy as np
import pandas as pd
matriz = np.array([['Brasil', 'Brasilia', '214000000'],
                   ['Angola', 'Luanda', '34500000'],
                   ['China', 'Pequim', '1412000000']])
df = pd.DataFrame(matriz, columns=['País', 'Capital', 'População'])
print(df)