import datetime

url = 'https://store.steampowered.com/search/?specials=1&os=win'
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init(autoreset=True)

now = datetime.datetime.now()
print(f"{Fore.YELLOW}{Style.BRIGHT}Scraped at: {now.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
print("-" * 60)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"{Fore.RED}{Style.BRIGHT}Failed to reach the URL: {e}{Style.RESET_ALL}")
    exit(1)

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
    print(f"{Fore.CYAN}{Style.BRIGHT}Title:{Style.RESET_ALL} {game['Title']}")
    print(f"{Fore.GREEN}Original Price:{Style.RESET_ALL} {game['Original Price']}")
    print(f"{Fore.RED}Final Price:{Style.RESET_ALL} {game['Final Price']}")
    print(f"{Fore.MAGENTA}Discount:{Style.RESET_ALL} {game['Discount']}")
    print(f"{Fore.BLUE}Link:{Style.RESET_ALL} {game['Link']}")
    print("-" * 60)

print(f"{Fore.YELLOW}{Style.BRIGHT}Total games found: {len(games_data)}{Style.RESET_ALL}")

with open('games_data.txt', 'w', encoding='utf-8') as file:
    file.write(f"Scraped at: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("-" * 60 + "\n\n")
    for game in games_data:
        file.write(f"Title: {game['Title']}\n")
        file.write(f"Original Price: {game['Original Price']}\n")
        file.write(f"Final Price: {game['Final Price']}\n")
        file.write(f"Discount: {game['Discount']}\n")
        file.write(f"Link: {game['Link']}\n")
        file.write("-" * 60 + "\n")
    
    file.write(f"Total games found: {len(games_data)}\n")
    file.write("Script by Adib - https://github.com/Adib23704/Steam-Offer-Scraper\n")

print(f"{Fore.GREEN}{Style.BRIGHT}Data has been saved to 'games_data.txt'.{Style.RESET_ALL}")
print(f"{Fore.WHITE}{Style.BRIGHT}Script by Adib - https://github.com/Adib23704/Steam-Offer-Scraper{Style.RESET_ALL}")
