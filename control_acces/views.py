from django.shortcuts import render

import folium
from folium import plugins

from django.views.generic import TemplateView
# Create your views here.
'''
def Control_acces(request):
    context={}
    return render(request,'control_acces/control_acces.html',context)
'''

class FoliumView(TemplateView):
    template_name = "control_acces/control_acces.html"

    def get_context_data(self, **kwargs):
        # définir les villes dans la carte
        villes={
        'Brest' : (48.3885,-4.4841),
        "Paris": (48.8550,2.3542),
        "Rabat":(34.0169,-6.8019)}

        locations = [[5.22252,-52.77741],
                 [5.22287,-52.78058],
                 [5.22431,-52.78165],
                 [5.22624,-52.78087],
                 [5.22604,-52.77859],
                 [5.2282,-52.7781],
                 [5.2272,-52.7756],
                 [5.2256,-52.7762],
                 [5.22358,-52.77628],
                 [5.22252,-52.77741]
                 ]
        ports={
        'E' : [5.22766,-52.77771],
        "D": [5.22640,-52.77815],
        'C':[5.22612,-52.77661],
        'B':[5.2238,-52.7767],
        'A':[5.2230,-52.7779]
        }

        # Créer un object figure
        figure = folium.Figure()
        # Posionner la carte sur Guyane
        m = folium.Map(location=[5.2254,-52.7773],width='60%', height='70%', 
        left='22%', top='0%',zoom_start=16,control_scale=True)
        m.add_to(figure)
        # Afficher les villes
        for ville, coords in villes.items():
            folium.Marker(coords, popup=f'<b>{ville}</b><br>{coords}',
            tooltip=ville,
            icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
        # Créer un cercle dans la carte
        #folium.CircleMarker( location=[5.22370,-52.77830], radius=12, fill=False ,weight=5,).add_to(m)
        # Controler les couches sur la carte 
        folium.raster_layers.TileLayer('OpenStreetMap').add_to(m)
        folium.raster_layers.TileLayer('CartoDB positron').add_to(m)
        folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
        folium.raster_layers.TileLayer('Mapbox Bright').add_to(m)
        folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
        folium.LayerControl().add_to(m)
        # Ajouter Geocoder
        #plugins.Geocoder().add_to(m)
        # Géolocaliser l'utilisateur.
        folium.plugins.LocateControl().add_to(m)
        # Trace un rectangle
        #folium.vector_layers.Rectangle
        folium.vector_layers.Polygon(locations=locations, tooltip='Centre Spatial Guyannais').add_to(m)
        #
        for  port_name, port in ports.items():
            folium.vector_layers.Circle(location=port,radius=30, tooltip=port_name,color='#ff3333').add_to(m)
            folium.Marker(port, popup=f'<b>{port}</b><br>Port {port_name}',
            tooltip=port_name,
            icon=folium.Icon(color="orange",icon="wrench", prefix='fa')
            ).add_to(m)
        # "user-times" and "user-o" , "wrench"
        figure.render()
        return {"control_acces": figure}