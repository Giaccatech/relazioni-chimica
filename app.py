import streamlit as st
st.title("Il mio generatore di relazioni di Chimica! 🧪")

import streamlit as st

# Titolo del sito
st.title("🧪 Relazioni di Chimica PRO")
st.write("Compila i campi qui sotto per creare la tua relazione perfetta.")

# --- SEZIONE DOMANDE ---
# Qui chiediamo all'utente di scrivere le cose
titolo_esp = st.text_input("Titolo dell'esperimento")
scopo_esp = st.text_area("Scopo dell'esperimento (cosa vogliamo dimostrare?)")

st.warning("Ricordati di mettere portata e sensibilità degli strumenti!")
strumenti = st.text_area("Strumenti usati")

procedimento = st.text_area("Procedimento (scrivi a punti)")

# --- BOTTONE PER GENERARE ---
# Se l'utente preme il bottone...
if st.button("Genera Relazione"):
    
    st.divider() # Fa una linea di separazione
    st.success("Ecco la tua relazione pronta da stampare! (Premi Ctrl+P)")
    
    # Qui il sito "stampa" a schermo quello che l'utente ha scritto prima
    st.header(titolo_esp)
    
    st.subheader("1. Scopo")
    st.write(scopo_esp)
    
    st.subheader("2. Strumenti")
    st.write(strumenti)
    
    st.subheader("3. Procedimento")
    st.write(procedimento)
