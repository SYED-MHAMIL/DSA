
# # def diagonalDifference(arrs):
# #      # Write your code here
# #   right_diag=sum([ar[i] for i,ar in enumerate(arrs)])
# #   left_diag= sum([ar[i] for i,ar in enumerate(arrs[::-1])])
# #   return right_diag

# # arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# # print(diagonalDifference(arr))
# # arrs=[1,2,3]
# # for i in range(len(arrs),0,-1):
# #     print(i-1)
# # 11 2 4
# # 4  5 6
# #10  8 -12

# def diagonalDifference(arrs):
#      # Write your code here
#   right_diag=sum([arrs[i][i] for i in range(len(arrs))])
#   left_diag= ([arrs[i-1][-i] for i in range(len(arrs),0,-1)])
#   return left_diag

# arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# print(diagonalDifference(arr))