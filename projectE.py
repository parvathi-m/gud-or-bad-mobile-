import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv('dete.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()],['gud or bad level'],show_hist=False)
fig.show()