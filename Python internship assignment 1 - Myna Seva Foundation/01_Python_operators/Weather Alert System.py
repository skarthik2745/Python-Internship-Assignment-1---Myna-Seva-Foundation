temp = int(input("Enter temperature in °C: "))
humidity = int(input("Enter humidity in %: "))
alert = temp > 35 and humidity > 75
print("Send heatwave alert?", alert)
