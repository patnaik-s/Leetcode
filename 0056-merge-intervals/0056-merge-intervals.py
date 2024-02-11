class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        n = len(arr) # size of the array

    # sort the given intervals:
        arr.sort()

        ans = []

        for i in range(n): # select an interval:
            start, end = arr[i][0], arr[i][1]

            # Skip all the merged intervals:
            if ans and end <= ans[-1][1]:
                continue

            # check the rest of the intervals:
            for j in range(i + 1, n):
                if arr[j][0] <= end:
                    end = max(end, arr[j][1])
                else:
                    break
            ans.append([start, end])
        return ans
            