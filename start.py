with open('countries.txt', 'r') as f:
    countrylist = [line.strip() for line in f]

correctans = []
score = 0


while score < 196:
    answer = input("country name")

    if answer in countrylist:
        countrylist.remove(answer)
        correctans.append(answer)
        print("correct")
        score = score + 1

    else:
        print("Country not recognised, try again.")

