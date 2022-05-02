'''
class Solution:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    def romanToInt(self, s: str) -> int:
        int = 0
        list = s.split()
        list = list.append(0)
        for i in range(len(list)+2):
            if i <= len(list):
                if list[i] == "M":
                    int = int + 1000
                elif list[i] == "D":
                    int = int + 500
                elif list[i] == "C":
                    if list[i+1] != "D" and list[i+1] == "M":
                        int = int + 900
                        i = i+2
                    if list[i+1] == "D" and list[i+1] != "M":
                        int = int + 400
                        i = i+2
                    if list[i+1] != "D" and list[i+1] != "M":
                        int = int + 100
                elif list[i] == "L":
                    int = int + 50
                elif list[i] == "X":
                    if list[i+1] != "L" and list[i+1] == "C":
                        int = int + 90
                        i = i+2
                    if list[i+1] != "D" and list[i+1] == "M":
                        int = int + 40
                        i = i+2
                    if list[i+1] != "D" and list[i+1] != "M":
                        int = int + 10
                elif list[i] == "V":
                    int = int + 5
                elif list[i] == "I":
                    if list[i+1] != "V" and list[i+1] == "X":
                        int = int + 9
                        i = i+2
                    if list[i+1] != "X" and list[i+1] == "V":
                        int = int + 4
                        i = i+2
                    if list[i+1] != "X" and list[i+1] != "V":
                        int = int + 1
            else:
                continue
'''                


new_list = []
s = ["H","a","n","n","a","h"]

def reverseString(new_list, s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    if len(s) == len(new_list):
        return new_list
        
    else:
        new_list.insert(0,s[len(new_list)])
        return reverseString(new_list,s)
    
    
print(reverseString(new_list,s))