import csv
csv_reader = csv.reader(open("score.csv",encoding='utf-8'))
f = open('./data.csv', 'a+',encoding='utf-8',newline='')
csv_save=csv.writer(f)
for row in csv_reader:
    if len(row)==0:
        continue
    else:
        csv_save.writerow(row)