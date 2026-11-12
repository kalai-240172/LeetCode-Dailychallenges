class Solution:
    def longestMonotonicSubarray(self, num: List[int]) -> int:
        
        increasingArr=1
        DecreasingArr=1
        DeFaultreturn=1

        for i in range (1,len(num)):
            
            if num[i] > num[i-1]:
                increasingArr+=1
                DecreasingArr=1

            elif num[i] < num[i-1]:
                increasingArr=1
                DecreasingArr+=1
            
            else:
                increasingArr=1
                DecreasingArr=1
            
            DeFaultreturn = max(increasingArr,DecreasingArr,DeFaultreturn)

        return DeFaultreturn

