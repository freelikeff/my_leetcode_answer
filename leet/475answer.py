#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/11 21:33 
# @Author : freelikeff 
# @Site : 
# @File : 475answer.py 
# @Software: PyCharm


# 每间房要么用前面的暖气，要么用后面的，所以需求是min，所以是求max（min）
class Solution(object):
    def findRadius(self, houses, heaters): # TODO:理解生成器
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        def heaters_generator(heaters):
            yield -2e9 - 2
            yield from sorted(heaters)
            yield 2e9 + 2

        # 写生成器是想少写一些代码...
        # 半径生成器，给出每个房屋与最近的供暖器的距离
        def radius_generator(houses, heaters):
            generator = heaters_generator(heaters)
            # 供暖器位置生成器中，在很远的地方增加了两个供暖器，这样任何一栋房屋左右都有供暖器，后续代码就不用考虑特殊情况了
            # 左侧和右侧最近的供暖器是left和right
            left, right = next(generator), next(generator)

            for house in sorted(houses):
                while house >= right:
                    left, right = right, next(generator)
                yield min(right - house, house - left)

        return max(radius_generator(houses, heaters))




if __name__ == '__main__':
    s = Solution()
    inpt = [1,2,3],[2]
    answer = s.findRadius(*inpt)
    print(answer)