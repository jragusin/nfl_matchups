from django.db import models

TEAM_CHOICES = (
    ('Arizona Cardinals', 'Arizona Cardinals'),
    ('Atlanta Falcons', 'Atlanta Falcons'),
    ('Baltimore Ravens', 'Baltimore Ravens'),
    ('Buffalo Bills', 'Buffalo Bills'),
    ('Carolina Panthers', 'Carolina Panthers'),
    ('Chicago Bears', 'Chicago Bears'),
    ('Carolina Panthers', 'Carolina Panthers'),
    ('Cincinnati Bengals', 'Cincinnati Bengals'),
    ('Cleveland Browns', 'Cleveland Browns'),
    ('Dallas Cowboys', 'Dallas Cowboys'),
    ('Denver Broncos', 'Denver Broncos'),
    ('Detroit Lions', 'Detroit Lions'),
    ('Green Bay Packers', 'Green Bay Packers'),
    ('Houston Texans', 'Houston Texans'),
    ('Indianapolis Colts', 'Indianapolis Colts'),
    ('Jacksonville Jaguars', 'Jacksonville Jaguars'),
    ('Kansas City Chiefs', 'Kansas City Chiefs'),
    ('Las Vegas Raiders', 'Las Vegas Raiders'),
    ('Los Angeles Chargers', 'Los Angeles Chargers'),
    ('Los Angeles Rams', 'Los Angeles Rams'),
    ('Miami Dolphins', 'Miami Dolphins'),
    ('Minnesota Vikings', 'Minnesota Vikings'),
    ('New England Patriots', 'New England Patriots'),
    ('New Orleans Saints', 'New Orleans Saints'),
    ('New York Giants', 'New York Giants'),
    ('New York Jets', 'New York Jets'),
    ('Philadelphia Eagles', 'Philadelphia Eagles'),
    ('San Francisco 49ers', 'San Francisco 49ers'),
    ('Seattle Seahakws', 'Seattle Seahakws'),
    ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'),
    ('Tennessee Titans', 'Tennessee Titans'),
    ('Washington Football Team', 'Washington Football Team'),
)

# Create your models here.
class Teams(models.Model):
    team_name = models.CharField(max_length=100, choices=TEAM_CHOICES)

    def __str__(self):
        return self.team_name

    def __eq__(self, other):
        return self.team_name == other.team_name

class Games(models.Model):
    road_team = models.CharField(max_length=100)
    road_score = models.IntegerField()
    home_team = models.CharField(max_length=50)
    home_score = models.IntegerField()
    date = models.DateField()
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.roadteam + ' ' + self.road_score + ' ' + self.home_team + ' ' + self.home_score + ' ' + self.date.strftime('%B %-d, %Y')