import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Trafic aérien mondial", layout="wide")
st.title("✈️ Trafic aérien mondial")

# --- Chargement des données ---
@st.cache_data  # évite de re-télécharger à chaque interaction
def load_data():
    url = "https://ourworldindata.org/grapher/number-airline-passengers.csv?v=1&csvType=full&useColumnShortNames=false"
    df = pd.read_csv(url, storage_options={'User-Agent': 'Streamlit app - personal project'})
    return df

df = load_data()

# Renommer la colonne longue pour plus de simplicité dans le code
df = df.rename(columns={"Air transport, passengers carried": "Passengers"})

# --- Séparer pays réels et agrégats (World, continents...) ---
# Les vrais pays ont un Code ISO à 3 lettres ; les agrégats (World, Europe...) ont un Code vide ou différent
df_countries = df[df["Code"].notna() & (df["Code"].str.len() == 3)]

# --- Sidebar : filtres ---
st.sidebar.header("Filtres")

all_entities = sorted(df["Entity"].unique())
selected_entities = st.sidebar.multiselect(
    "Choisir un ou plusieurs pays / régions",
    options=all_entities,
    default=["World"] if "World" in all_entities else all_entities[:1]
)

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())
year_range = st.sidebar.slider(
    "Période",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# --- Filtrer les données selon la sélection ---
df_filtered = df[
    (df["Entity"].isin(selected_entities)) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

# --- Graphique principal ---
st.subheader("Évolution du nombre de passagers dans le temps")

# Événements marquants à annoter sur le graphique
events = [
    {"year": 2001, "label": "11 septembre"},
    {"year": 2008, "label": "Crise financière"},
    {"year": 2020, "label": "COVID-19"},
]

if df_filtered.empty:
    st.warning("Aucune donnée pour cette sélection.")
else:
    fig_line = px.line(
        df_filtered,
        x="Year",
        y="Passengers",
        color="Entity",
        labels={"Passengers": "Passagers", "Year": "Année", "Entity": "Pays / région"}
    )

    # Ajouter une ligne verticale + annotation pour chaque événement,
    # uniquement s'il tombe dans la période sélectionnée
    for event in events:
        if year_range[0] <= event["year"] <= year_range[1]:
            fig_line.add_vline(
                x=event["year"],
                line_dash="dash",
                line_color="gray",
                opacity=0.6
            )
            fig_line.add_annotation(
                x=event["year"],
                yref="paper",
                y=1.02,
                text=event["label"],
                showarrow=False,
                font=dict(size=11, color="gray"),
                textangle=0
            )

    fig_line.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(fig_line, use_container_width=True)

# --- Aperçu des données filtrées ---
with st.expander("Voir les données brutes filtrées"):
    st.dataframe(df_filtered)

# --- Carte du monde interactive ---
st.subheader("Carte mondiale du trafic aérien")

map_year = st.slider(
    "Choisir une année pour la carte",
    min_value=min_year,
    max_value=max_year,
    value=max_year,
    key="map_year"  # nécessaire car on a déjà un slider "year_range" plus haut
)

df_map = df_countries[df_countries["Year"] == map_year]

fig = px.choropleth(
    df_map,
    locations="Code",
    color="Passengers",
    hover_name="Entity",
    color_continuous_scale="Blues",
    projection="natural earth",
    title=f"Passagers transportés par pays en {map_year}",
    labels={"Passengers": "Passagers"}
)
fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))

st.plotly_chart(fig, use_container_width=True)