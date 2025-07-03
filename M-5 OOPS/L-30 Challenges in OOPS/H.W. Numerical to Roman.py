class Roman:
    def to_rom(self, n):
        rom = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        vals= sorted(rom.keys(), reverse=True) # The keys r sorted in vals. iterates through vals, subtracting the highest value from n while adding the Roman numeral to res.
        res =""
        for i in vals:
            while n >= i:
                res += rom[i] # res is roman
                n -= i
        return res
obj1 = Roman()
num = int(input("Enter an integer: "))
print(f"Roman numeral: {obj1.to_rom(num)}")
