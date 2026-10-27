import streamlit as st

# --- Funções da Cifra de Vigenère ---
def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - 65
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text.append(new_char)
            key_index += 1
        else:
            encrypted_text.append(char)
    return "".join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - 65
            new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text.append(new_char)
            key_index += 1
        else:
            decrypted_text.append(char)
    return "".join(decrypted_text)

# --- Interface do Streamlit ---
st.title("🔑 Cifra de Vigenère")
st.write("Criptografe ou descriptografe suas mensagens usando uma chave.")

# Entrada do usuário
mensagem = st.text_area("Digite a mensagem:", "Olá Mundo!")
chave = st.text_input("Digite a chave (apenas letras):", "KEYWORD")

# Escolha da operação
operacao = st.radio("Escolha a operação:", ("Criptografar", "Descriptografar"))

if st.button("Processar"):
    if not chave.isalpha():
        st.error("Por favor, insira uma chave contendo apenas letras.")
    elif not mensagem:
        st.warning("Por favor, insira uma mensagem.")
    else:
        if operacao == "Criptografar":
            resultado = vigenere_encrypt(mensagem, chave)
            st.success("Mensagem Criptografada:")
        else:
            resultado = vigenere_decrypt(mensagem, chave)
            st.success("Mensagem Descriptografada:")
        
        st.code(resultado)