import streamlit as st

# -----------------------------------
# CONFIG
# -----------------------------------
st.set_page_config(page_title="FORMO Nutrition", layout="wide")

# -----------------------------------
# CUSTOM CSS (NEON STYLE)
# -----------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #050505;
    color: white;
}

.neon {
    color: #39ff14;
    text-shadow: 0 0 10px #39ff14, 0 0 20px #39ff14;
}

.stButton>button {
    background: linear-gradient(90deg, #39ff14, #00ff99);
    color: black;
    border-radius: 10px;
    font-weight: bold;
    height: 3em;
}

.card {
    background-color: #111;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(57,255,20,0.3);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# NAVIGATION
# -----------------------------------
page = st.sidebar.radio("Navigation", [
    "Startseite",
    "Essensbox",
    "Kalorienrechner"
])

# -----------------------------------
# STARTSEITE
# -----------------------------------
if page == "Startseite":

    st.image("formo_logo.jpg", width=250)

    st.markdown("<h1 class='neon'>FORMO NUTRITION</h1>", unsafe_allow_html=True)
    st.markdown("### Fuel your day. Build your future.")

    st.markdown("---")

    st.image("shakes.jpg", use_column_width=True)

    st.markdown("""
    ## 🔥 MORNING FUEL. REAL RESULTS.

    ✔ 25g Protein pro Portion  
    ✔ Low Sugar  
    ✔ Perfekt für dein Fitnessziel  

    Egal ob **Cutting, Maintenance oder Bulking** – wir liefern dir die passende Ernährung.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.image("yogurt.jpg", use_column_width=True)

    with col2:
        st.markdown("""
        ## 🍓 Protein Yogurt Bites

        - High Protein  
        - Low Sugar  
        - Perfekt als Snack  
        - Ideal für unterwegs  

        Ergänze deine Box perfekt.
        """)

    st.markdown("---")

    st.markdown("<h2 class='neon'>🍱 Baue deine eigene Box</h2>", unsafe_allow_html=True)

    st.write("Stelle dir deine perfekte Full Day of Eating Box zusammen.")

    if st.button("🚀 Jetzt starten"):
        st.session_state.page = "Essensbox"


# -----------------------------------
# ESSENSBOX
# -----------------------------------
elif page == "Essensbox":

    st.markdown("<h1 class='neon'>🍱 Deine Fitness Box</h1>", unsafe_allow_html=True)

    st.image("shakes.jpg", use_column_width=True)

    st.markdown("## 🎯 Ziel")

    ziel = st.selectbox("", ["Cutting", "Maintenance", "Bulking"])

    st.markdown("## 🥗 Komponenten")

    protein = st.selectbox("Protein", ["Hähnchen", "Rind", "Tofu", "Lachs"])
    carbs = st.selectbox("Carbs", ["Reis", "Nudeln", "Quinoa"])
    fats = st.selectbox("Fette", ["Avocado", "Nüsse"])

    extras = st.multiselect("Extras", [
        "Protein Shake",
        "Snack Bar",
        "Yogurt Bites"
    ])

    st.markdown("## 📦 Menge")

    meals = st.slider("Mahlzeiten pro Tag", 2, 6, 3)
    days = st.slider("Tage", 1, 7, 3)

    price = meals * days * 9

    st.markdown(f"## 💰 Preis: {price} €")

    st.markdown("## 📩 Vorbestellung")

    name = st.text_input("Name")
    email = st.text_input("E-Mail")

    if st.button("🔥 Vorbestellen"):
        if name and email:
            st.success("✅ Bestellung gespeichert (Demo)")
        else:
            st.error("Bitte alle Felder ausfüllen")


# -----------------------------------
# KALORIENRECHNER
# -----------------------------------
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
