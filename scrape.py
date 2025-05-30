url = 'https://store.steampowered.com/search/?specials=1&os=win'
import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

games_data = []

for game_item in soup.find_all('a', class_='search_result_row'):
    title = game_item.find('span', class_='title').text if game_item.find('span', class_='title') else 'Title Not Available'
    
    link = game_item.get('href', 'No link found')
        
    original_price = game_item.find('div', class_='discount_original_price').text if game_item.find('div', class_='discount_original_price') else 'Price Not Available'
    final_price = game_item.find('div', class_='discount_final_price').text if game_item.find('div', class_='discount_final_price') else 'Price Not Available'
    
    discount = game_item.find('div', class_='discount_pct').text if game_item.find('div', class_='discount_pct') else 'Discount Not Available'
    
    games_data.append({
        'Title': title,
        'Link': link,
        'Original Price': original_price,
        'Final Price': final_price,
        'Discount': discount
    })

for game in games_data:
    print(game)