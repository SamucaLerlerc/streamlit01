# import streamlit as st 
# import pandas as pd
# dados = {"Produto" : ["Caneta", "Caderno", "Lapís"] , "Preco": [2.5,15.0,1.0] }
# df = pd.DataFrame(dados)
# st.title("Minha loja")
# st.dataframe(df)
# categoria = st.selectbox("Escolha uma categoria:", ["Pizza", "Cachorro quente", "Hamburger"])
# valor_maximo = st.slider("Valor Máximo:", min_value=0, max_value=100, value=50)
# categorias = st.multiselect ("Escolha categorias", ["Pizza", "Cachorro quente", "Hamburguer"])

import streamlit as st 
import pandas as pd

dados = {
    "restaurante": ["Pizza Bella", "Sushi House", "Burger King", "Doce Sabor",
    "Pizza Bella", "China in Box", "Sushi House", "Burger King",
    "Doce Sabor", "China in Box"],
    "categoria": ["Pizza", "Japonesa", "Hambúrguer", "Doces",
    "Pizza", "Chinesa", "Japonesa", "Hambúrguer",
    "Doces", "Chinesa"],
    "valor": [45.90, 60.00, 35.50, 25.00, 52.30, 40.00, 75.00, 38.90, 22.50, 48.00],
    "tempo_entrega": [35, 50, 20, 15, 40, 45, 55, 25, 18, 42],
    "avaliacao": [4.5, 4.8, 4.0, 4.2, 4.6, 3.9, 4.9, 4.1, 4.3, 4.0]
}
df = pd.DataFrame(dados)

st.sidebar.title("Filtros")
categoria_escolida = st.sidebar.selectbox(
    "Categoria", ["Todas"] + list(df["categoria"].unique())
)

valor_maximo = st.sidebar.slider(
    "Valor máximo do pedido R$:", 
    min_value=float(df["valor"].min()),
    max_value=float(df["valor"].max()),
    value=float(df["valor"].max())
)

df_filtrado = df[df["valor"] <= valor_maximo]
if categoria_escolida != "Todas":
        df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria_escolida]
    
st.subheader("Pedidos Filtrados")
st.dataframe(df_filtrado)

col1, col2 = st.columns(2)
faturamento_total = df_filtrado["valor"].sum()
avaliacao_media = df_filtrado["avaliacao"].mean() if len(df_filtrado) > 0 else 0

col1.metric("Faturamento total", f"R$ {faturamento_total:.2f}")
col2.metric("Avaliação média", f"{avaliacao_media:.1f}")

st.subheader("Valor total por restaurante")
if len(df_filtrado) > 0:
        valor_por_restaurante = df_filtrado.groupby("restaurante")["valor"].sum()
        st.bar_chart(valor_por_restaurante)
else:
    st.write("Nenhum pedido encontrado com esse filtro")