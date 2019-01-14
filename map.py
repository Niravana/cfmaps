import pandas as pd 
import folium

def main():
	m = folium.Map(location = [40.0150, -105.2705],zoom_start=6,tiles='Mapbox bright')
	folium.Marker(location = [36.311005, -94.127434], popup = 'Providence').add_to(m)
	m

main()

