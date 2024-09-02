import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def analyze_csv(df):
    # Upewnij się, że kolumna "Czas cyklu mieszarki" jest numeryczna
    df['Czas cyklu mieszarki'] = pd.to_numeric(df['Czas cyklu mieszarki'], errors='coerce')

    # Oblicz podstawowe statystyki
    cycle_time_stats = df['Czas cyklu mieszarki'].describe()

    # Wyświetl statystyki
    st.write("### Podstawowe statystyki 'Czas cyklu mieszarki'")
    st.write(cycle_time_stats)

    # Wyświetl wykres histogramu
    st.write("### Rozkład 'Czas cyklu mieszarki'")
    plt.figure(figsize=(10, 6))
    plt.hist(df['Czas cyklu mieszarki'].dropna(), bins=20, color='blue', edgecolor='black')
    plt.title('Distribution of Czas Cyklu Mieszarki')
    plt.xlabel('Czas cyklu mieszarki (sekundy)')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt)


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
        analyze_csv(df)


if __name__ == "__main__":
    main()
