def numTilePossibilities(tiles: str) -> int:
    counter = [0] * 26
    for tile in tiles:
        counter[ord(tile) - ord('A')] += 1

    def dfs(record):
        s = 0
        for i in range(26):
            if not record[i]: continue
            record[i] -= 1
            s += dfs(record) + 1
            record[i] += 1
        return s

    return dfs(counter)


print(numTilePossibilities('AAA'))
