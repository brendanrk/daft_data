import requests
from pprint import pprint
import json
import datetime
current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

if __name__ == '__main__':
    daftset = []
    count = 0

    r = requests.post("https://search-gateway.dsch.ie/v1/listings", headers={
        "Content-Type": "application/json",
        "brand": "daft",
        "platform": "web"
    }, json={
        "section": "residential-to-rent",
        "paging":
            {
                "from": 0,
                "pageSize": "50"
            }
    },)
    res_json = r.json()
    totalPages = int(res_json["paging"]["totalPages"])
    totalResults = int(res_json["paging"]["totalResults"])
    nextFrom = int(res_json["paging"]["nextFrom"])
    print(res_json["paging"])
    for listing in res_json["listings"]:
        # print(count, listing["listing"]["publishDate"], listing["listing"]["title"])
        daftset.append(listing["listing"])
        count += 1
    for page in range(2, totalPages + 1):
        print("page", page, "nextFrom", nextFrom)
        r = requests.post("https://search-gateway.dsch.ie/v1/listings", headers={
            "Content-Type": "application/json",
            "brand": "daft",
            "platform": "web"
        }, json={
        "section": "residential-to-rent",
        "paging":
            {
                "from": nextFrom,
                "pageSize": "50"
            }
        },)
        res_json = r.json()
        nextFrom = int(res_json["paging"]["nextFrom"])
        print(res_json["paging"])
        for listing in res_json["listings"]:
            # print(count, listing["listing"]["publishDate"], listing["listing"]["title"])
            daftset.append(listing["listing"])
            count += 1
    with open('dataset_rent_{}_No{}.json'.format(current_time, totalResults), 'w') as f:
        json.dump(daftset, f)
