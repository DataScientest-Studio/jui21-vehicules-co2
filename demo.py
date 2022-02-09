import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, ElasticNetCV
from sklearn.tree import DecisionTreeRegressor

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
@st.cache
def preprocess_data_test(preprocessor, X_test):

    # Transformations des données grâce au ColumnTransformer
    X_test_scaled = preprocessor.transform(X_test)
    
    return X_test_scaled


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
def app(df):
    st.title("Démonstration")

    # Suppression des variables de mesure de pollution, de la puissance administrative 98, des consommations urb et exurb et de la masse max
    df_reduit = df.drop(['co_typ_1', 'nox', 'ptcl', 'puiss_admin_98', 'conso_urb', 'conso_exurb', 'masse_ordma_max'], axis = 1)

    # Choix des variables par l'utilisateur
    st.subheader('Choix des variables')
    option_marque = st.selectbox('Sélectionnez la marque du véhicule :', df['lib_mrq'].unique(), 0)
    option_carrosserie = st.selectbox('Sélectionnez le type de carrosserie du véhicule :', df['Carrosserie'].unique(), 0)
    option_gamme = st.selectbox('Sélectionnez la gamme du véhicule :', df['gamme'].unique(), 0)
    option_puiss = st.slider('Sélectionnez la puissance du véhicule :', int(df['puiss_max'].min()), int(df['puiss_max'].max()), 147)
    option_conso = st.slider('Sélectionnez la consommation moyenne du véhicule :', int(df['conso_mixte'].min()), int(df['conso_mixte'].max()), 8)
    option_masse = st.slider('Sélectionnez la masse à vide du véhicule en kg :', int(df['masse_ordma_min'].min()), int(df['masse_ordma_min'].max()), 1505)

    # Choix du modèle par l'utilisateur
    st.subheader('Choix du modèle')
    option_modele = st.selectbox('Sélectionnez le modèle à tester :', ('Régression linéaire', 'Elastic Net', 'Arbre de décision'))

    # Pré-processing des données d'entraînement
    preprocessor, X_train_scaled, y_train = preprocess_data_train(df_reduit)

    # Pré-processing des données de test
    liste_col = df_reduit.columns.to_series().drop('co2')
    liste_val = np.array([option_marque, option_puiss, option_conso, option_masse, option_carrosserie, option_gamme])
    X_test_user = pd.DataFrame([liste_val], columns = liste_col)
    X_test_scaled = preprocess_data_test(preprocessor, X_test_user)

    # Création et entraînement du modèle
    clf = fit_model(option_modele, X_train_scaled, y_train)

    # Prédiction du modèle
    st.subheader('Résultat prédit par le modèle')
    y_pred = clf.predict(X_test_scaled)
    st.write("L'émission de CO2 prédite par ce modèle pour ce type de véhicule est : ", round(y_pred.item(),2))