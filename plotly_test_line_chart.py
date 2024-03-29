import plotly.plotly as py
import plotly
from plotly.graph_objs import *

plotly.tools.set_credentials_file(username='sabb', api_key='WQqoRzGv8gKMfTDn1lsZ')

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.iplot(data, filename = 'basic-line')