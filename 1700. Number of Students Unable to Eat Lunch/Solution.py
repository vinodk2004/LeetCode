class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_0 = 0
        count_1 = 0
        for num in students:
            if num == 0:
                count_0 += 1
            else:
                count_1 += 1
        
        for i in sandwiches:
            if count_0 == 0 and i == 0:
                return count_1
            elif count_1 == 0 and i == 1:
                return count_0
            
            if i == 0:
                count_0 -= 1
            else:
                count_1 -= 1
        return 0