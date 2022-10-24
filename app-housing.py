import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Siran Wang')

df = pd.read_csv('housing.csv')

price_filter = st.sidebar.slider('Median House Price', 0, 500001, 200000)
location_filter = st.sidebar.multiselect('Location', df.ocean_proximity.unique(), df.ocean_proximity.unique())
income_filter = st.sidebar.radio('income level', ('Low', 'Medium', 'High'))

df = df[df.median_house_value <= price_filter]
df = df[df.ocean_proximity.isin(location_filter)]
if income_filter is not None:
    if income_filter == 'Low':
        df = df[df.median_income <= 2.5]
    elif income_filter == 'Medium':
        df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
    elif income_filter == 'High':
        df = df[df.median_income > 4.5]
else:
    pass

fig, ax = plt.subplots()
house_price = df.median_house_value
house_price.hist(ax=ax, bins=30)

st.map(df)
st.pyplot(fig)