import dash
import pandas as pd

import plotly.express as px
import pandas as pd
import dash_html_components as html
import plotly.graph_objects as go

#Analysing the count of sent vs received messages year wise
dfMessages=pd.read_csv('./data/Messages_Modified.csv')
dfMessages['DATE'] = pd.DatetimeIndex(dfMessages['DATE']).year
dfMessagesSent=dfMessages[dfMessages['FROM']=='Komal Khetlani']
dfMessagesReceived=dfMessages[dfMessages['TO']=='Komal Khetlani']
dfMessagesSentCount=dfMessagesSent.groupby(['DATE']).size().reset_index(name="Count")
dfMessagesReceivedCount=dfMessagesReceived.groupby(['DATE']).size().reset_index(name="Count")
fig1 = go.Figure(data=[
    go.Bar(name='Sent', x=dfMessagesSentCount['DATE'], y=dfMessagesSentCount['Count']),
    go.Bar(name='Received', x=dfMessagesReceivedCount['DATE'], y=dfMessagesReceivedCount['Count'])
])
fig1.update_layout(barmode='stack')


app = dash.Dash(__name__, title="LinkedIn Data Visualisation")

app.layout=html.Div(children=[
    html.H1("Hello World"),
    html.H1("Hello World"),
    dcc.Graph(id='messageGraph',figure=fig1)
])

if __name__ == '__main__':

    app.run_server(debug=False)