import streamlit as st

# Page de présentation des modèles et des résultats
def app(df):
    st.title("Présentation des modèles et des résultats")

    st.write("Le but du projet étant de prédire l’émission de CO2 (en g/km), qui est une variable numérique continue, nous avons utilisé plusieurs algorithmes de type régression.")

    st.subheader('Algorithmes de Machine Learning')
    st.write("Tout d’abord, nous avons testé ces différents modèles de Machine Learning :")
    st.write("* Régression linéaire multiple avec l’ensemble des variables sélectionnées  \n* Régression linéaire multiple affinée à 5 variables  \n* Elastic Net  \n* Decision Tree  \n* Random Forest")
    
    st.subheader('Réseau de neurones')
    st.write("Nous nous sommes également intéressés aux modèles de Deep Learning \
        et nous avons construit un réseau de neurones adapté à notre problématique.  \n\
        Ce réseau est composé d’une première couche dense avec 32 neurones et une \
        fonction d’activation de type “Rectified Linear Unit” , puis d’une seconde \
        couche dense avec un unique neurone et une fonction d’activation de type linéaire.  \n\
        L’optimiseur utilisé est Adam et la fonction de perte est la MSE. Nous entraînons \
        notre réseau sur 30 époques avec une taille de batch de 64.")

    st.subheader('Résultats obtenus')
