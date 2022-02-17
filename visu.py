import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page de visualisation des données
def app(df, data_path):
    st.title("Visualisation des données")
    st.markdown("""
    Cette page présente quelques visualisations choisies du jeu de données afin de mieux appréhender le lien 
    entre les variables, et plus particulièrement entre la variable cible et quelques variables importantes.
    """)

    st.subheader('Le jeu de données')

    st.markdown("""
    Les données proviennent de l’ADEME (Agence De l'Environnement et de la Maîtrise de l'Énergie) et sont 
    disponibles [ici](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_).
    \nElles recensent tous les véhicules commercialisés en France au cours de l’année 2014 et contiennent leurs principales 
    caractéristiques techniques ainsi que les consommations de carburant, les émissions de CO2 et les émissions de polluants dans l’air
    \nLe jeu de données contient 55 001 lignes et 14 colonnes après nettoyage. Chaque ligne représente un modèle de véhicule homologué, 
    chaque colonne contient une caractéristique technique ou une mesure. 
    \nVoici un aperçu des premières lignes de données :
    """)
    st.dataframe(df.head(8))


    st.subheader('Corrélations entre les variables')

    st.markdown("Voici la heatmap des corrélations :")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax, annot=True, cmap = 'magma')
    st.pyplot(fig)
    st.markdown("""
    On remarque que la variable cible est très corrélée avec les variables de consommations. Elle est également corrélée, 
    dans une moindre mesure, avec les variables de poids du véhicule.
    """)

    
    st.subheader("Corrélations avec la variable cible")
    
    st.write("Relation entre la puissance maximale et l'émission de CO2 :")
    fig = sns.lmplot(
        x='puiss_max',
        y='co2', data=df,
        line_kws={'color': 'red'},
        scatter_kws={'color' : 'blue', 's' : 10, 'alpha' : 0.3}
    )
    st.pyplot(fig)

    st.write("Relation entre la consommation extra-urbaine et l'émission de CO2 :")
    fig = sns.lmplot(
        x='conso_exurb',
        y='co2', data=df,
        line_kws={'color': 'red'},
        scatter_kws={'color' : 'blue', 's' : 10, 'alpha' : 0.3}
    )
    st.pyplot(fig)

    st.write("Relation entre la masse à vide et l'émission de CO2 :")
    fig = sns.lmplot(
        x='masse_ordma_min',
        y='co2', data=df,
        line_kws={'color': 'red'},
        scatter_kws={'color' : 'blue', 's' : 10, 'alpha' : 0.3}
    )
    st.pyplot(fig)

    st.write("Relation entre la gamme et l'émission de CO2 :")
    fig = sns.catplot(
        x = 'gamme',
        y = 'co2',
        data = df,
        order = ['ECONOMIQUE', 'INFERIEURE', 'MOY-INFER', 'MOY-SUPER', 'SUPERIEURE', 'LUXE'],
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)
