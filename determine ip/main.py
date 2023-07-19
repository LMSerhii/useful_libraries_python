import requests
import folium

from pyfiglet import Figlet


def get_info_by_ip(ip="127.0.0.1"):
    """  """
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()    # Запрос информации про IP
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[ORG]': response.get('org'),
            '[timezone]': response.get('timezone'),
            '[lat]': response.get('lat'),
            '[lon]': response.get('lon'),
            '[zip]': response.get('zip'),
            '[regionName]': response.get('regionName'),
            '[country]': response.get('country'),
        }

        for k, v in data.items():
            print(f"{k} - {v}")

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f"{response.get('query')}_{response.get('city')}.html")     # сохраняем карту в html

    except requests.exceptions.ConnectionError:
        print("Please enter your connection!")


def main():

    preview_text = Figlet(font='slant')
    print(preview_text.renderText("I P   I N F O"))  # выводим красивый шрифт

    ip = input("Please enter a target IP: ")
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()