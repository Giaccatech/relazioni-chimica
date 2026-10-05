import streamlit as st

st.set_page_config(page_title="AI Relazioni Chimica", page_icon="🤖")

st.title("🤖 Generatore AI per Relazioni di Chimica")
st.write("Scrivi i tuoi appunti grezzi. L'AI li trasformerà in una relazione da massimo dei voti seguendo la griglia del prof!")

# --- 1. SCOPO E DOMANDA ---
st.header("1. Scopo e Domanda Investigabile")
appunti_scopo = st.text_area("Cosa volevate scoprire? Qual era la domanda iniziale?", 
                             placeholder="Es. Volevamo vedere se l'acqua bolle prima col sale. Domanda: Il sale altera il punto di ebollizione?")

# --- 2. CAMPIONI E MATERIALI (Qui si fanno i punti grossi!) ---
st.header("2. Campioni, Materiali e Strumenti")
st.warning("Ricorda: Il prof dà 9 punti sui campioni! Spiega a cosa servivano.")
appunti_campioni = st.text_area("Che campioni e reagenti avete usato? A cosa servivano? Cosa ti aspettavi succedesse?", 
                                placeholder="Es. Acqua di rubinetto (solvente). Sale grosso (soluto). Mi aspettavo che sciogliendosi alzasse la temperatura.")
appunti_strumenti = st.text_area("Strumenti usati (con portata/sensibilità) e materiali di consumo", 
                                 placeholder="Es. Becher da 250ml, termometro sensibilità 1°C, piastra riscaldante.")

# --- 3. PROCEDIMENTO E DATI ---
st.header("3. Procedimento e Dati")
appunti_procedimento = st.text_area("Cosa avete fatto fisicamente? (Scrivilo in modo grezzo)", 
                                    placeholder="Es. Abbiamo messo 100ml di acqua nel becher, acceso la piastra e aspettato. Poi abbiamo buttato 10g di sale...")
appunti_dati = st.text_area("Che dati avete raccolto? Che calcoli hai fatto?", 
                            placeholder="Es. L'acqua bolliva a 102°C.")

# --- 4. CONCLUSIONI ---
st.header("4. Conclusioni (Valgono 6 punti!)")
appunti_conclusioni = st.text_area("L'esperimento ha risposto alla domanda? Che problemi ci sono stati? Come lo miglioreresti?", 
                                   placeholder="Es. Sì, il sale alza la temperatura. Però abbiamo disperso calore, la prossima volta userei un coperchio.")

# --- BOTTONE ---
if st.button("✨ Fai la Magia (Genera con AI)"):
    st.info("Questa funzione si collegherà a breve all'Intelligenza Artificiale!")
    # Per ora stampiamo solo a schermo per vedere se le caselle funzionano
    st.write("I tuoi appunti sono stati salvati. Stiamo preparando l'integrazione con l'AI!")
