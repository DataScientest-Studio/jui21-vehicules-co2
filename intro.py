import streamlit as st

# Page d'introduction
def app(df):
    st.title("Prédiction des émissions de CO2 par les véhicules homologués en France")
    
    st.subheader("Contexte")
    st.markdown("Le réchauffement climatique et les moyens d'y faire face sont au cœur de toutes les préoccupations. Le secteur des transports, reconnu aujourd'hui comme l'un des principaux émetteurs de CO2, fait l'objet de nombreuses réformes et incitations pour diminuer son empreinte écologique.")
    st.markdown("Ainsi, déterminer quels sont les véhicules qui émettent le plus de CO2 est important pour identifier les caractéristiques techniques qui jouent un rôle dans la pollution.")
    
    st.subheader("Objectif")
    st.markdown("L’objectif de ce projet est de réussir à prédire l’émission de CO2 des différents types de véhicules en se basant sur leurs caractéristiques techniques.")