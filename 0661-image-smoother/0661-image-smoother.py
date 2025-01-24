class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row,col=len(img),len(img[0])
        res=[[0]*col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                tot,count=0,0
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if i < 0 or i == row or j < 0 or j == col:
                            continue
                        tot+=img[i][j] % 256 # ___ 1111 1111 given constrain 255 so anything before is always greater than 255
                        count+=1
                    
                res[r][c]= res[r][c] ^ (tot // count) << 8 #XOR OR operation to shifting 8 bit coz want to store result 
        return res