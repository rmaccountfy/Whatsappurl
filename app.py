import streamlit as st

def gerar_url_whatsapp(numero):
    numero_limpo = ''.join(filter(str.isdigit, numero))
    return f"https://web.whatsapp.com/send/?phone={numero_limpo}"

# Interface com Streamlit
st.title("Gerador de URL para WhatsApp")
numero_telefone = st.text_input("Digite o número de telefone:")

if st.button("Gerar URL"):
    url = gerar_url_whatsapp(numero_telefone)
    st.write("URL do WhatsApp:", url)
    st.markdown(f"[Abrir no WhatsApp]({url})")

