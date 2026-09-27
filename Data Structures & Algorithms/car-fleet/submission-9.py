class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        max_speed = 0
        line = sorted(zip(position, speed), reverse = True)

        for car in line:
            if (target - car[0]) / car[1] > max_speed:
                count += 1
                max_speed = (target - car[0]) / car[1]


        return count