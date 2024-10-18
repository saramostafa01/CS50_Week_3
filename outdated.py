list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        month , day , year = [int(_) for _ in date.split("/")]
        if month > 12 :
            continue
        else:
            print(f"{year}-{month:02}-{day:02}")
            break

    except ValueError:
        rest, year = date.split(",")
        year = int(year.strip())
        month , day = rest.split(" ")
        day = int(day)
        if day > 31:
            continue
        else:
            month = (list.index(month)+1)
            print(f"{year}-{month:02}-{day:02}")
            break