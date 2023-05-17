#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        self.keys = set()

        def addRoom(rooms, keys):
            temp = set(keys) - self.keys
            self.keys = self.keys | set(keys)
            if len(temp):
                temp_keys = []
                for k in temp:
                    temp_keys += rooms[k]
                addRoom(rooms, temp_keys)

        addRoom(rooms, [0])
        return len(rooms) == len(self.keys)


# @lc code=end
