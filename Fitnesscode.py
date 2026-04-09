import streamlit as st

st.set_page_config(page_title="Fitness Food", layout="wide")

# -------------------------
# CUSTOM CSS (NEXT LEVEL UI)
# -------------------------
st.markdown("""
<style>
/* Hintergrund */
.stApp {
    background-color: #050505;
    color: white;
}

/* Neon Glow Effekt */
.neon {
    color: #39ff14;
    text-shadow: 0 0 10px #39ff14, 0 0 20px #39ff14;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #39ff14, #00ff99);
    color: black;
    border-radius: 12px;
    font-weight: bold;
    height: 3em;
}

/* Card Look */
.card {
    background-color: #111;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(57,255,20,0.3);
    margin-bottom: 20px;
}

/* Sidebar */
.css-1d391kg {
    background-color: #0a0a0a;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
page = st.sidebar.radio("Navigation", [
    "Startseite",
    "Essensbox",
    "Kalorienrechner",
])

# -------------------------
# STARTSEITE (UPGRADE)
# -------------------------
if page == "Startseite":

    # Logo
    st.image("assets/logo.png", width=150)

    st.markdown("<h1 class='neon'>FULL DAY OF EATING</h1>", unsafe_allow_html=True)

    st.image("assets/hero.jpg", use_column_width=True)

    st.markdown("""
    ## 💪 Dein Fitness. Dein Plan. Dein Essen.

    Keine Zeit zu kochen? Kein Problem.  
    Wir liefern dir komplette **Full Day of Eating Boxen** – perfekt abgestimmt auf dein Ziel.

    ---
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>🔥 Cutting</h3><p>Fett verlieren, Muskeln behalten.</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>⚖️ Maintenance</h3><p>Gewicht halten, clean essen.</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h3>💪 Bulking</h3><p>Muskelaufbau mit Überschuss.</p></div>", unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🚀 Warum wir?")
    st.write("""
    - Individuell anpassbare Boxen  
    - Hochwertige Zutaten  
    - Perfekt für Fitnessziele  
    - Spart Zeit & Aufwand  
    """)

# -------------------------
# ESSENSBOX BUILDER
# -------------------------
elif page == "Essensbox":

    st.markdown("<h1 class='neon'>🍱 Baue deine Box</h1>", unsafe_allow_html=True)

    ziel = st.selectbox("Ziel", ["Cutting", "Maintenance", "Bulking"])

    protein = st.selectbox("Protein", ["Hähnchen", "Rind", "Tofu", "Lachs"])
    carbs = st.selectbox("Carbs", ["Reis", "Nudeln", "Quinoa"])
    fats = st.selectbox("Fette", ["Avocado", "Nüsse"])

    extras = st.multiselect("Extras", ["Shake", "Riegel", "Obst"])

    meals = st.slider("Mahlzeiten/Tag", 2, 6, 3)
    days = st.slider("Tage", 1, 7, 3)

    price = meals * days * 9

    st.markdown(f"## 💰 {price} €")

    name = st.text_input("Name")
    email = st.text_input("E-Mail")

    if st.button("Vorbestellen"):
        if name and email:
            st.success("🔥 Bestellung gespeichert (Demo)")
        else:
            st.error("Bitte alles ausfüllen")

# -------------------------
# KALORIENRECHNER (NEU 🔥)
# -------------------------
elif page == "Kalorienrechner":

    st.markdown("<h1 class='neon'>🧮 Kalorienrechner</h1>", unsafe_allow_html=True)

    gewicht = st.number_input("Gewicht (kg)", 40.0, 200.0)
    groesse = st.number_input("Größe (cm)", 140.0, 220.0)
    alter = st.number_input("Alter", 14, 80)

    geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])

    aktivitaet = st.selectbox("Aktivität", [
        "Wenig Bewegung",
        "Leicht aktiv",
        "Sportlich",
        "Sehr aktiv"
    ])

    if st.button("Berechnen"):

        # Grundumsatz (Mifflin-St Jeor)
        if geschlecht == "Männlich":
            bmr = 10 * gewicht + 6.25 * groesse - 5 * alter + 5
        else:
            bmr = 10 * gewicht + 6.25 * groesse - 5 * alter - 161

        faktor = {
            "Wenig Bewegung": 1.2,
            "Leicht aktiv": 1.375,
            "Sportlich": 1.55,
            "Sehr aktiv": 1.725
        }

        tdee = bmr * faktor[aktivitaet]

        st.markdown(f"## 🔥 Erhaltung: {int(tdee)} kcal")
        st.markdown(f"## 🔻 Cutting: {int(tdee - 500)} kcal")
        st.markdown(f"## 🔺 Bulking: {int(tdee + 300)} kcal")
