car1 = {
  "brand": "Corolla",
  "model": "Auto",
  "year": 2001
}

car2 = {
  "brand": "Corolla",
  "model": "Auto",
  "year": 2002
}

for key, value in car1.items():
    if car1[key] == car2[key]:
        print(True)
    else:
        print(False)