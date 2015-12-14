from inputs import FOURTEENTH


reindeers = FOURTEENTH.speeds



distances = {}

for reindeer in reindeers:
    distance = 0
    total_seconds = 2503
    rspeed = reindeers[reindeer]['fly']
    time = reindeers[reindeer]['time']
    rest = reindeers[reindeer]['rest']
    while total_seconds >= time:
        total_seconds -= time
        distance += time * rspeed

        if total_seconds >= rest:
            total_seconds -= rest
            continue
        else:
            total_seconds = 0

    if total_seconds:
        distance += total_seconds * rspeed

    distances[reindeer] = distance

print distances, max(distances.values())

current_scores = {}

distances = {}

for reindeer in reindeers:
    current_scores[reindeer] = 0
    distances[reindeer] = 0
    reindeers[reindeer]['resting'] = 0
    reindeers[reindeer]['running'] = 0

for i in range(0,2503):
    for reindeer in reindeers:
        rspeed = reindeers[reindeer]['fly']
        time = reindeers[reindeer]['time']
        rest = reindeers[reindeer]['rest']
        resting = reindeers[reindeer]['resting']
        running = reindeers[reindeer]['running']

        if not resting:
            distances[reindeer] += rspeed
            reindeers[reindeer]['running'] += 1
            if reindeers[reindeer]['running'] == time:
                reindeers[reindeer]['resting'] = rest
                reindeers[reindeer]['running'] = 0
        else:
            reindeers[reindeer]['resting'] -= 1

    farthest = max(distances.values())
    winners = []
    for reindeer, dist in distances.items():
        if dist == farthest:
            winners.append(reindeer)
    for winner in winners:
        current_scores[winner] += 1

print current_scores




