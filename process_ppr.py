import csv

with open("PPR-ALL.csv") as f:
    with open("PPR-ALL_format1.csv","w", newline="") as fw:
        csvdata = csv.reader(f)
        csvwriter = csv.writer(fw)
        headers = next(csvdata)
        headers.append("price (int)")
        print("headers", headers)
        count = 0
        csvwriter.writerow(headers)
        for row in csvdata:
            row.append(''.join(i for i in row[4] if i.isdigit() or i =="."))
            print(row)
            csvwriter.writerow(row)
            count += 1
            # if count == 10000:
            #     break
            # writer.writerow(row)