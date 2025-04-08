import random

outcome = ['w', 0, 1, 4, 0, 1, 0, 2, 4, 0, 1, 6, 0, 1, 2, 0, 1, 0, 1, 2, 1, 'w', 0, 1, 4, 0, 1, 0, 2, 4, 0, 1, 6, 0, 1,
           2, 0, 1, 0, 1, 3, 1]
outcome1 = ['w', 0, 2, 4, 6, 2, 1, 2, 4, 1, 1, 6, 1, 1, 2, 4, 1, 0, 2, 3, 0, 'w', 1, 1, 4, 0, 1, 0, 2, 4, 1, 1, 6, 0, 1,
            2, 1, 2, 0, 1, 4, 1]
outcome2 = ['w', 0, 1, 0, 1, 0, 2, 4, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 1, 'w', 0, 1, 4, 0, 1, 0, 2, 4, 0, 1, 6, 0, 1,
            2, 0, 1, 'w', 1, 3, 1]
outcome3 = ['w', 0, 2, 4, 6, 2, 1, 2, 4, 1, 1, 6, 1, 1, 2, 4, 1, 0, 2, 3, 0, 'w', 1, 1, 4, 0, 1, 0, 2, 4, 1, 1, 6, 0, 1,
            2, 1, 2, 0, 1, 4, 1,'w', 0, 2, 4, 6, 2, 1, 2, 4, 1,'w', 1, 6, 1, 1, 2, 4, 1, 0, 2, 0, 'w']
outcome4 = ['w', 0, 1, 4, 0, 1, 0, 2, 0, 1, 0, 0, 1, 0, 1, 2, 1, 4, 0, 1, 0, 0, 1, 2, 0, 1, 0, 1, 2, 1, 'w', 0, 1, 4, 0, 1, 0, 2, 0, 1, 0, 0, 1, 0, 1, 2, 1, 4, 0, 1, 6, 0, 1, 2, 0, 1, 0, 1, 3, 1, 0, 1, 0, 0, 1, 0, 1, 2, 1, 1, 0, 1, 0, 0, 1, 0, 1, 2, 1]
opponent = ['SA','AUS', 'ENG', 'WI', 'NZ', 'PAK']
oppteam = random.choices(opponent)
b = oppteam[0]
print('----------- CRICKET SCORE SIMULATOR -----------')
print('')
print('IND VS', b)
toss = ['H', 'T']
while True:
    call = input('Call the toss:H or T:')
    if call == 'H' or call == 'T':
        break
    else:
        print('Invalid Call!')
toss = random.choices(toss)
toss = toss[0]
choice = ['BAT', 'BOWL']
choice = random.choices(choice)
choice = choice[0]
batting_order = {'Shikhar Dhawan': 1, 'Rohit Sharma': 2, 'Virat Kohli': 3, 'Rishabh Pant': 4, 'Shreyash Iyer': 5,
                 'Surya Kumar Yadav': 6, 'Ravindra Jadeja': 7, 'Deepak Chahar': 8, 'Yuzvendra Chahal': 9,
                 'Md.Siraj': 10,
                 'Jasprit Bumrah': 11}
runs = {'Shikhar Dhawan': 0, 'Rohit Sharma': 0, 'Virat Kohli': 0, 'Rishabh Pant': 0, 'Shreyash Iyer': 0,
        'Surya Kumar Yadav': 0, 'Ravindra Jadeja': 0, 'Deepak Chahar': 0, 'Yuzvendra Chahal': 0, 'Md.Siraj': 0,
        'Jasprit Bumrah': 0}
bat_ball = {'Shikhar Dhawan': 0, 'Rohit Sharma': 0, 'Virat Kohli': 0, 'Rishabh Pant': 0, 'Shreyash Iyer': 0,
            'Surya Kumar Yadav': 0, 'Ravindra Jadeja': 0, 'Deepak Chahar': 0, 'Yuzvendra Chahal': 0, 'Md.Siraj': 0,
            'Jasprit Bumrah': 0}
sixes = {'Shikhar Dhawan': 0, 'Rohit Sharma': 0, 'Virat Kohli': 0, 'Rishabh Pant': 0, 'Shreyash Iyer': 0,
         'Surya Kumar Yadav': 0, 'Ravindra Jadeja': 0, 'Deepak Chahar': 0, 'Yuzvendra Chahal': 0, 'Md.Siraj': 0,
         'Jasprit Bumrah': 0}
fours = {'Shikhar Dhawan': 0, 'Rohit Sharma': 0, 'Virat Kohli': 0, 'Rishabh Pant': 0, 'Shreyash Iyer': 0,
         'Surya Kumar Yadav': 0, 'Ravindra Jadeja': 0, 'Deepak Chahar': 0, 'Yuzvendra Chahal': 0, 'Md.Siraj': 0,
         'Jasprit Bumrah': 0}
