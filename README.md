# 🌍 SDG Impact Analyzer

An AI-powered interactive tool that predicts which **United Nations Sustainable Development Goal (SDG)** a user’s idea contributes to and visualizes relevant global development data using indicators from the World Bank.

The application combines **Natural Language Processing (NLP)**, **Machine Learning**, and **data visualization** to help users understand the potential global development impact of their ideas.

---

# 🚩 Problem Statement

Innovators, students, and policymakers often have ideas that could support global development goals, but it is difficult to determine:

* Which **Sustainable Development Goal (SDG)** the idea aligns with
* Where in the world the issue is most relevant
* What global data supports the need for such solutions

Without accessible analytical tools, linking ideas to global development priorities can be challenging.

This project addresses that problem by providing a simple AI interface where users can input an idea and receive:

1. A predicted **Sustainable Development Goal**
2. A **global visualization of development indicators**
3. Insight into the potential worldwide relevance of the idea

---

# 🎯 Project Objectives

The main objectives of the project are:

* Build a **machine learning model** that predicts SDGs from textual ideas
* Integrate **global development datasets**
* Provide **interactive visualizations**
* Create an accessible **web-based interface**

---

# 📊 Data Sources

The project uses global development indicators from:

World Bank – World Development Indicators (WDI)

These datasets provide statistics on topics such as:

* energy access
* poverty
* agriculture
* education
* economic development
* infrastructure

---

# 🧠 Machine Learning Approach

The project uses **Natural Language Processing (NLP)** to analyze user input.

### Steps

1. Collect training examples mapping ideas to SDGs
2. Convert text into numerical features using TF-IDF vectorization
3. Train a classification model to predict SDG labels
4. Deploy the model inside an interactive application

---

# ⚙️ System Architecture

The system follows this workflow:

User Idea
↓
Text Vectorization (TF-IDF)
↓
Machine Learning Model
↓
Predicted SDG
↓
Global Development Dataset
↓
Interactive Visualization

---

# 💻 Application Interface

The application was built using **Streamlit**.

The interface allows users to:

* Enter an idea or project description
* Analyze the idea using the ML model
* View a predicted SDG
* Explore global development data through an interactive world map

---

# 🗂 Project Structure

```
sdg-impact-analyzer
│
├── app.py
├── models
│   ├── sdg_model.pkl
│   └── vectorizer.pkl
│
├── data
│   └── worldbank_data.csv
│
├── training_text
│   └── sdg_training_data.csv
│
├── requirements.txt
└── README.md
```

---

# 🔎 Code Design

## 1. Model Training

A dataset of example ideas mapped to SDGs is processed.

Steps:

* Text cleaning
* TF-IDF vectorization
* Model training using a classification algorithm
* Exporting the trained model as a `.pkl` file

The trained model and vectorizer are saved in the `models` directory.

---

## 2. Streamlit Application

The `app.py` file performs the following operations:

### Load ML Components

The trained model and vectorizer are loaded using pickle.

### Load Global Dataset

The application loads development indicators from the World Bank dataset.

### User Input

Users enter a text description of an idea.

### SDG Prediction

The input text is transformed using the vectorizer and passed into the machine learning model to generate a predicted SDG.

### Data Visualization

The application automatically detects the latest available year in the dataset and visualizes global values using a world choropleth map.

---

# 📈 Visualization

The project uses **Plotly** to generate an interactive choropleth map that displays development indicators by country.

This allows users to quickly see:

* geographic distribution of development indicators
* countries most affected by specific issues
* potential regions where solutions could have impact

---

# 🚀 How to Run the Project

## 1. Clone the repository

```
git clone https://github.com/yourusername/sdg-impact-analyzer.git
cd sdg-impact-analyzer
```

## 2. Install dependencies

```
pip install -r requirements.txt
```

## 3. Run the application

```
streamlit run app.py
```

## 4. Open the interface

```
http://localhost:8501
```

---

# 🌐 Deployment

The application can be deployed online using **Streamlit Community Cloud**, allowing users to access the interface through a public URL.

---

# 🧩 Technologies Used

Python
Streamlit
Scikit-learn
Pandas
Plotly
Machine Learning (NLP)

---

Live Demo:

https://sdg-impact-analyzer-mqrsj4irhsmeb66the9tgq.streamlit.app/




# 📚 Potential Future Improvements

Possible extensions of this project include:

* Mapping SDGs to multiple indicators
* Showing top countries where an idea would have highest impact
* Adding multiple machine learning models
* Improving SDG prediction accuracy
* Integrating additional datasets from UN or WHO

---

# 📜 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

Joseph Albert D Costa



