class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        binary_list = [format(val, '08b') for val in data]

        byte_1 = '0'
        byte_2 = '110'
        byte_3 = '1110'
        byte_4 = '11110'
        byte_end = '10'

        pos = 0
        byte_count = 1
        length = len(binary_list) - 1
        while True:
            if byte_count == 1:
                if binary_list[pos][:1] == byte_1:
                    pos += 1
                else:
                    byte_count += 1

            if byte_count == 2 and pos + 1 < length:
                if binary_list[pos][:3] == byte_2 and binary_list[pos + 1][:2] == byte_end:
                    pos += 2
                    byte_count = 1
                else:
                    byte_count += 1
            
            if byte_count == 3 and pos + 2 < length:
                if (binary_list[pos][:4] == byte_3 and 
                binary_list[pos + 1][:2] == byte_end and 
                binary_list[pos + 2][:2] == byte_end):
                    pos += 3
                    byte_count = 1
                else:
                    byte_count += 1
            if byte_count == 4 and pos + 3 < length:
                if (binary_list[pos][:5] == byte_4 and 
                binary_list[pos + 1][:2] == byte_end and 
                binary_list[pos + 2][:2] == byte_end and 
                binary_list[pos + 3][:2] == byte_end):
                    pos += 4
                    byte_count = 1
                else:
                    return False
            
            if pos >= length:
                print(len(binary_list), pos, byte_count)
                return True
            elif pos + byte_count > length:
                return False
        

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []
        n = 0 #row
        m = 0 #column
        max_n = len(matrix)
        max_m = len(matrix[0])
        count = 0
        while True:
            # start moving right, increase m
            if m != max_m:
                for i in range(m, max_m):
                    
                    spiral.append(matrix[n][i])
                n += 1

            # start moving down, increase n
            if n != max_n:
                for i in range(n, max_n):
                    spiral.append(matrix[i][max_m - 1])
                max_m -= 1

            #moving left, decrease m
            if m != max_m:
                for i in range(max_m -1, m, -1):
                    spiral.append(matrix[max_n - 1][i])
                max_n -= 1

            #moving up, decrease n
            if n != max_n:
                for i in range(max_n, n - 1, -1):
                    spiral.append(matrix[i][m])
                m += 1

            if m == max_m and n == max_n:
                return spiral
            
            print(spiral, m, max_m, n, max_n)
            count += 1
            if count == 4:
                break

    
    def findball(self, grid: list[list[int]]) -> list[int]:
        
        result = []
        for i in range(len(grid[0])):
            print(i)
            result.append(findBallDropColumn(0, i, grid))
        return result


    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = commonPrefix(strs[0], strs[1])
        for i in range(2, len(strs)):
            result = commonPrefix(result, strs[i])
            if result == "":
                break
    
        return result


    def multiply(self, num1: str, num2: str) -> str:
        all_nums = []
        for i in range(len(num1)):
            pos1 = 10 ** (len(num1) - i - 1) 
            val1 = int(num1[i]) * pos1
            for j in range(len(num2)):
                pos2 = 10 ** (len(num2) - j - 1)
                val2 = int(num2[j]) * pos2
                all_nums.append(val1 * val2)
        
        result = 0
        for val in all_nums:
            result += val          
            
        return str(result)


def commonPrefix(str1, str2):
    result = []
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            result.append(str1[i])
        else:
            break
    result = "".join(result)
    return result

    
def findBallDropColumn(row, col, grid):
    if row == len(grid):
        return col
    next_column = col + grid[row][col]
    if next_column < 0 or next_column > len(grid[0]) - 1 or grid[row][col] != grid[row][next_column]:
        return -1
    
    return findBallDropColumn(row + 1, next_column, grid)

       
# print(Solution.validUtf8("a", [255]))
# print(Solution.spiralOrder("a" ,[[1,2,3],[4,5,6],[7,8,9]]))
# print(Solution.spiralOrder("a" ,[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# print(Solution.findball("a" ,[[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
# print(Solution.longestCommonPrefix("a" ,["",""]))
print(Solution.multiply("a" ,"111", "13"))
