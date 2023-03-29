import xml.etree.ElementTree as ET 
import random 

genres = ["comedy", "action", "thriller", "documentary"]
years = [1999,2021,2022,1780,2016,2017]


nr = int(input("How many movies to generate? "))

movies = ET.Element('movies') 

for i in range(nr):
    movie = ET.Element('movie') 
    name = ET.SubElement(movies, 'name') 
    name.text= "Movie " + str(i)
    year = ET.SubElement(movies, 'year') 
    year.text = str(years[random.randint(0, len(years) - 1)])
    genre = ET.SubElement(movies, 'genre') 
    genre.text = genres[random.randint(0, len(genres) - 1)	]

xml_send = ET.tostring(movies)

print(xml_send)
