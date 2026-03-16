import numpy as np

class NoiseRemovalSetMaxValue:

    def __init__(self, max_value: int):
        self.max_value = max_value

    def transform(self, data: np.array):
        g = np.copy(data)

        for i in range(0, data.shape[0]):
          for j in range(0, data.shape[1]):
            pos = (i,j)
            if data[pos] >= self.max_value:
                g[pos] = self.max_value

        return g

class AdjustScaleWithFixedMaxValue:

    def __init__(self, max_value: int):
        self.max_value = max_value

    def transform(self, data: np.array):
        data = data.astype('float32')
        data /= self.max_value
        
        return data