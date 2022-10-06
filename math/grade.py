class Solution:
    def solution(self, a, b, c):
        title = " ### 성적표 ### "
        total = a + b + c
        avg = round(total / 3)
        grade = ""
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"    
        elif avg >= 70:
            grade = "C" 
        elif avg >= 60:
            grade = "D" 
        elif avg >= 50:
            grade = "E" 
        else:
            grade = "F"
        return f"{title} \n  총점: {total}, 평균: {avg}, 학점: {grade}"

if __name__=="__main__":
    solution = Solution()
    a = int (input(" 국어: "))
    b = int (input(" 영어: "))
    c = int (input(" 수학: "))
    print(solution.solution(a, b, c))
