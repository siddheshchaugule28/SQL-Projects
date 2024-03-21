import streamlit as st
#[ to open page in browser write in terminal : $ streamlit run app.py]
# search the link in browser.

import plotly.graph_objects as go
import plotly.express as px


#import DB class from dbhelper
from dbhelper import DB

# create an object 
db=DB()

# create a SIDE BAR 
st.sidebar.title("Flight Analytics")

# create a SELECT BOX
user_option=st.sidebar.selectbox('Menu',['Select one','Check Flight','Analytics'])

# Write If-Else logic to take action according to selection
if user_option=="Check Flight":
    st.title('Check Flight')
    # create two columns 
    col1,col2=st.columns(2)

    # call fetch_city_names function and store city names in city
    city=db.fetch_city_names()

    # in column 1 show Source city
    with col1:
        Source = st.selectbox('Source',sorted(city))

    # in column 2 show Destination city
    with col2:
        Destination = st.selectbox('Destination',sorted(city))
    
    # create a button for search
    if st.button("Search"):
        result = db.fetch_all_flights(Source,Destination)
        st.dataframe(result)

elif user_option=='Analytics':
    # plot pie chart
    airline,frequency=db.fetch_airlin_frequency()
    fig=go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )
    st.header("Pie chart")
    st.plotly_chart(fig)

    # plot bar graph
    # city,frequency1=db.busy_airport()
    # fig=go.Figure(
    #     go.Bar(
    #         labels=city,
    #         values=frequency,
    #         hoverinfo="label+percent",
    #         textinfo="value"
    #     )
    # )
    # st.header("Bar chart")
    # st.plotly_chart(fig)

    city,frequency1=db.busy_airport()
    fig=px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig,theme="streamlit", use_container_width=True)

else: 
    st.title('information about project')


