from django.shortcuts import render
from .forms import TeamSelectionForm
from .models import Teams, Games
from django.db.models import Q
from .helpers import get_record, get_tugowar_ratios, get_largest_mov, get_longest_streak, get_mov_values
from .colors import TEAM_COLORS

# Create your views here.
def home(request):
    context = {
        'teams': Teams.objects.all(),
        'form': TeamSelectionForm(),
    }
    if request.method == 'POST':
        t_form = TeamSelectionForm(request.POST)
        context.update(form = t_form)
        if t_form.is_valid():
            team1 = request.POST['team1']
            team2 = request.POST['team2']
            if team1 != team2:
                context['first'] = team1
                context['second'] = team2
                context['team1_color'] = TEAM_COLORS[team1]
                context['team2_color'] = TEAM_COLORS[team2]
                set1 = Games.objects.filter(Q(road_team=team1) & Q(home_team=team2))
                set2 = Games.objects.filter(Q(home_team=team1) & Q(road_team=team2))
                games = (set1 | set2).order_by('-date')
                context['games'] = games
                records = get_record(team1, team2, list(games))
                context['tugowar_ratios'] = get_tugowar_ratios(records[0], records[1], records[2])
                context['record'] = records
                (context['team1_streak'], context['team1_streak_dates']) = get_longest_streak(team1, games)
                (context['team2_streak'], context['team2_streak_dates']) = get_longest_streak(team2, games)
                (context['team1_mov'] , context['team1_mov_date']) = get_largest_mov(team1, games)
                (context['team2_mov'], context['team2_mov_date']) = get_largest_mov(team2, games)
                context['mov_data'] = get_mov_values(team1, games)
        return render(request, 'games/home.html', context)
    return render(request, 'games/home.html', context)