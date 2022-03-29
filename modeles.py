import streamlit as st
import matplotlib.pyplot as plt
import os

# Page de présentation des modèles et des résultats
def app(df, dir_path):
    st.title("Présentation des modèles")

    st.markdown("""
    Le but du projet étant de prédire l’émission de CO2 (en g/km), qui est une variable numérique
    continue, nous avons utilisé plusieurs algorithmes de type régression.
    """)

    st.subheader('Algorithmes de Machine Learning')
    st.markdown("""
    Dans un premier temps, nous avons testé ces différents modèles de Machine Learning :
    * Régression linéaire multiple avec l’ensemble des variables sélectionnées  
    * Régression linéaire multiple affinée à 5 variables  
    * Elastic Net  
    * Decision Tree  
    * Random Forest
    """)
    
    st.subheader('Réseau de neurones')
    st.markdown("""
    Nous nous sommes également intéressés aux modèles de Deep Learning 
    et nous avons construit un réseau de neurones adapté à notre problématique.  
    \nCe réseau est composé d’une première couche dense avec 32 neurones et une 
    fonction d’activation de type “Rectified Linear Unit” , puis d’une seconde 
    couche dense avec un unique neurone et une fonction d’activation de type linéaire.  
    \nL’optimiseur utilisé est Adam et la fonction de perte est la MSE. Nous entraînons 
    notre réseau sur 30 époques avec une taille de batch de 64.
    """)

    st.title("Performance des modèles")

    st.subheader('Comparaison des R² et RMSE')
    st.markdown("""
    Pour mesurer la performance de tous nos modèles et pouvoir les comparer entre eux,
    nous avons utilisé deux métriques :
    * le coefficient de détermination R², afin d’avoir une idée de la proportion de variance expliquée par le modèle, et savoir si l’ajustement du modèle est de bonne qualité.
    * la RMSE, qui représente l'écart type des résidus produits par notre modèle et peut être interprétée dans les mêmes unités que notre cible, l’émission de CO2. Nous avons préféré cette mesure à la MAE afin de bien prendre en compte les valeurs aberrantes pendant le processus d'ajustement.
    """)
    st.markdown("""
    Voici ci-dessous les résultats obtenus sur le jeu de test pour les différents modèles :
    """)
    resultats = plt.imread(os.path.join(dir_path , "data\Perfo_modeles.JPG"))
    st.image(resultats)

    st.subheader('Comparaison des émissions de CO2 réelles et prédites')
    st.markdown("""
    Une autre façon de mesurer la performance des modèles est de visualiser l'émission de CO2 prédite en fonction 
    de l'émission réelle. Plus on obtient de points le long de la droite y = x (représentée en rouge ci-dessous) et 
    plus le modèle est performant.
    \nVoici le graphique réalisé à partir des prédictions du modèle Random Forest :
    """)
    comparaison = plt.imread(os.path.join(dir_path , "data\Comparaison_CO2_reel_predit.JPG"))
    st.image(comparaison)
    st.markdown("""
    On constate que les points se trouvent majoritairement le long de la ligne y = x, 
    ce qui confirme les bons résultats obtenus par le calcul des R² et RMSE.
    """)