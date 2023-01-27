Names= ["Omar", "Reem", "Arwa", "May", "Basma", "Achraf", "Mohammad"]

for y in range(6):
  print(Names[y])

for x in range(6):
  print(f"Hey, Welcome {Names[x]}!")

Visit= ["Dubai", "Liverpool", "Newyork", "Amman", "Paris"]
print(Visit)
print(sorted(Visit))
Visit.sort()
print(Visit)
Visit.sort(reverse=True)
print(Visit)
Visit.reverse()

print(len(Visit))
Visit.append("London")
print(Visit)
Visit.insert(2, "Manchester")
print(Visit)
del Visit[1]
print(Visit)
Visit.remove("Manchester")
print(Visit)
x = Visit.pop(3)
print(Visit)