def SumarListas(l1, l2):
    return l1 + l2


l1 = [1,2,3,4]
l2 = [9,8,7,6]


resultado = map(SumarListas, l1, l2)

print l1
print l2, "+ "
print "------------"

print resultado