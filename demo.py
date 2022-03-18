import streamlit as st
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, ElasticNetCV
from sklearn.tree import DecisionTreeRegressor
from PIL import Image
import urllib.request

# Fonction pour pré-processer les données d'entraînement
@st.cache
def preprocess_data_train(df):

    # Séparation des variables explicatives dans un dataframe X et de la variable cible dans y
    y_train = df['co2']
    features = df.drop('co2', axis = 1)

    # OneHotEncoding pour les colonnes catégorielles
    col_cat = features.select_dtypes(include=['object', 'category']).columns.tolist()
    ohe = OneHotEncoder(sparse=False)

    # MinMaxScaling pour les colonnes numériques
    col_num = features.select_dtypes(include=['number']).columns.tolist()
    scaler = MinMaxScaler()

    # Application aux données avec un ColumnTransformer
    preprocessor = ColumnTransformer([
        ('cat', ohe, col_cat),
        ('num', scaler, col_num)
    ])
    X_train_scaled = preprocessor.fit_transform(features)
    
    return preprocessor, X_train_scaled, y_train

# Fonction pour pré-processer les données de test
def preprocess_data_test(soup, preprocessor):

    # Récupération de la masse
    masse = []
    for element in soup.select('.colR+ .b0 span~ span'):
        masse.append(element.text.strip().split()[0]) 

    # Récupération du co2
    co2 = []
    for element in soup.select('.colR:nth-child(10) span~ span'):
        co2.append(element.text.strip().split()[0])

    # Récupération de la conso mixte
    conso_mixte = []
    for element in soup.select('.colL:nth-child(9) span:nth-child(6)'):
        conso_mixte.append(element.text.strip().split()[0])
        
    # Récupération de la puissance
    puissance = []
    for element in soup.select('span+ .clear span'):
        puissance.append(element.text.strip().split()[0])    
        
    # Récupération de la marque
    marque = []
    for element in soup.select('.lH35'):
        marque.append(element.text.strip().split()[2].upper())    # Upper > pour passer en majuscule

    # Création du DataFrame
    X_test_user = pd.DataFrame(list(zip(marque,puissance,conso_mixte,masse,co2)), columns=["lib_mrq","puiss_max","conso_mixte","masse_ordma_min","co2"])
    
    # On vérifie qu'il ne manque pas de données dans les variables récupérées
    for col1,col2,col3,col4,col5 in zip(X_test_user['lib_mrq'].values,X_test_user['puiss_max'].values,X_test_user['conso_mixte'].values,X_test_user['masse_ordma_min'].values,X_test_user['co2'].values) : 
        if (col1=='NC') | (col2=='NC') | (col3=='NC') | (col4=='NC') | (col5=='NC') :
            X_test_user = pd.DataFrame()
        else :
            X_test_user = X_test_user.astype({"puiss_max":'float64', "conso_mixte":'float64', 'co2' :'float64', 'masse_ordma_min' : 'int64' })
 

    # Transformations des données grâce au ColumnTransformer
    if not X_test_user.empty :
        X_test_scaled = preprocessor.transform(X_test_user)
    else :
        X_test_scaled = np.array([])
    
    return X_test_scaled, co2


# Fonction pour créer et entraîner le modèle choisi
@st.cache
def fit_model(option_modele, X_train, y_train):

    # Création du modèle choisi
    if(option_modele == 'Régression linéaire') :
        clf = LinearRegression()
    elif(option_modele == 'Elastic Net') :
        clf = ElasticNetCV(l1_ratio = (0.1, 0.5, 0.8, 0.9, 0.99), alphas=(0.001, 0.01, 0.1, 0.5, 1.0), cv = 10)
    else :
        clf = DecisionTreeRegressor()

    # Entraînement du modèle
    clf.fit(X_train, y_train)

    return clf


# Page de démonstration
def app(df, data_path):
    st.title("Démonstration")
    st.markdown("""
    Sur cette page, vous pouvez saisir l'URL d'une page du site internet "LaCentrale" correspondant à la fiche technique d'un véhicule.
    Vous pouvez également choisir un modèle de Machine Learning.
    \nSi toutes les données nécessaires sont disponibles dans la fiche technique, le modèle sélectionné effectuera une prédiction de 
    l'émission de CO2 émise par le véhicule choisi.
    """)

    # Suppression des variables de mesure de pollution, de la puissance administrative 98, des consommations urb et exurb, de la masse max et du type de carrosserie et gamme
    df_reduit = df.drop(['co_typ_1', 'nox', 'ptcl', 'puiss_admin_98', 'conso_urb', 'conso_exurb', 'masse_ordma_max', 'Carrosserie', 'gamme'], axis = 1)

    # Choix de la page à scrapper par l'utilisateur
    st.subheader('Choix du véhicule')
    choix_page = st.text_input("Saisir l'URL de la page à scrapper sur le site de la Centrale\
    (attention à bien choisir une page contenant les caractéristiques techniques d'un véhicule) :",
    'https://www.lacentrale.fr/fiche-technique-voiture-citroen-berlingo-ii+1.6+e_hdi+90+airdream+collection+etg6-2014.html')
    # URL de la page technique saisie par l'utilisateur
    page_LC = urlopen(choix_page)
    soup = BeautifulSoup(page_LC, 'html.parser')

    # Choix du modèle par l'utilisateur
    st.subheader('Choix du modèle de Machine Learning')
    option_modele = st.selectbox('Sélectionner le modèle à tester :', ('Régression linéaire', 'Elastic Net', 'Arbre de décision'))

    # Pré-processing des données d'entraînement
    preprocessor, X_train_scaled, y_train = preprocess_data_train(df_reduit)

    # Pré-processing des données de test
    X_test_scaled, co2_test = preprocess_data_test(soup, preprocessor)

    # Affichage des résultats
    st.subheader('Résultat prédit par le modèle')
    st.write("Vous avez choici ce véhicule :")

    # Récupération de l'image du véhicule
    image_tags = soup.find_all('img', class_='noBold italic block max100 imgModelCom' )
    links=[]
    for image_tag in image_tags :
        links.append(image_tag['src'])
    urllib.request.urlretrieve(links[0], ".jpg")
    # Affichage
    dimensions = (260, 370)
    i = Image.open('.jpg')
    i.thumbnail(dimensions)
    st.image(i)

    # On fait tourner le modèle si les données récupérées sont ok
    if X_test_scaled.size != 0 :
        # Création et entraînement du modèle
        clf = fit_model(option_modele, X_train_scaled, y_train)

        # Prédiction du modèle
        y_pred = clf.predict(X_test_scaled)
        st.write("L'émission de CO2 prédite par ce modèle pour ce type de véhicule est :", round(y_pred.item(),2), "g/km.")
        st.write("L'émission de CO2 réelle (donnée sur la fiche technique du site \"LaCentrale\" ) est :", co2_test[0], "g/km.")
    
    else :
        st.warning("Il manque des données sur cette page ! Impossible de réaliser une prédiction.")