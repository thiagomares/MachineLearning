import requests
from PIL import Image

key = 'Kinv0DCxdefhPpukvoI7NmuqeRNvsLPnVlqXDRmS'

url = f'https://api.nasa.gov/planetary/apod?api_key={key}'

r = requests.get(url=url)

img = Image.OPEN

# show a image from astronomic photo of day?'