from fake_useragent import UserAgent
import requests
import json
import time

fagent = UserAgent()


# print(fagent.random)


def collect_data():
    # response = requests.get(
    #     url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=0&type=2&withStack=true',
    #     headers={'user-agent': f'{fagent.random}'}
    # )
    #
    # with open('source.json', 'w') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    offset = 0
    step_size = 60
    source = []
    count = 0

    while True:
        for element in range(offset, offset + step_size, 60):
            # max_offset=8922
            # price = 1500
            #w
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1500&offset={element}&type=13&withStack=true'
            response = requests.get(
                url=url,
                headers={'user-agent': f'{fagent.random}'}
            )
            time.sleep(2.454545443332111)
            offset += step_size

            data = response.json()
            items = data.get('items')

            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    items_full_name = i.get('fullName')
                    items_3d_view = i.get('3d')
                    items_price = i.get('price')
                    items_overprice = i.get('overprice')

                    source.append(
                        {
                            'item_fullname': items_full_name,
                            'item_url': items_3d_view,
                            'item_price': items_price,
                            'item_overprice': items_overprice
                        }
                    )

        count += 1
        print(f'Page #{count}')
        print(url)

        if len(items) < 60:
            break

        with open('gloves.json', 'w') as file:
            json.dump(source, file, indent=4, ensure_ascii=False)

        print(len(source))


def main():
    collect_data()




if __name__ == "__main__":
    main()
