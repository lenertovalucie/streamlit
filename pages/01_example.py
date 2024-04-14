import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Vytvoření DataFrame
df = pd.DataFrame({
    'První sloupec': [1, 2, 3, 4],
    'Druhý sloupec': [10, 20, 30, 40]
})

# Zobrazení DataFrame v aplikaci
st.write("Zobrazení datového rámce:")
st.dataframe(df)

# Vytvoření grafu
plt.figure(figsize=(10, 4))
plt.bar(df['První sloupec'], df['Druhý sloupec'])

# Nastavení popisků os pro lepší čitelnost
plt.xlabel('První sloupec')
plt.ylabel('Druhý sloupec')
plt.title('Graf sloupcové hodnoty')

# Zobrazení grafu v Streamlit aplikaci
st.write("Vizualizace dat v grafu:")
st.pyplot(plt)
