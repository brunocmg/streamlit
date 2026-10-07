import streamlit as st


def caesar_cipher(text, shift, mode='encrypt'):
    """
    Implementa a cifra de César para criptografar ou descriptografar um texto.

    Args:
        text (str): O texto a ser processado.
        shift (int): O número de posições para "deslocar" cada letra.
        mode (str): 'encrypt' para criptografar, 'decrypt' para descriptografar. Padrão é 'encrypt'.

    Returns:
        str: O texto processado.
    """
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            result += shifted_char
        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            result += shifted_char
        else:
            result += char
    return result


st.title("Cifra de César")

# Entradas do usuário
text = st.text_area("Digite o texto:", value="Hello, World!")

shift = st.number_input(
    "Deslocamento (shift):",
    min_value=1,
    max_value=25,
    value=3,
    step=1,
)

mode_label = st.radio("Modo:", ["Criptografar", "Descriptografar"], horizontal=True)
mode = 'encrypt' if mode_label == "Criptografar" else 'decrypt'

# Processa ao clicar no botão
if st.button("Executar"):
    result = caesar_cipher(text, int(shift), mode=mode)

    st.subheader("Resultado:")
    st.code(result, language=None)