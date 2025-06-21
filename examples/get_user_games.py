from roblox import *
from roblox.objects.bases.basegame import BaseGame

client = RobloxClient()
games_iterator = client.fetch_user_games(2525288738)

for games_batch in games_iterator:
    for game in games_batch:
        game: BaseGame

        if game.id == 2535663803:
            print(game.fetch_game_media())



