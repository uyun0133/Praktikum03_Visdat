import streamlit as st
import matplotlib.pyplot as plt 

# Buat dta sample 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Layout Streamlit 
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi",("Single Line Plot",
                                                        "Multiple & Customizations",
                                                        "Jenis Garis untuk Menunjukan Tren",
                                                        "Subplot"))
st.header("Kelompok 20")
st.markdown("""
1. FAHLIA ATHIYYA MARWA - 0110122176
2. FAHMI YUSRON FADILLAH - 0110222072
3. UYUN NILJANAH - 0110222081
""")

# Single Line Plot 
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle="--", marker='o')
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Multiple Line Plot & Customization 
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A",  color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label="Product B", color='red', linestyle='--', marker='x')

    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend() 
    ax.grid(True)
    st.pyplot(fig)

# Jenis Garis untuk Tren 
product_C_sales = [18, 22, 25, 28, 32, 38, 42, 45, 48, 52, 56, 60]
product_D_sales = [7, 9, 11, 13, 16, 20, 23, 25, 28, 30, 33, 35]
def tren_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_C_sales, label='Product C', color='green', linestyle="--")
    ax.plot(months, product_D_sales, label='Product D', color='purple', linestyle="--")

    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Subplot
def subplots():
     fig, ax = plt.subplots(2, 1, figsize=(10, 8))

     # plot pertama untuk product C
     ax[0].plot(months, product_C_sales, label='Product C', color='green', marker="d")
     ax[0].set_title('Penjualan Produk C Per Bulan')
     ax[0].set_xlabel('Bulan')
     ax[0].set_ylabel('Jumlah Penjualan')
     ax[0].legend()
     ax[0].grid(True)

     # plot pertama untuk product D
     ax[1].plot(months, product_D_sales, label='Product D', linestyle="--", color='purple')
     ax[1].set_title('Penjualan Produk C Per Bulan')
     ax[1].set_xlabel('Bulan')
     ax[1].set_ylabel('Jumlah Penjualan')
     ax[1].legend()
     ax[1].grid(True)

     plt.tight_layout()
     st.pyplot(fig)

# Logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customizations":
    customize_line_plot()
elif option == "Jenis Garis untuk Menunjukan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()