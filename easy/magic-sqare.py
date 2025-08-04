def formingMagicSquare(s):
    magic_squares = [
        [[8,1,6], [3,5,7], [4,9,2]],
        [[6,1,8], [7,5,3], [2,9,4]],
        [[4,9,2], [3,5,7], [8,1,6]],
        [[2,9,4], [7,5,3], [6,1,8]],
        [[8,3,4], [1,5,9], [6,7,2]],
        [[4,3,8], [9,5,1], [2,7,6]],
        [[6,7,2], [1,5,9], [8,3,4]],
        [[2,7,6], [9,5,1], [4,3,8]]
    ]

    min_cost = float('inf')

    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])
                print(cost)
        min_cost = min(min_cost, cost)
    print(min_cost)
    return min_cost

print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))



# def forming_matrix(mat):
#     magic_matrix=[
#         [[8,1,6], [3,5,7], [4,9,2]],
#         [[6,1,8], [7,5,3], [2,9,4]],
#         [[4,9,2], [3,5,7], [8,1,6]],
#         [[2,9,4], [7,5,3], [6,1,8]],
#         [[8,3,4], [1,5,9], [6,7,2]],
#         [[4,3,8], [9,5,1], [2,7,6]],
#         [[6,7,2], [1,5,9], [8,3,4]],
#         [[2,7,6], [9,5,1], [4,3,8]]
#     ]
#     cost_max= float("inf")
#     for magic in magic_matrix:
#         cost =0
#         for i in range(3):
#             for j in range(3):
#                 cost+=abs(mat[i][j] - magic[i][j])
#                 print(cost,"mohamil")
#         min_cost =min(cost_max,cost)
#     return min_cost
    
# forming_matrix([[5, 3, 4], [1, 5, 8], [6, 4, 2]])