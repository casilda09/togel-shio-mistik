# togel-shio-mistik
Aplikasi Togel 4D dengan Shio dan Angka Mistik
import random
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

# Daftar shio
shio_list = [
    "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
    "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
]

# Fungsi togel
def generate_togel_4d():
    return [random.randint(0, 9) for _ in range(4)]

# Fungsi shio
def get_shio(year):
    return shio_list[year % 12]

# Fungsi angka mistik
def get_mistik_number(birth_date):
    total = sum(int(digit) for digit in birth_date if digit.isdigit())
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total

# Judul aplikasi
st.title('Togel 4D + Shio + Angka Mistik')

# Input
num_simulations = st.slider('Jumlah Simulasi', 100, 5000, 1000)
birth_year = st.number_input('Tahun Kelahiran (Shio)', min_value=1900, max_value=2100, value=2000)
birth_date = st.text_input('Tanggal Lahir (format DDMMYYYY)', value='01011990')

# Hitung shio dan angka mistik
shio = get_shio(birth_year)
mistik_number = get_mistik_number(birth_date)

# Simulasi angka
semua_angka = []
for _ in range(num_simulations):
    angka = generate_togel_4d()
    semua_angka.extend(angka)

# Hitung frekuensi
frekuensi = Counter(semua_angka)
angka = list(range(10))
jumlah = [frekuensi[i] for i in angka]

# Buat grafik
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(angka, jumlah, color='skyblue', edgecolor='black')
ax.set_title(f'Frekuensi Angka 0–9 ({num_simulations} nomor)')
ax.set_xlabel('Angka')
ax.set_ylabel('Jumlah')
ax.set_xticks(angka)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Tampilkan hasil
st.write(f"**Shio:** {shio}")
st.write(f"**Angka Mistik:** {mistik_number}")
