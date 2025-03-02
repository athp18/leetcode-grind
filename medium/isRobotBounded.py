class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in instructions:
            if i == 'G':
                x += dx[direction]
                y += dy[direction]
            elif i == 'L':
                direction = (direction + 3) % 4
            elif i == 'R':
                direction = (direction + 1) % 4
        
        return (x == 0 and y == 0) or direction != 0
