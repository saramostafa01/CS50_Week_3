def main():
    fuel = getFraction()
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else :
        print(f"{fuel}%")

def getFraction():
    while True:
        try:
            f = input("Fraction: ")
            x , y = f.split("/")
            x = int(x)
            y = int(y)
            if not x <= y:
                continue
            else:
                fuel = round((x/y)*100)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass 
    return fuel
main()