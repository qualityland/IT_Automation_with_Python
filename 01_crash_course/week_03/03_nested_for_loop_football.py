teams = ["SC Freiburg", "Herta BSC", "Union Berlin", "BVB Dortmund"]
for home_team in teams:
    for guest_team in teams:
        if home_team != guest_team:
            print(home_team + " : " + guest_team)