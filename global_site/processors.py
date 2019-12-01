from players.models import Player

def highscores(request):
    top = Player.objects.order_by('-experience').only('name', 'experience', 'level')[:10]
    return {'highscores': top }
