import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Načtení dat
def load_data():
    data = pd.read_csv('youtube.csv')
    # Čištění dat pro jazyky a země
    data['Primary language'] = data['Primary language'].str.extract(r'([a-zA-Z ]+)')
    data['Country'] = data['Country'].str.extract(r'([a-zA-Z- ]+)')
    return data

df = load_data()

# Selekce kategorie a země pomocí Streamlit rozbalovacího seznamu
category = st.selectbox('Vyberte kategorii', options=df['Category'].unique())
country = st.selectbox('Vyberte zemi', options=df['Country'].unique())

# Filtr dat podle výběru uživatele
filtered_data = df[(df['Category'] == category) & (df['Country'] == country)]

# Vytvoření grafu
plt.figure(figsize=(10, 4))
plt.bar(filtered_data['Name'], filtered_data['Subscribers (millions)'], color='skyblue')
plt.xlabel('Název kanálu')
plt.ylabel('Počet odběratelů (milióny)')
plt.title(f'Počet odběratelů pro {category} kanály v zemi {country}')
plt.xticks(rotation=45, ha='right')

# Zobrazení grafu
st.pyplot(plt)
