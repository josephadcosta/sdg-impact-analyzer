import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# Load ML model
model = pickle.load(open("models/sdg_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# Load World Bank dataset
data = pd.read_csv("data/worldbank_data.csv")

st.title("Global SDG Impact Analyzer")

st.write("Enter an idea and the system predicts which Sustainable Development Goal (SDG) it impacts.")

# User input
user_input = st.text_area("Enter your idea")

if st.button("Analyze"):

    # Predict SDG
    X = vectorizer.transform([user_input])
    prediction = model.predict(X)

    st.subheader("Predicted SDG")
    st.write(prediction[0])

    st.subheader("Global Data Visualization")

    # Detect year columns automatically (like '1960 [YR1960]')
    year_columns = [col for col in data.columns if "YR" in col]

    if len(year_columns) > 0:

        # Select the most recent year
        year_column = year_columns[-1]

        df = data[["Country Name", year_column]].copy()

        # Convert values to numeric
        df[year_column] = pd.to_numeric(df[year_column], errors="coerce")

        df = df.dropna()

        df.columns = ["country", "value"]

        fig = px.choropleth(
            df,
            locations="country",
            locationmode="country names",
            color="value",
            title=f"World Development Indicator ({year_column})"
        )

        st.plotly_chart(fig)

    else:
        st.write("No year columns found in dataset.")