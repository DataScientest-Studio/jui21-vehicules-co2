import streamlit as st

# Page de présentation des modèles et des résultats
def app(df, data_path):
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
