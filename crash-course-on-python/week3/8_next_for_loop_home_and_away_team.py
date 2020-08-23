# teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:

# What should the next line be to avoid both variables being printed with the same value?

# 1. while home_team != away_team:
# 2. for home_team == away_team:
# 3. away_team = home_team
# 4. if home_team != away_team:

# Solution:

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team: #option #4
            print(home_team+ " vs "+away_team, end=",")
    print()