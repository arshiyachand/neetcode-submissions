class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            mid = (l+r)//2
            if not self.can_eat(piles, mid, h):
                l = mid + 1
            else:
                r = mid

        return l
    def can_eat(self, piles, speed, h):
        hour = 0

        for pile in piles:
            if speed >= pile:
                hour += 1
            else:
                hour += math.ceil(pile/speed)
        return hour<=h



        