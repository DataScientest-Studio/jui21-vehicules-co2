import streamlit as st
import matplotlib.pyplot as plt
import os

# Page d'introduction
def app(df, dir_path):
    st.title("Prédiction des émissions de CO2 par les véhicules homologués en France")
    
    # Affichage du logo du pojet
    logo = plt.imread(os.path.join(dir_path , "data\image_voiture.jfif"))
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.write("")
    with col2:
        st.image(logo)
    with col3:
        st.write("")


    st.subheader("Contexte")
    st.markdown("""
    Le réchauffement climatique et les moyens d'y faire face sont au cœur de toutes les préoccupations. 
    Le secteur des transports, reconnu aujourd'hui comme l'un des principaux émetteurs de CO2, fait l'objet de nombreuses 
    réformes et incitations pour diminuer son empreinte écologique.
    \nAinsi, déterminer quels sont les véhicules qui émettent le plus de CO2 nous semble important pour identifier 
    les caractéristiques techniques qui jouent un rôle dans la pollution.
    \nCela pourrait permettre de prévenir l’apparition sur le marché de nouveaux types de véhicules présentant un 
    ensemble de caractéristiques susceptibles de favoriser l’émission de CO2 et d’aggraver la pollution de l’air et le réchauffement climatique.""")


    st.subheader("Objectif du projet")
    st.markdown("L’objectif de ce projet est de réussir à prédire l’émission de CO2 des différents types de véhicules en se basant sur leurs caractéristiques techniques.")