import requests
from bs4 import BeautifulSoup


URL = 'https://only.digital/'


def parse_url(url):
    try:
        url_response = requests.get(url)
        url_response.raise_for_status()
        soup = BeautifulSoup(url_response.text, 'html.parser')
        assert soup.find('footer'), "Футер не найден"
        assert soup.find('div', class_='sc-222969c7-5 dHBZCP'), "Контакты не найдены"
        print("Футер и контакты успешно найдены")
        return soup.find('footer')
    except requests.RequestException as e:
        assert False, f"Ошибка при запросе к URL: {e}"
    finally:
        print("Проверки выполнены")


result = parse_url(URL)
if result:
    print("Текст найденного футера:", result.text)
else:
    print("Не удалось найти футер.")