temps = []

while True:
    temperature = input("Enter temperature ('done' to stop): ")
    if temperature == "done":
        break
    temps.append(int(temperature))


print(temps)                                    