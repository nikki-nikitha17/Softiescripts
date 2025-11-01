def calculate_max_players():
    import sys
    sys.setrecursionlimit(10000)

    player_count = int(input())
    player_names = input().split()
    ability_scores = list(map(int, input().split()))

    name_to_id = {name: i for i, name in enumerate(player_names)}

    friend_count = int(input())
    parent = list(range(player_count))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    for _ in range(friend_count):
        a, b = input().split()
        if a in name_to_id and b in name_to_id:
            union(name_to_id[a], name_to_id[b])

    rival_count = int(input())
    rivals = set()
    for _ in range(rival_count):
        a, b = input().split()
        if a in name_to_id and b in name_to_id:
            rivals.add((name_to_id[a], name_to_id[b]))
            rivals.add((name_to_id[b], name_to_id[a]))

    max_total_score = int(input())

    groups = {}
    for i in range(player_count):
        root = find(i)
        groups.setdefault(root, []).append(i)

    group_list = list(groups.values())
    best = 0

    def backtrack(index, selected, total_score, selected_set):
        nonlocal best
        if total_score > max_total_score:
            return
        if index == len(group_list):
            best = max(best, selected)
            return

        group = group_list[index]
        valid = True
        for i in group:
            for j in selected_set:
                if (i, j) in rivals:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            new_score = total_score + sum(ability_scores[i] for i in group)
            backtrack(index + 1, selected + len(group), new_score, selected_set | set(group))

        backtrack(index + 1, selected, total_score, selected_set)

    backtrack(0, 0, 0, set())
    print(best)

if __name__ == "__main__":
    calculate_max_players()