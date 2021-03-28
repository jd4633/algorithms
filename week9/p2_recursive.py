def get_team_options(people, depth=0):
    t = " " * depth
    print(f'{t}Getting team options for: {people}')
    if (len(people) == 1):
        team_options=[[people[0]]] 
        print(f'{t}Only one person. Returning team options: {team_options}')
        return team_options
    people_copy = people.copy()
    person = people_copy.pop()
    print(f'{t}Popped person: {person}')
    print(f'{t}Making recursive call with remaining list: {people_copy}')
    sub_team_options = get_team_options(people_copy, depth+1)
    print(f'{t}Return from recursive call: {sub_team_options}')
    team_options = []
    for sub_team_option in sub_team_options:
        print(f'{t}Determining options to add {person} to: {sub_team_option}')
        # Person could get added as their own team
        team_option = sub_team_option.copy()
        team_option.append(person)
        print(f'{t}Adding option where person is on their own team: {team_option}')
        team_options.append(team_option)
        # Person could get added to any of the existing teams
        for i in range(0, len(sub_team_option)):
            team_option = sub_team_option.copy()
            print(f'{t}Adding person to team: {team_option[i]}')
            team_option[i] = team_option[i] + person
            team_options.append(team_option)
    return team_options

people = ["a", "b", "c", "d"]
teams = get_team_options(people)
print(f'teams: {teams}')
print(f'teams size: {len(teams)}')