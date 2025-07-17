# Nested Reversal: Given a list of lists, reverse each inner list and then reverse the outer list.

list_nested = [[1, 2], [3, 4], [5, 6]]
# list_nested_sorted= sorted(sorted(list_nested,),reverse=True)
for l in list_nested:
    l.reverse()


list_nested.reverse()
print(list_nested)