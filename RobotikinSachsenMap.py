# Bibliotheken importieren
import folium
import pandas as pd

# Exceltabelle importieren
df = pd.read_excel(r'E:\Programmierung\RobotikinSachsen\RobotikinSachsenMap\map.xlsx')
#df.fillna(0)                                        #NaN Values zu 0
#df['latitude'] = pd.to_numeric(df['latitude'])      #Spalte latitude Datenformat Zahl
#df['longitude'] = pd.to_numeric(df['longitude'])    #Spalte logitude Datenformat Zahl
#df=df.dropna(subset=['longitude'])                  #NaN Values löschen
#df=df.dropna(subset=['latitude'])                   #NaN Values löschen

# Map erstellen mit Wilsdruff als Zentrum
m = folium.Map(location=[51.0503651, 13.5363349],
               zoom_start=9,
               tiles='OpenStreetMap'
               )
# geojson file importieren
kreisSachsen = f"E:\Programmierung\RobotikinSachsen\RobotikinSachsenMap\kreis3.geojson"
folium.GeoJson(kreisSachsen,
               name='Kreis Sachsen')
# geojson file zur Map hinzufügen
folium.Choropleth(
    geo_data=kreisSachsen,
    fill_opacity=0.2,
    line_opacity=0.6,
    fill_color='#baff00',
    legend_name='Kreis Sachsen',
    name='Landkreise'
).add_to(m)

# Layer auswählbar machen
folium.LayerControl().add_to(m)

# Costum Logo erstellen
# iconXXX = folium.features.CustomIcon(
#    'E:\Programmierung\RobotikinSachsen\RobotikinSachsenMap\XXX.png',
#    icon_size=(30,30)
# )

# Marker erstellen und über alle Punkte in der Excel iterieren
i = 1
while i <= df.shape[0]:
    folium.Marker(
        location=[df['longitude'].iloc[i-1], df['latitude'].iloc[i-1]],
        tooltip=(df['Name'].iloc[i-1]),
        popup=(df['Beschreibung'].iloc[i-1]),
        icon=folium.Icon(
            color='orange',
            icon_color='white',
            icon=df['icon'].iloc[i-1],
            prefix='fa')
    ).add_to(m)
    i += 1


# Map als html speichern
m.save('E:\Programmierung\RobotikinSachsen\RobotikinSachsenMap\RobotikinSachsen.html')


