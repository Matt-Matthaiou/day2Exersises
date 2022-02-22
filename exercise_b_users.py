users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathansTwitter = users["Jonathan"]["twitter"]
print(jonathansTwitter)
# 2. Get Erik's hometown
eriksHometown = users["Erik"]["home_town"]
print(eriksHometown)
# 3. Get the array of Erik's lottery numbers
eriksLotteryNumbers = users["Erik"]["lottery_numbers"]
print(eriksLotteryNumbers)
# 4. Get the species of Avril's pet Monty
montySpecies = users["Avril"]["pets"][0]["species"]
print(montySpecies)
# 5. Get the smallest of Erik's lottery numbers
print(min(eriksLotteryNumbers))
#can also sort the list and print the 0 index.
# 6. Return an array of Avril's lottery numbers that are even
avrilsLotteryNumbers = users["Avril"]["lottery_numbers"]
avrilsEvenLotteryNumbers = []
for number in avrilsLotteryNumbers:
  if number %2 == 0:
    avrilsEvenLotteryNumbers.append(number)
print(avrilsEvenLotteryNumbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "Fluffy"
users["Erik"]["pets"].append({"name", "Fluffy" })

# 10. Add another person to the users dictionary
users["Matt"] = {"twitter": "Mattmatt", "lotttery_numbers": [1, 2, 3,], "home_town": "Thessaloniki", "pets": [{"name": "Timon", "species": "dog"}]}
print(users["Matt"])