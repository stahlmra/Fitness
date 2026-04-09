import streamlit as st

# -------------------------
# Seiten-Config
# -------------------------
st.set_page_config(page_title="Fitness Food", layout="wide")

# -------------------------
# Custom CSS (Schwarz + Neon Grün)
# -------------------------
st.markdown("""
<style>
body {
    background-color: #0a0a0a;
    color: white;
}
.stApp {
    background-color: #0a0a0a;
}
h1, h2, h3 {
    color: #39ff14;
}
.stButton>button {
    background-color: #39ff14;
    color: black;
    border-radius: 10px;
    font-weight: bold;
}
.stSelectbox, .stNumberInput, .stSlider {
    background-color: #111;
    color: white;
}
.card {
    background-color: #111;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    box-shadow: 0 0 10px #39ff14;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Navigation
# -------------------------
page = st.sidebar.radio("Navigation", ["Startseite", "Essensbox erstellen", "BMI Rechner"])

# -------------------------
# STARTSEITE
# -------------------------
if page == "Startseite":
    st.markdown("<h1 style='text-align:center'>🔥 Fitness Food Boxes</h1>", unsafe_allow_html=True)
    st.markdown("### Willkommen bei deiner interaktiven Fitness-Ernährungsplattform 💪")
    st.markdown("Stelle dir direkt hier deine eigene Full Day of Eating Box zusammen!")

    st.markdown("---")
    
    # Interaktive Mini-Box Auswahl
    st.markdown("## 📦 Mini-Box Vorschau (klicke deine Zutaten an!)")
    col1, col2, col3 = st.columns(3)
    with col1:
        protein = st.selectbox("Protein", ["Hähnchen", "Rind", "Tofu", "Lachs"])
    with col2:
        carbs = st.selectbox("Kohlenhydrate", ["Reis", "Süßkartoffel", "Nudeln", "Quinoa"])
    with col3:
        fats = st.selectbox("Fette", ["Avocado", "Nüsse", "Olivenöl"])
    extras = st.multiselect("Extras", ["Protein Shake", "Snack Bar", "Obst", "Yogurt Bites"])

    st.markdown("### Deine aktuelle Box enthält:")
    st.markdown(f"- Protein: **{protein}**")
    st.markdown(f"- Kohlenhydrate: **{carbs}**")
    st.markdown(f"- Fette: **{fats}**")
    if extras:
        st.markdown(f"- Extras: **{', '.join(extras)}**")
    else:
        st.markdown("- Extras: **keine**")

    # Mini Preisberechnung direkt auf Startseite
    meals_per_day = st.slider("Mahlzeiten pro Tag", 2, 6, 3)
    days = st.slider("Für wie viele Tage?", 1, 7, 3)
    base_price = 8
    total_price = base_price * meals_per_day * days
    st.markdown(f"### 💰 Geschätzter Preis: {total_price} €")

    st.markdown("---")

    # Highlights & Fun Facts
    st.subheader("💥 Unsere Highlights")
    st.markdown("""
    - 🥗 **Low Sugar & Clean Ingredients**  
    - 💪 **25g Protein pro Portion**  
    - ⏱️ **Snack oder Meal in Minuten bereit**  
    - 🍽️ **Perfekt für Cutting, Maintenance & Bulking**
    """)

    st.subheader("💡 Fun Facts & Tipps")
    st.markdown("""
    - Protein unterstützt Muskelaufbau 🏋️‍♂️  
    - Kleine Mahlzeiten stabilisieren den Blutzucker 🌡️  
    - Meal Prep spart bis zu 5 Stunden pro Woche ⏳  
    - Snacks clever planen = keine Heißhungerattacken 🍓
    """)

    # Call-to-Action Buttons
    st.markdown("---")
    st.markdown("## 🚀 Starte jetzt!")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🍱 Box zusammenstellen"):
            st.session_state.page = "Essensbox erstellen"
    with col2:
        if st.button("🧮 BMI Rechner"):
            st.session_state.page = "BMI Rechner"

# -------------------------
# ESSENSBOX BUILDER
# -------------------------
elif page == "Essensbox erstellen":
    st.title("🍱 Baue deine eigene Box")
    st.subheader("1️⃣ Ziel wählen")
    ziel = st.selectbox("Dein Ziel", ["Cutting", "Maintenance", "Bulking"])

    st.subheader("2️⃣ Mahlzeiten auswählen")
    protein = st.selectbox("Proteinquelle", ["Hähnchen", "Rind", "Tofu", "Lachs"])
    carbs = st.selectbox("Kohlenhydrate", ["Reis", "Süßkartoffel", "Nudeln", "Quinoa"])
    fats = st.selectbox("Fette", ["Avocado", "Nüsse", "Olivenöl"])
    extras = st.multiselect("Extras", ["Protein Shake", "Snack Bar", "Obst", "Yogurt Bites"])

    st.subheader("3️⃣ Menge & Preis")
    meals_per_day = st.slider("Mahlzeiten pro Tag", 2, 6, 3)
    days = st.slider("Für wie viele Tage?", 1, 7, 3)
    base_price = 8
    total_price = base_price * meals_per_day * days
    st.markdown(f"### 💰 Preis: {total_price} €")

    st.subheader("4️⃣ Vorbestellung")
    name = st.text_input("Dein Name")
    email = st.text_input("Deine E-Mail")
    if st.button("🚀 Vorbestellen"):
        if name and email:
            st.success("✅ Bestellung gespeichert! (Simulation)")
        else:
            st.error("Bitte Name und E-Mail eingeben.")

# -------------------------
# BMI RECHNER + Fragen
# -------------------------
elif page == "BMI Rechner":
    st.title("🧮 BMI Rechner & Ernährungsfragen")
    gewicht = st.number_input("Gewicht (kg)", min_value=30.0, max_value=200.0)
    groesse = st.number_input("Größe (cm)", min_value=120.0, max_value=230.0)
    ziel = st.selectbox("Dein Fitness-Ziel", ["Cutting", "Maintenance", "Bulking"])

    if st.button("BMI berechnen"):
        bmi = gewicht / ((groesse / 100) ** 2)
        st.markdown(f"### Dein BMI: {round(bmi, 2)}")

        if bmi < 18.5:
            st.warning("Untergewicht")
            tip = "💡 Tipp: Setze auf proteinreiche, kalorienoptimierte Mahlzeiten, um gesund zuzunehmen."
        elif 18.5 <= bmi < 25:
            st.success("Normalgewicht")
            tip = "💡 Tipp: Halte deine Ernährung ausgewogen und passe Protein & Kalorien an dein Training an."
        elif 25 <= bmi < 30:
            st.warning("Übergewicht")
            tip = "💡 Tipp: Reduziere einfache Kohlenhydrate, erhöhe Proteine, kombiniere mit regelmäßigem Training."
        else:
            st.error("Adipositas")
            tip = "💡 Tipp: Konsultiere ggf. einen Arzt oder Ernährungsberater. Fokus auf gesunde, kalorienkontrollierte Ernährung."
        st.markdown(tip)

    st.markdown("---")
    st.subheader("❓ Stelle eine Frage an deine Fitness Food App")
    user_question = st.text_input("Deine Frage hier... (z.B. 'Wie viele Mahlzeiten für Cutting?')")

    if st.button("Antwort erhalten"):
        if user_question:
            question = user_question.lower()
            if "cutting" in question:
                st.info("Für Cutting empfehlen wir 3–5 kleinere Mahlzeiten pro Tag, proteinreich, kalorienbewusst.")
            elif "bulking" in question or "muskel" in question:
                st.info("Für Bulking empfehlen wir 4–6 Mahlzeiten pro Tag, proteinreich und kalorienüberschuss.")
            elif "maintenance" in question:
                st.info("Für Maintenance 3–5 Mahlzeiten pro Tag, ausgewogen und kalorienneutral.")
            elif "bmi" in question:
                st.info("Dein BMI hilft dir, dein Gewicht im Verhältnis zur Größe einzuschätzen.")
            else:
                st.info("Interessante Frage! Achte auf dein Fitness-Ziel und eine ausgewogene Ernährung.")
        else:
            st.error("Bitte schreibe zuerst eine Frage.")