batsman = list()
for striker in runs:
    batsman.append(striker)
striker = batsman[0]
non_striker = batsman[1]
batsman_count = 1
score = 0
wicket = 0
over = 0.0
rem = 120
rr = 0.0
dot_ball = 0
single = 0
Double = 0
triple = 0
four = 0
six = 0
runs_in_over = 0
over_timeline = list()
ind = False
bat = 2
if call == toss:
    c = choice
    if c == 'BAT':
        ind = True
        bat = 1
        print(' IND Won The Toss Choose Bat First')
    elif c == 'BOWL':
        ind = False
        bat = 2
        print(' India Won The Toss Choose Bowl First')
elif call != toss:
    opp = choice
    if opp == 'BAT':
        ind = False
        bat = 2
        print('', b, 'Won The Toss Choose Bat First')
    elif opp == 'BOWL':
        ind = True
        bat = 1
        print('', b, 'Won The Toss Choose The Bowl First')

j = input()
team_1_score = 0
team_1_wicket = 0
over = 0.0

if ind is False and bat == 2:
    print('', b, 'Batting')
    rr = 0
    over = 0.0
    print('', b, '', team_1_score, '-', team_1_wicket, ', overs:', over, 'RR:', rr)
    for balls in range(1, 121):
        if team_1_wicket > 6:
            rand = random.choices(outcome2)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        elif over > 15 and team_1_wicket <= 5:
            print('high time')
            rand = random.choices(outcome1)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        else:
            rand = random.choices(outcome)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        over_timeline.append(n)
        if rand[0] == 'w':
            team_1_wicket += 1
        elif rand[0] == n:
            team_1_score = team_1_score + n
        rr = float(team_1_score / over)
        if over % 1 == 0:
            i = input()
            print('', b, '', team_1_score, '-', team_1_wicket, ', overs:', over, 'RR:', rr)
            print(over_timeline)
            over_timeline.clear()
        if team_1_wicket == 10:
            i = input()
            print('', b, '', team_1_score, '-', team_1_wicket, ', overs:', over, 'RR:', rr)
            print(over_timeline)
            over_timeline.clear()
            break

    ind = True
if ind is True and bat == 1:
    rr = 0
    over = 0.0
    part_run=0
    part_bowl=0
    print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
    for balls in range(1, 121):
        g = input()
        if batting_order[striker] > 7:
            rand = random.choices(outcome2)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        elif over > 15 and wicket <= 5:
           
            if g.lower()=='h':
                rand = random.choices(outcome3)
                print('high time HIT')
                print()
            else:
                rand = random.choices(outcome1)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        else:
            if g.lower()=='h':
                rand = random.choices(outcome3)
                print('HIT')
                print()
            elif g.lower()=='d':
                rand = random.choices(outcome4)
                print('DEF')
                print()
            else:
                rand = random.choices(outcome)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        if n == 4:
            four += 1
            fours[striker] = fours.get(striker, 0) + 1
        if n == 6:
            six += 1
            sixes[striker] = sixes.get(striker, 0) + 1

        if n == 'w':
            part_run=0
            part_bowl=0
            wicket += 1
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
        elif n % 2 == 0:
            score += n
            part_bowl+=1
            part_run+=n
            runs_in_over += n
            runs[striker] = runs.get(striker, 0) + n
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
        else:
            part_bowl+=1
            part_run+=n
            score += n
            runs_in_over += n
            runs[striker] = runs.get(striker, 0) + n
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
            temp = striker
            striker = non_striker
            non_striker = temp
        over_timeline.append(n)
        if n == 1:
            single += 1
        elif n == 2:
            Double += 1
        elif n == 3:
            triple += 1
        elif n == 0:
            dot_ball += 1
        if n == 'w':
            if wicket == 10:
                print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
                print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)
                over_timeline.clear()
                break
            batsman_count += 1
            striker = batsman[batsman_count]
        if balls % 6 == 0:
            temp = striker
            striker = non_striker
            non_striker = temp
        rr = float((score / balls)*6)
        if over % 1 == 0:
            
            print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
            print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)
            print(striker, runs[striker], '(', bat_ball[striker], ')', ':', non_striker, runs[non_striker], '(',
                  bat_ball[non_striker], ')')
            print('Paartnership: ',str(part_run)+'('+str(part_bowl)+')')
            over_timeline.clear()
            runs_in_over = 0
        else:
            
            print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
            print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)
            print(striker, runs[striker], '(', bat_ball[striker], ')', ':', non_striker, runs[non_striker], '(',
                  bat_ball[non_striker], ')')
            print('Paartnership: ',str(part_run)+'('+str(part_bowl)+')')
    print('')
    print('----------Scorecard----------')
    print('')
    print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
    print('')
    for x, y in runs.items():
        if bat_ball[x] == 0:
            strike = '-'
        else:
            strike = int((runs[x] / bat_ball[x]) * 100)
        if wicket == 10 and x == non_striker:
            print('')
            print(non_striker, '*', y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], ':S/R', strike)
        else:
            if x == non_striker:
                print('')
                print(non_striker, '*', y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], 'S/R', strike)
                continue
            if x == striker:
                print('')
                print(striker, '*', y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], ':S/R', strike)
            else:
                print('')
                print(x, y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], ':S/R', strike)
    print('0s', dot_ball, ':1s', single, ':2s', Double, ':3s', triple, ':4s', four, ':6s', six)
    ind = False
