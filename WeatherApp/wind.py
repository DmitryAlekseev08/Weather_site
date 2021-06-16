def direction(response):
    if response['cod'] == 200:
        if response['wind']['deg'] == 0 or response['wind']['deg'] == 360:
            return 'N'
        elif 90 > response['wind']['deg'] > 0:
            return 'NE'
        elif response['wind']['deg'] == 90:
            return 'E'
        elif 180 > response['wind']['deg'] > 90:
            return 'SE'
        elif response['wind']['deg'] == 180:
            return 'S'
        elif 270 > response['wind']['deg'] > 180:
            return 'SW'
        elif response['wind']['deg'] == 270:
            return 'W'
        else:
            return 'NW'
