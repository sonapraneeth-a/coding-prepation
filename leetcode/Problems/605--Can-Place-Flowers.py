class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if flowerbed[0] == 0 and len(flowerbed) >= 2 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n == 0:
                return True
        elif len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        
        if flowerbed[-1] == 0 and len(flowerbed) >= 2 and flowerbed[len(flowerbed)-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            if n == 0:
                return True
        
        return False
                
            
        