import skimage.io as ski
import pandas as pd
import numpy  as np
import glob

class Dataset:

    '''
    Load an image by its file_name
    '''
    def load_img(
        self, 
        img_file_name: str, 
        img_dir: str, 
        transformations: list = []):
        
        x_data = ski.imread(f'{img_dir}/{img_file_name}')
        for trf in transformations:
            x_data = trf.transform(x_data)

        return x_data