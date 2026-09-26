class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        max_time = 0.0
        for p, s in cars:
            time = (target - p) / s
            if time > max_time:
                max_time = time
                fleets += 1
        return fleets