import requests
import pandas
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def core_team_data(url):
    http_get_response = requests.get(url)
    soup = BeautifulSoup(http_get_response.text, 'lxml')
    base_url = url
    team_data = []
    team_members = soup.select('.speakers-list_item')
    for member in team_members:
        name_element = member.select_one('h3.speakers-list_item-heading')
        if name_element:
            role_element = name_element.find_next('div')
            image_element = member.select_one('img')
            image_src = urljoin(base_url, image_element['src'])
            core_team_member = {
                'name': name_element.text.strip(),
                'role': role_element.text.strip(),
                'image': image_src
            }
            team_data.append(core_team_member)
    return team_data


def save_to_csv(scraped_data, filename):
    df = pandas.DataFrame(scraped_data)
    df.to_csv(filename, index=False)
    

def save_to_json(scraped_data, filename):
    df = pandas.DataFrame(scraped_data)
    df.to_json(filename, orient='records', indent=2)


core_team_info = core_team_data('https://interaction24.ixda.org/')

save_to_csv(core_team_info, 'team_data.csv')
save_to_json(core_team_info, 'team_data.json')
