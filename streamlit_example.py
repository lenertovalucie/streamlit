import streamlit as st

st.write('Hello, world!')

user_input = st.text_input("Zadejte něco a stiskněte enter:")
st.write('Zadali jste: ', user_input)

# Přidání tlačítka
if st.button('Stiskni mě'):
    st.write('Tlačítko bylo stisknuto!')

# Přidání posuvníku pro výběr čísla
number = st.slider('Vyber číslo:', 0, 100, 50)
st.write('Vybrané číslo:', number)

# Přidání výběru z možností
option = st.selectbox(
    'Jakou máte rádi zmrzlinu?',
    ('Čokoládová', 'Vanilková', 'Jahodová')
)
st.write('Vaše oblíbená zmrzlina:', option)

st.markdown("""
# Nadpis první úrovně
Toto je *kurzíva* a toto je **tučné**.

- Bod 1
- Bod 2
- Bod 3

""")