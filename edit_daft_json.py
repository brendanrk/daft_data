import json

with open("dataset_2021_11_06_18_59_40_No15503.json") as fj:
    with open("dataset_daft_format.json", "w") as fw:
        with open("dataset_sales_pandas.json", "w") as fdp:
            data = json.load(fj)
            count = 0
            data_pandas = []
            for bit in data:
                bit['longitude'] = bit['point']['coordinates'][0]
                bit['latitude'] = bit['point']['coordinates'][1]
                bit['county'] = bit['title'].split(",")[-1].replace("Co.","").replace(" ","")
                bit['county'] = ''.join(i for i in bit['county'] if not i.isdigit())
                bit['price (int)'] = ''.join(i for i in bit['price'].split("(")[-1] if i.isdigit())
                if bit['price (int)'] == "":
                    bit['price (int)'] = None
                else:
                    bit['price (int)'] = int(bit['price (int)'])
                if 'numBathrooms' in bit:
                    bit['baths (int)'] = int(''.join(i for i in bit['numBathrooms'] if i.isdigit()))
                else:
                    bit['baths (int)'] = None
                if 'numBedrooms' in bit:
                    bit['beds (int)'] = int(''.join(i for i in bit['numBedrooms'] if i.isdigit()))
                else:
                    bit['beds (int)'] = None
                if 'propertySize' in bit:
                    if "m" in bit['propertySize']:
                        bit['propertySize (m2)'] = float(''.join(i for i in bit['propertySize'] if (i.isdigit() and ord(i) < 128) or i =="."))
                    elif "a" in bit['propertySize']:
                        bit['propertySize (m2)'] = float(''.join(i for i in bit['propertySize'] if (i.isdigit() and ord(i) < 128) or i ==".")) * 4046.86
                    else:
                        print("what?", bit['propertySize'])
                else:
                    bit['propertySize (m2)'] = None
                if 'propertySize' in bit:
                    print(bit['propertySize'], bit['propertySize (m2)'])
                if 'ber' in bit:
                    if 'rating' in bit['ber']:
                        bit['ber.rating'] = bit['ber']['rating']
                    if 'epi' in bit['ber']:
                        bit['ber.epi'] = bit['ber']['epi']
                # fw.write(json.dumps(bit))
                # fw.write("\n")
                count += 1
                data_pandas.append(bit)
                # if count == 10000:
                #     break
            json.dump(data_pandas, fdp)