class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen=set()
        for i in range(1,len(tiles)+1):
            for p in permutations(tiles,i):
                seen.add(p)
        return len(seen)