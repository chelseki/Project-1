def vote_menu():
    print('----------------------------------')
    print('VOTE MENU')
    print('----------------------------------')
    print('v: Vote')
    print('x: Exit')
    option = input('Option: ').lower().strip()
    while option != 'v' and option != 'x':
        option = input('Invalid (v/x): ').lower().strip()
    return option 

def candidate_menu():
    print('----------------------------------')
    print('CANDIDATE MENU')
    print('----------------------------------')
    print('1: Bianca')
    print('2: Edward')
    print('3: Felicia')
    cand = int(input('Candidate: '))
    while cand != 1 and cand != 2 and cand != 3:
        cand = int(input('Invalid (1/2/3): '))
    if cand == 1:
        cand = 'Bianca'
    elif cand == 2:
        cand = 'Edward'
    elif cand == 3:
        cand = 'Felicia'
        
    print('Voted', cand)
    return cand

def main():
    Bi = 0
    Ed = 0
    Fe = 0
    
    option = vote_menu()
    while option != 'x':
        if option == 'v':
            cand = candidate_menu()
            if cand == 'Bianca':
                Bi += 1
            elif cand == 'Edward':
                Ed += 1
            elif cand == 'Felicia':
                Fe += 1
        option = vote_menu()
    total = Bi + Ed + Fe
    print('----------------------------------')
    print(f'Bianca - {Bi}, Edward - {Ed}, Felicia - {Fe}, Total - {total}')
    print('----------------------------------')

main()
    
