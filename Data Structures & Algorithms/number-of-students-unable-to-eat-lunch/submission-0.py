class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while count != len(students) and students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                temp = students.pop(0)
                students.append(temp)
                count += 1
        
        return count
                