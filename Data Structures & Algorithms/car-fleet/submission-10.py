class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        max_speed = 0
        line = sorted(zip(position, speed), reverse = True)

        for p, s in line:
            if (target - p) / s > max_speed:
                count += 1
                max_speed = (target - p) / s


        return count