print("This is a electronics shop\nThese are the avalible goods:\nAir Conditioning Unit: ₹42,990/-\nRefirigirator: ₹64,900/-\n Washing Machine: ₹40,280/-\nInstallation: ₹1080")
ac = 42990
refrig = 64900 
washm = 40280
inst1 = 1080
shopp = input(" What do you wish to buy ?\n Enter the exact name from above : ")
bill = 0
if shopp == "Air Conditioning Unit" :
  bill += ac
elif shopp == "Refirigirator" :
  bill += refrig
elif shopp == "Washing Machine" :
  bill += washm
elif shopp == "Installation" :
  bill += inst1
print("Bill without tax : Rs.",bill)
print("Final Payable Amount : Rs.",(bill*0.18)+bill)