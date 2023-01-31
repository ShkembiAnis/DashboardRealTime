from INNOLAB.DAL.DataGetter import read_data_from_database
import time
from INNOLAB.PLOTLY.FigureCreator import grouper

Start = time.time()
df = read_data_from_database(Start)



print(df)
# Outputs RangeIndex(start=0, stop=5, step=1)

