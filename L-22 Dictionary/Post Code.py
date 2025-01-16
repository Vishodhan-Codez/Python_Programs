pc = {"India":"0056","Australia":"0097","Japan":"0087","USA":"0001","France":"0021","Germany":"0023","UK":"0012"}
req = input("Enter a name of a country to check for shipping : ")
deny = "This country is not part of our shipping network :( "
print(req,":",pc.get(req,deny))
