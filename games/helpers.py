
def get_record(team1, team2, games):
    team1_wins = 0
    team2_wins = 0
    ties = 0
    for game in games:
        if game.road_score == game.home_score:
            ties += 1
        elif (team1 == game.road_team) & (game.road_score > game.home_score):
            team1_wins += 1
        elif (team1 == game.home_team) & (game.home_score > game.road_score):
            team1_wins += 1
        elif (team2 == game.road_team) & (game.road_score > game.home_score):
            team2_wins += 1
        elif (team2 == game.home_team) & (game.home_score > game.road_score):
            team2_wins += 1
    return [team1_wins, team2_wins, ties]

def get_tugowar_ratios(team1_wins, team2_wins, ties):
    team1_ratio = (team1_wins/(team1_wins+team2_wins+ties)) * 100
    team2_ratio = (team2_wins/(team1_wins+team2_wins+ties)) * 100
    ties_ratio = (ties/(team1_wins+team2_wins+ties)) * 100
    return [team1_ratio, team2_ratio, ties_ratio]

def get_largest_mov(team1, games):
    mov = [0,0]
    mov_date = ''
    margin = 0
    for game in games:
        if (team1 == game.road_team) & (game.road_score > game.home_score):
            current_margin = game.road_score - game.home_score
            if current_margin > margin:
                mov_date = game.date
                margin = current_margin
                mov[0] = game.road_score
                mov[1] = game.home_score
        elif (team1 == game.home_team) & (game.home_score > game.road_score):
            current_margin = game.home_score - game.road_score
            if current_margin > margin:
                mov_date = game.date
                margin = current_margin
                mov[0] = game.home_score
                mov[1] = game.road_score
    return (mov, mov_date)

def get_longest_streak(team1, games):
    streak = 0
    current_streak = 0
    current_streak_start_date = ''
    current_streak_end_date = ''
    dates = ['', '']
    for game in games:
        if team1 == game.road_team:
            if game.road_score > game.home_score:
                if current_streak == 0:
                    current_streak_start_date = game.date
                else:
                    current_streak_end_date = game.date
                current_streak += 1
                if current_streak > streak:
                    streak = current_streak
                    dates[0] = current_streak_start_date
                    dates[1] = current_streak_end_date
            else:
                current_streak = 0
        else:
            if game.home_score > game.road_score:
                if current_streak == 0:
                    current_streak_start_date = game.date
                else:
                    current_streak_end_date = game.date
                current_streak += 1
                if current_streak > streak:
                    streak = current_streak
                    dates[0] = current_streak_start_date
                    dates[1] = current_streak_end_date
            else:
                current_streak = 0
    return (streak, dates)

def get_mov_values(team1, games):
    mov = []
    for game in games:
        if team1 == game.road_team:
            mov.append(game.road_score - game.home_score)
        else:
            mov.append(game.home_score - game.road_score)
    return mov


