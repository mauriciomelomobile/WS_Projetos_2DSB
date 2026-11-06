import streamlit as st
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="etecpj2dsb",
    password="123456",
    database="login_DB"
)

if conexao.is_connected():
    st.success("Banco de Dados Conectado com Sucesso!")

conexao.close()