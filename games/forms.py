from django import forms
from .models import Teams, TEAM_CHOICES

class TeamSelectionForm(forms.Form):
    team1 = forms.CharField(max_length=100)
    team2 = forms.CharField(max_length=100)
    class Meta:
        model = Teams
        fields = ['team1', 'team2']