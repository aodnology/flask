import konlpy
import pandas as pd
import numpy as np


df_train = pd.read_csv('ratings_train.txt', delimiter='/t', keep_default_na=False)
df_train.head()