print('End of Inning')
if ind is True and bat == 2:
    rr = 0
    over = 0.0
    part_bowl=0
    part_run=0
    print('')
    margin = abs(team_1_score - score) + 1
    print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
    print('', team_1_score - score + 1, 'Needed in 20.0 Overs')
    for balls in range(1, 121):
        g=input()
        if batting_order[striker] > 7:
            rand = random.choices(outcome2)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1

        elif over > 15 and wicket <= 5:
            
            if g.lower()=='h':
                rand = random.choices(outcome3)
                print('high HIT')
                print()
            else:
                rand = random.choices(outcome1)
                print('high time')
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        else:
            if g.lower()=='h':
                rand = random.choices(outcome3)
                print('HIT')
                print()
            elif g.lower()=='d':
                rand = random.choices(outcome4)
                print('DEF')
                print()
            else:
                rand = random.choices(outcome)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        if n == 4:
            four += 1
            fours[striker] = fours.get(striker, 0) + 1
        if n == 6:
            six += 1
            sixes[striker] = sixes.get(striker, 0) + 1

        if n == 'w':
            part_run=0
            part_bowl=0
            wicket += 1
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
        elif n == 0:
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
            part_bowl+=1
        elif n == 6 or n == 4:
            part_run+=n
            part_bowl+=1
            score += n
            runs_in_over += n
            runs[striker] = runs.get(striker, 0) + n
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
        elif n > (team_1_score+1)-(score):
            print(n)
            print('vulnerable')
            n = (team_1_score+1)-score
            runs_in_over += n
            part_run+=n
            part_bowl+=1
            score += n
            runs[striker] = runs.get(striker, 0) + n
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
        elif n == 2:
            score += n
            part_run+=n
            part_bowl+=1
            runs_in_over += n
            runs[striker] = runs.get(striker, 0) + n
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
        else:
            score += n
            part_run+=n
            part_bowl+=1
            runs_in_over += n
            runs[striker] = runs.get(striker, 0) + n
            bat_ball[striker] = bat_ball.get(striker, 0) + 1
            temp = striker
            striker = non_striker
            non_striker = temp
        over_timeline.append(n)
        if n == 1:
            single += 1
        elif n == 2:
            Double += 1
        elif n == 3:
            triple += 1
        elif n == 0:
            dot_ball += 1
        rem = 120 - balls
        rr = float((score / balls) * 6)
        if n == 'w':
            if wicket == 10:
                print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
                break
            batsman_count += 1
            striker = batsman[batsman_count]
        elif score > team_1_score:
            i = input()
            rr = float(score / over)
            print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
            print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)
            break
        if balls % 6 == 0:
            temp = striker
            striker = non_striker
            non_striker = temp
        req=str(((team_1_score - score + 1)/(120 - balls))*6)
        if over % 1 == 0:
            print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
            print('Need', team_1_score - score + 1, 'Runs in', 120 - balls, 'Balls','   REQR:',req[:5])
            print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)
            print(striker, runs[striker], '(', bat_ball[striker], ')', ':', non_striker, runs[non_striker], '(',
                  bat_ball[non_striker], ')')
            print('Paartnership: ',str(part_run)+'('+str(part_bowl)+')')
            over_timeline.clear()
            runs_in_over = 0
        else:
            print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
            print('Need', team_1_score - score + 1, 'Runs in', 120 - balls, 'Balls','   REQR:',req[:5])
            print('Over Timeline:', over_timeline, runs_in_over, 'Runs In This Over')
            print(striker, runs[striker], '(', bat_ball[striker], ')', ':', non_striker, runs[non_striker], '(',
                  bat_ball[non_striker], ')')
            print('Paartnership: ',str(part_run)+'('+str(part_bowl)+')')

    print('')
    print('----------Scorecard----------')
    print('')
    print('  IND:', score, '-', wicket, ', overs:', over, 'RR:', rr)
    print('')
    for x, y in runs.items():
        if bat_ball[x] == 0:
            strike = '-'
        else:
            strike = int((runs[x] / bat_ball[x]) * 100)
        if wicket == 10 and x == non_striker:
            print('')
            print(non_striker, '*', y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], ':S/R', strike)
        else:
            if x == non_striker:
                print('')
                print(non_striker, '*', y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], 'S/R', strike)
                continue
            if x == striker:
                print('')
                print(striker, '*', y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], ':S/R', strike)
            else:
                print('')
                print(x, y, '(', bat_ball[x], ')', ':4s', fours[x], ':6s', sixes[x], ':S/R', strike)
    print('')
    print('0s', dot_ball, ':1s', single, ':2s', Double, ':3s', triple, ':4s', four, ':6s', six)
    ind = False
