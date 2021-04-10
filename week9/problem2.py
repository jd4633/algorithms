def get_team_options(people):
    r = []
    s = [] 
    print(f'len(people): {len(people)}')
    for i in range(0, len(people)):
        r.append(0)
        s.append([])
        person=people[i]
        print(f'person: {person}')
        people_list = people[0:i]
        print(f'people_list: {people_list}')
        if (len(people_list) == 0):
            s[i]=[[person]]
            r[i]=1
            continue
        print(f'looping through subteam options: {s[i-1]}')
        for subteam_option in s[i-1]:
            print(f'determining options to add {person} to subteam_option: {subteam_option}')
            print(f'adding {person} to their own team')
            team_option = subteam_option.copy()
            team_option.append(person)
            s[i].append(team_option)
            for j in range(0,len(subteam_option)):
                team_option = subteam_option.copy()
                team_option[j] = team_option[j] + person
                s[i].append(team_option)
    return s[len(people)-1]

people = ["a", "b", "c", "d"]
teams = get_team_options(people)
print(f'teams: {teams}')
print(f'teams size: {len(teams)}')