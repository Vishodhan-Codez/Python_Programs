temperature = float(input("Enter the current temperature in Celsius: "))
if temperature >= 40 or temperature <= 7.5:
    print("The temperature is extreme. Rohan should stay indoors and wear protective clothes.")
elif 30 <= temperature < 40:
    print("It's very hot! Rohan should wear light, breathable clothes.")
elif 25 <= temperature < 30:
    print("It's hot. Light clothes are perfect for this weather.")
elif 20 <= temperature < 25:
    print("It's warm. Rohan can comfortably wear light clothes.")
elif 15 <= temperature < 20:
    print("It's a bit cool. Rohan should consider wearing a light jacket.")
elif 10 <= temperature < 15:
    print("It's cold. Rohan should wear warm clothes like a jacket or pullover.")
else:  
    print("It's very cold. Rohan should dress in heavy winter clothes.")