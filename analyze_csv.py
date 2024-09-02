import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
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