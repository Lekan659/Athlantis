def print_last_30_day_rating_for_top_player(username) -> None:
    from datetime import datetime, timedelta
    import requests
# An example of how to use requests
    resp = requests.get('https://lichess.org/api/user/' + username + '/rating-history')
    if resp.status_code != 200:
        return print('Api reurning error', str(resp.status_code))
    data = resp.json()
    pointdata = []
    pointlist = {}
    c = -1
    today_date = datetime.now().date()
    end_date = today_date - timedelta(days=29)

    if not data:
        return print('No data here')

    for i in range(len(data)):
        if data[i]['name'] == 'Classical':
            pointdata = data[i]['points']

    newpoint = pointdata[-1][3]
    loop = True

    for day in reversed(range((today_date - end_date).days + 1)):
        current_date = end_date + timedelta(days=day)
        if current_date.day < pointdata[c][2] and loop:
            c -= 1
            if pointdata[c][2] > pointdata[c + 1][2]:
                loop = False
            
            newpoint = pointdata[c][3]
       
        pointlist["today -" + str(29 - day)] = newpoint

    return print(username, pointlist)


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
        # print_last_30_day_rating_for_top_player(data['users'][i]['username'])
        if i == 49:
            break




def generate_rating_csv_for_top_50_classical_players(username) -> None:
    from datetime import datetime, timedelta
    today_date = datetime.now().date()
    end_date = today_date - timedelta(days=29)

    cheaders = [username]

    # Reverse count down from 2024-01-30 to 2024-01-01 and print the dates
    for day in range((today_date - end_date).days + 1):
        print(day)
        current_date = end_date + timedelta(days=day)
        formatted_date = current_date.strftime("%Y-%m-%d")
        cheaders.append(formatted_date)
    
    print(cheaders)
    # pass




generate_rating_csv_for_top_50_classical_players('strategyforchess')

# print_top_50_classical_players()


# print_last_30_day_rating_for_top_player('strategyforchess')
