import streamlit as st
import pandas as pds
import yfinance as yf

# criar funções de carregamento de dados 
    # cotações do Itau ITUB$ de 2010 a 2024
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2025-05-02")
    cotacoes_acao = cotacoes_acao[["Close"]]
    
                   
    return cotacoes_acao

dados = carregar_dados("ITUB4.SA")
print(dados)

# prepara as visualizações

# criar a interface do streamlit
st.write ("""
### App Preços ações
    O gráfico abaixo representa a variação das ações ITUB4 de 2010 a 2025
""")
# markdown
# criar o gráfico
st.line_chart(dados)

st.write ("""
# Fim do App
    
""")



          
