# ✈️ Trafic aérien mondial

Application interactive de visualisation du transport aérien mondial (nombre de passagers transportés) par pays et par période, de 1970 à aujourd'hui.

🔗 **[Voir l'application en ligne](https://app-test-kylian.streamlit.app/)** 

## Aperçu

<img width="1907" height="950" alt="image" src="https://github.com/user-attachments/assets/f344b639-371a-40ef-a363-27848bd95c01" />

## Fonctionnalités

- 📈 **Évolution temporelle** : courbe du nombre de passagers par pays/région, filtrable par période, avec annotation des événements marquants (11 septembre 2001, crise financière 2008, COVID-19)
- 🗺️ **Carte interactive** : visualisation choroplèthe du trafic aérien par pays pour une année donnée
- 🎛️ **Filtres dynamiques** : sélection multiple de pays/régions et de période via une barre latérale

## Données

Les données proviennent de [Our World in Data](https://ourworldindata.org/grapher/number-airline-passengers), issues de l'Organisation de l'aviation civile internationale (OACI) via la Banque Mondiale. Elles couvrent la période 1970–2023 et comptabilisent les passagers domestiques et internationaux des compagnies aériennes enregistrées dans chaque pays.

## Stack technique

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — interface et déploiement
- [Pandas](https://pandas.pydata.org/) — traitement des données
- [Plotly](https://plotly.com/python/) — visualisations interactives

## Lancer le projet en local

```bash
# Cloner le dépôt
git clone https://github.com/Kyky25/trafic-aerien-mondial.git
cd trafic-aerien-mondial

# Créer et activer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # sous Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

L'application s'ouvre ensuite sur `http://localhost:8501`.

## Pistes d'amélioration

- Ajouter le nombre d'avions en circulation en temps réel (API OpenSky Network)
- Classement top 10 des pays par période
- Échelle logarithmique sur la carte pour mieux contraster les pays à trafic modéré

## Auteur

*Kylian GRENIER*
