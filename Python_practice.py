voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for voting_dict in voting_data:
    print(f"{voting_dict['county']} county has{voting_dict['registered_voters']: ,} registered voters.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has{voters: ,} registered voteers")

print("if this prints everything is getting run")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voter in counties_dict.items():
    print(county, " county has ", voter, " registered voters")