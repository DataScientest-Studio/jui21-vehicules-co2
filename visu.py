import streamlit as st
from math import pi
from bokeh.plotting import figure
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource, BasicTicker, ColorBar, LinearColorMapper
from bokeh.palettes import Magma256
from bokeh.transform import transform

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
    # Preparation des donnees au bon format pour bokeh
    correlation = df.corr()
    correlation.index.name = 'AllColumns1'
    correlation.columns.name = 'AllColumns2'
    correlation = correlation.stack().rename("value").reset_index()
    source0 = ColumnDataSource(correlation)

    # Instanciation d'un outil HoverTool
    h0 = HoverTool(tooltips = [("coef de correlation", "@value")])

    # Preparation des couleurs
    mapper = LinearColorMapper(palette=Magma256, low=-1, high=1)

    # Graphique
    p0 = figure(plot_width=700, plot_height=500,
        x_range=list(correlation.AllColumns1.drop_duplicates()),
        y_range=list(correlation.AllColumns2.drop_duplicates()))
    p0.rect(x="AllColumns1", y="AllColumns2",
        width=1, height=1,
        source=source0,
        line_color=None,
        fill_color=transform('value', mapper))

    # Legende
    color_bar = ColorBar(
        color_mapper=mapper,
        ticker=BasicTicker(desired_num_ticks=10))
    p0.add_layout(color_bar, 'right')
    p0.xaxis.major_label_orientation = pi/4
    p0.yaxis.major_label_orientation = pi/4
    p0.add_tools(h0)
    st.bokeh_chart(p0)

    st.markdown("""
    On remarque que la variable cible est très corrélée avec les variables de consommations. Elle est également corrélée, 
    dans une moindre mesure, avec les variables de masses et de puissances du véhicule.
    """)

    
    st.subheader("Corrélations avec la variable cible")
    
    st.write("Relation entre la puissance maximale et l'émission de CO2 :") 
    # Conversion des données pour bokeh
    source1 = ColumnDataSource(df)
    # Instanciation d'un outil HoverTool
    h1 = HoverTool(tooltips = [("puissance max", "@puiss_max"), 
                            ("co2", "@co2"),
                            ("marque", "@lib_mrq")])
    # Graphique
    p1 = figure(plot_width=600, plot_height=350)     
    p1.circle(x='puiss_max', y='co2', source = source1, alpha=0.2 )
    p1.xaxis.axis_label = "Puissance maximale (kW)"              
    p1.yaxis.axis_label = "CO2 (g/km)"              
    p1.add_tools(h1)
    st.bokeh_chart(p1)

    st.write("Relation entre la consommation extra-urbaine et l'émission de CO2 :")
    # Conversion des données pour bokeh
    source2 = ColumnDataSource(df)
    # Instanciation d'un outil HoverTool
    h2 = HoverTool(tooltips = [("conso extra urbaine", "@conso_exurb"), 
                            ("co2", "@co2"),
                            ("marque", "@lib_mrq")])
    # Graphique
    p2 = figure(plot_width=600, plot_height=350)     
    p2.circle(x='conso_exurb', y='co2', source = source2, alpha=0.2)    
    p2.xaxis.axis_label = "Consommation extra-urbaine (L)"              
    p2.yaxis.axis_label = "CO2 (g/km)"
    p2.add_tools(h2)
    st.bokeh_chart(p2)

    st.write("Relation entre la masse à vide et l'émission de CO2 :")
    # Conversion des données pour bokeh
    source3 = ColumnDataSource(df)
    # Instanciation d'un outil HoverTool
    h3 = HoverTool(tooltips = [("poids en ordre de marche mini", "@masse_ordma_min"), 
                            ("co2", "@co2"),
                            ("marque", "@lib_mrq")])
    # Graphique
    p3 = figure(plot_width=600, plot_height=350)     
    p3.circle(x='masse_ordma_min', y='co2', source = source3, alpha=0.2)    
    p3.xaxis.axis_label = "Masse à vide (kg)"              
    p3.yaxis.axis_label = "CO2 (g/km)"              
    p3.add_tools(h3)
    st.bokeh_chart(p3)

    st.write("Relation entre la gamme et l'émission de CO2 :")
    # Conversion des données pour bokeh
    source4 = ColumnDataSource(df)
    liste_gammes = ['ECONOMIQUE', 'INFERIEURE', 'MOY-INFER', 'MOY-SUPER', 'SUPERIEURE', 'LUXE']
    # Instanciation d'un outil HoverTool
    h4 = HoverTool(tooltips = [("gamme", "@gamme"), 
                            ("co2", "@co2"),
                            ("marque", "@lib_mrq")])
    # Graphique
    p4 = figure(plot_width=600, plot_height=350, x_range = liste_gammes)
    p4.circle(x='gamme', y='co2',  source = source4, alpha=0.2)
    p4.xaxis.axis_label = "Gamme"              
    p4.yaxis.axis_label = "CO2 (g/km)"              
    p4.add_tools(h4)
    st.bokeh_chart(p4)
