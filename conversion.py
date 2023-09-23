conversion = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
conversion_factors = [1000, 100, 10, 1, 0.1, 0.01, 0.001]
print("Conversion: km, hm, dam, cm, dm, hm, mm")


input_value = float(input("Input number: "))
early = input("Early: ")
last = input("Last: ")

from_early = -1
to_last = -1

for f, unit in enumerate(conversion):
    if early == unit:
        from_early = f
    if last == unit:
        to_last = f
        
if from_early !=-1 and to_last !=-1:
    if from_early == to_last:
        result = input_value
    else:
        meters= input_value*conversion_factors[from_early]
        
        
        if conversion[to_last] !=0:
            result=meters/conversion_factors[to_last]
        else:
            print( "Invalid, cannot be converted")
            exit(1)
            
    print(input_value, early, "=", result, last)
else:
    print("Invalid units entered")