import streamlit as st
import pandas as pd

import analyze_csv


def main():
    st.title("Analiza danych z pliku CSV")

    # Sekcja do uploadowania pliku
    uploaded_file = st.file_uploader("Wgraj plik CSV", type=["csv"])

    if uploaded_file is not None:
        # Wczytaj plik CSV z odpowiednim kodowaniem i separatorem
        df = pd.read_csv(uploaded_file, encoding='windows-1250', sep=';')

        # Wyświetl kilka pierwszych wierszy
        st.write("### Podgląd danych")
        st.write(df.head())

        # Przeprowadź analizę
        analyze_csv.analyze_csv(df)


if __name__ == "__main__":
    main()
