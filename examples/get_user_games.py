from roblox import RobloxClient

client = RobloxClient()
games_iterator = client.fetch_games(10916243)


for games_batch in games_iterator:
    print(games_batch)
