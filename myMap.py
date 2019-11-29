import folium
import pandas



data = pandas.read_excel("Italy.xlsx", sheet_name=1)

nam = list(data["Name"])
lat = list(data["Latitude"])
log = list(data["Longitute"])
pho1 = list(data["Photo1"])
desc1 = list(data["Dscrp1"])
pho2 = list(data["Photo2"])
desc2 = list(data["Dscrp2"])
pho3 = list(data["Photo3"])
desc3 = list(data["Dscrp3"])

# print(nam)
# print(pho1)
# print(desc1)

my_map = folium.Map(location=[40, 15], zoom_start=7, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")



for name, lati, logi, photo1, description1, photo2, description2, photo3, description3 in zip(nam, lat, log, pho1, desc1, pho2, desc2, pho3, desc3):
    fg.add_child(folium.Marker(location=[lati, logi],
    popup= """<h3 style="color:darkred"><strong>""" + name +  """</strong></h3>""" + " " + 
    
    """<div id="my-pics" class="carousel slide" data-ride="carousel" style="width:500px;margin:auto;">


            <ol class="carousel-indicators">
            <li data-target="#my-pics" data-slide-to="0" class="active"></li>
            <li data-target="#my-pics" data-slide-to="1"></li>
            <li data-target="#my-pics" data-slide-to="2"></li>
            </ol>


            <div class="carousel-inner" role="listbox">


            <div class="item active">
            <p>""" + description1 + """ </p>
            <img src=""" + photo1 + """>
            </div>


            <div class="item">
            <p>""" + description2 + """ </p>
            <img src=""" + photo2 + """>
            </div>


            <div class="item">
            <p>""" + description3 + """ </p>
            <img src=""" + photo3 + """>
            
            </div>

           
            </div>


            <a class="left carousel-control" href="#my-pics" role="button" data-slide="prev">
            <span class="icon-prev" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#my-pics" role="button" data-slide="next">
            <span class="icon-next" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
            </a>

            </div>""",

    icon=folium.Icon(color='darkred')))


my_map.add_child(fg)

my_map.save("My_map.html")









