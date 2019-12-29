# variable to contain the input
cities = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'London']


def group_cities(arr):
    results = []
    ignores = []
    # loop through each of the cities
    for index, city in enumerate(arr):

        if index in ignores:
            continue

        posibilities = []
        count_words = len(city)

        # rotate the name in any possible combination
        while count_words:
            rotated = city[count_words:] + city[:count_words]
            posibilities.append(rotated.lower())
            count_words -= 1

        # match start for next index and cross check posibilities
        # skip previous city
        # index + 1 is because we need actual index for the match city
        matches = {l_index + index + 1: l_city for l_index, l_city in
                   enumerate(arr[index + 1:]) if l_city.lower() in posibilities}

        if not matches:
            # append city to new group
            results.append([city])
        else:
            # append ignore index
            ignores.extend(match for match in matches.keys())

            # append city to same group
            results.append([city, *[match for match in matches.values()]])

    print(f"Test : {results}")


def group_cities_str_method(arr):
    results = []
    ignores = []
    for index, city in enumerate(arr):

        if index in ignores:
            continue

        hack_city = city.lower() * 2
        matches = {l_index + index + 1: l_city for l_index, l_city in
                   enumerate(arr[index + 1:]) if
                   len(l_city) == len(city) and l_city.lower() in hack_city}

        if not matches:
            results.append([city])
        else:
            ignores.extend(k for k in matches.keys())
            results.append([city, *[match for match in matches.values()]])

    print(f"Test : {results}")


group_cities(cities)
group_cities_str_method(cities)