if ind is False and bat == 1:
    rr = 0
    over = 0.0
    margin = abs(team_1_score - score) + 1
    print('', b, 'Batting')
    print('')
    print(' ', b, team_1_score, '-', team_1_wicket, ', overs:', over, 'RR:', rr)
    for balls in range(1, 121):
        if team_1_wicket > 6:
            rand = random.choices(outcome2)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        elif over > 15 and team_1_wicket <= 5:
            print('high time')
            rand = random.choices(outcome1)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        else:
            rand = random.choices(outcome)
            n = rand[0]
            over = balls // 6
            over1 = balls % 6
            over1 = over1 / 10
            over = over + over1
        if n == 'w':
            team_1_wicket += 1
        elif n == 6 or n == 4:
            team_1_score += n
            runs_in_over += n
        elif n > margin:
            n = margin
            runs_in_over += n
            team_1_score += n

        elif rand[0] == n:
            team_1_score += n
            runs_in_over += n
        over_timeline.append(n)
        rem = 120 - balls
        if n == 'w':
            if team_1_wicket == 10:
                print(' ', b, team_1_score, '-', team_1_wicket, ', overs:', over, 'RR:', rr)
                print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)

                break
        elif score < team_1_score:
            i = input()
            print(' ', b, team_1_score, '-', team_1_wicket, ', overs:', over, 'RR:', rr)
            print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)
            break
        rr = float(team_1_score / over)
        if over % 1 == 0:
            n = input()
            print(' ', b, team_1_score, '-', team_1_wicket, ', overs:', over, 'RR:', rr)
            print('Need', score - team_1_score + 1, 'Runs in', 120 - balls, 'Balls')
            print('Over Timeline:', over_timeline, 'Runs In This Over', runs_in_over)
            over_timeline.clear()
            runs_in_over = 0
i = input()
print('')
tie = False
if score < team_1_score:
    if bat == 2:
        print('', b, 'Beat IND By', team_1_score - score, 'Runs')

    else:
        print('', b, 'Beat IND by', 10 - team_1_wicket, 'Wickets and with Remaining', rem, 'balls')
elif score == team_1_score:
    print('Match Tie')
    tie = True


else:
    if bat == 2:
        print('IND Beat', b, 'by', 10 - wicket, 'Wickets and With', rem, 'Remaining Balls')
    else:
        print('IND Beat', b, 'by', score - team_1_score, 'Runs')
print('')
print('')

if tie is True:
    while tie is True:
        team_1_score = 0
        team_1_wicket = 0
        over = 0.0
        print('')
        print('  Super over')
        print('')
        print('', b, 'Batting')
        print('')
        print('', b, team_1_score, '-', team_1_wicket, ', Balls 0')
        for balls in range(1, 7):
            rand = random.choices(outcome)
            n = rand[0]
            if rand[0] == 'w':
                team_1_wicket += 1
            elif rand[0] == n:
                team_1_score = team_1_score + n
                print('', b, team_1_score, '-', team_1_wicket, ', Balls:', balls)
            if team_1_wicket == 2:
                break
        print('')
        print('End of Over')
        score = 0
        wicket = 0
        print('IND', score, '-', wicket, 'Balls 0')
        print('', team_1_score - score + 1, 'Needed in', 6, 'Balls')
        margin = team_1_score - score + 1
        for balls in range(1, 7):
            i = input()
            rand = random.choices(outcome)
            n = rand[0]
            if rand[0] == 'w':
                wicket += 1
            elif margin < n:
                n = margin
                score += n
            elif rand[0] == n:
                score = score + n
                print(' IND', score, '-', wicket, ', Balls:', balls)
                print('', team_1_score - score + 1, 'Needed in', 6 - balls, 'Balls')
            if wicket == 2:
                break
            elif score > team_1_score:
                break
        if score < team_1_score:
            print('', b, 'Beat IND by', team_1_score - score, 'Runs')
            tie = False
        elif score == team_1_score:
            print('Match Tie')
        elif score > team_1_score:
            print(' IND Beat ', b, 'In The super over')
            tie = False
print('')
print('  Match over')
n=input()