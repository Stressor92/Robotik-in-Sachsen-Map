# Robotik-in-Sachsen-Map
Config files for my GitHub profile.
folium Map in Python, dass ein html File mit einer Sachsenkarte zu Akteuren im Robotikbereich erstellt
das Excelfile "map" wird genutzt mit den Spalten: 
  Name=Mouseover 
  Beschreibung + Website = Popup  
  latitute, logitute = Koordinanten    
  icon = icon von https://fontawesome.com, wird über die Kategorie bestimmt
um die Marker auf der Map zu erstellen
Das Excelfile Geocode wird mit einem Script genutzt, um die Koordinanten zu erstellen
Die geojson Datei beschreibt die Ländergrenzen von Sachsen, und legt eine Ebene auf die Map
Der Pythoncode erstellt die Map als html 

Zur individuellen nutzung: 
- Excel "Map" anpassen mit anderen Akteuren/Betrieben/Markern/icons
- kreis3.geojson mit einem anderen Gebiet austauschen, wenn etwas anderes Markiert werden soll, wenn es nicht Sachsen sein soll
