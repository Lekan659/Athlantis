def print_top_50_classical_players() -> None:
    import requests
# An example of how to use requests
    resp = requests.get('https://lichess.org/api/player/top/100/classical')
    if resp.status_code != 200:
        return print('Api reurning error', str(resp.status_code))
    data = resp.json()

    if not data:
        return print('No data here')
    
    print("Food", data)

    for i in range(len(data['users'])):
        print(data['users'][i]['username'])
        if i == 49:
            break


print_top_50_classical_players()

def print_last_30_day_rating_for_top_player() -> None:
    import requests
# An example of how to use requests
    resp = requests.get('https://lichess.org/api/player/top/100/classical')
    if resp.status_code != 200:
        return print('Api reurning error', str(resp.status_code))
    data = resp.json()

    if not data:
        return print('No data here')
    
