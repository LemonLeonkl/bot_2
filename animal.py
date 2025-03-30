import requests
def get_animal_image_url():    
        url = 'https://randomfox.ca/floof/'
        res = requests.get(url)
        data = res.json()
        return data['image']
