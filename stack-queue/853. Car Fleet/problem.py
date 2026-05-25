class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        car_fleet = []
        for p,s in sorted(pair)[::-1]:
            car_fleet.append((target-p)/s)
            if len(car_fleet) >= 2 and car_fleet[-1] <= car_fleet [-2]:
                car_fleet.pop()
        return len(car_fleet)