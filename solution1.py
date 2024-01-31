def print_top_50_classical_players() -> None:
    import requests
    resp = requests.get('https://lichess.org/api/player/top/100/classical')
    if resp.status_code != 200:
        return print('Api reurning error', str(resp.status_code))
    data = resp.json()

    if not data:
        return print('No data here')
    

    for i in range(len(data['users'])):
        print(data['users'][i]['username'])
        if i == 49:
            break


print_top_50_classical_players()