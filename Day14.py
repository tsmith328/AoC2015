deer = {}
distances = {}

time = 2503

def main():
    with open('input14.txt') as f:
        for line in f:
            line = line.split()
            speed = int(line[3])
            name = line[0]
            length = int(line[6])
            rest = int(line[13])
            deer[name] = (speed, length, rest)
            distances[name] = 0

    standings = simulate(time)
    print("The winning reindeer went this far:", standings[-1][1])

    standings = score(time)
    print("The winning reindeer had this many points:", standings[-1][1])

def simulate(time):
    rest_timer = {}
    tired = {}
    for durr in deer:
        tired[durr] = deer[durr][1]
    for i in range(time):
        for durr in deer:
            if durr not in rest_timer:
                #move forward
                distances[durr] += deer[durr][0]
                tired[durr] -= 1 #Gets tired
                if tired[durr] == 0:
                    rest_timer[durr] = deer[durr][2]
            else:
                #resting
                rest_timer[durr] -= 1
                if rest_timer[durr] == 0:
                    del rest_timer[durr]
                    tired[durr] = deer[durr][1]
    standings = [(x, distances[x]) for x in distances]
    standings.sort(key=lambda x: x[1])
    return standings

def score(time):
    scores = {}
    for durr in deer:
        scores[durr] = 0
    for i in range(1, time+1):
        for durr in distances:
            distances[durr] = 0
        standings = simulate(i)
        best = [standings[-1]]
        for buck in standings:
            if buck in best:
                continue
            if buck[1] == best[0][1]:
                best.append(buck)
        for buck in best:
            scores[buck[0]] += 1

    standings = [(x, scores[x]) for x in scores]
    standings.sort(key=lambda x: x[1])
    return standings


if __name__ == '__main__':
    main()