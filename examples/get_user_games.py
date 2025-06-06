from roblox import get_user_games, RobloxClient

client = RobloxClient()
games_iterator = get_user_games(10916243, client)

for games_batch in games_iterator:
    for game in games_batch:
        print(game)
