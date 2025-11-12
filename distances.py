


def distances(): 
     return{
    "Voyager 1" : "160",
    "Voyager 2" : "136",
    "Voyager 10" : "80 AU",
    "New Horizon" : "58",
    "Pionner 11" : "44 AU",
    }

def main():
        spacecraft = input("Enter a spacecraft: ") # I AM A BOY#
        data = distances() 
        try:
         au = data[spacecraft]
        except KeyError:
         print("Spacecraft not found.")
        except ValueError:
         print(f"can't convert {spacecraft} to meters")
    
        else:
         au = float(data[spacecraft])
        km = convert(au)
        print(f"{km} km away")

def convert(au):
        return au * 149597870.7

main()











