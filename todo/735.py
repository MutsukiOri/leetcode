class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        left = []
        left.append(asteroids[0])
        for i in range(1, len(asteroids)):
            print(left)
            if len(left) == 0:
                left.append(asteroids[i])

            elif asteroids[i] > 0:
                left.append(asteroids[i])
            elif left[-1] < 0:
                left.append(asteroids[i])
            else:
                alive = True
                while left[-1] > 0 and alive:
                    collision = left.pop()
                    if asteroids[i] + collision > 0:
                        left.append(collision)
                        alive = False
                        break
                    elif asteroids[i] + collision == 0:
                        alive = False
                        break
                    else:
                        if len(left) == 0:
                            break
                        else:
                            pass
                if alive:
                    left.append(asteroids[i])
        return left


solution = Solution()
asteroids = [1, -1, -2, -2]
print(solution.asteroidCollision(asteroids))
