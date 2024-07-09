import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="UNRIKA 2023",
    page_icon="😎",
)
st.write("Project T.industri<2A> DIES NATALIS 31 UNRIKA")
st.sidebar.success("silahkan dipilih,")

with st.sidebar : 
    selected = option_menu ('Mengitung Volume Bangun Ruang',
                            ['Menghitung Volume Balok',
                             'Menghitung Volume Tabung'],
                             default_index=0)

if (selected == 'Menghitung Volume Balok') : 
    st.title('Menghitung Volume Balok')
    panjang = st.slider ("masukan nilai panjang",0.0,100.0)
    lebar = st.slider ("masukan nilai lebar",0.0,100.0)
    tinggi = st.slider ("masukan nilai tinggi",0.0,100.0)
    hitung = st.button ("hitung volume")

    if hitung : 
        volume = panjang * lebar * tinggi
        st.success (f"volume Balok adalah = {volume}")

if (selected == 'Menghitung Volume Tabung') : 
    st.title('Menghitung Volume Tabung')
    r = st.slider ("masukan nilai jari-jari",0.0,100.0)
    tinggi = st.slider ("masukan nilai tinggi",0.0,100.0)
    hitung = st.button ("hitung volume")
    phi = 3.14
    if hitung : 
        volume = phi * r * r * tinggi
        st.success (f"volume Tabung adalah = {volume}")
        