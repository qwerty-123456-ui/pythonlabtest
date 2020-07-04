# Write a function subsetSum() that takes as input a list of positive numbers and a positive number target. Your function should return True if there are three numbers in the list that add up to target.
# For example, if the input list is [5, 4, 10, 20, 15, 19] and target is 38, then True should be returned since 4+15+19 = 38. However, if the input list is the same but the target value is 10, then the returned value should be False because 10 is not the sum of any three numbers in the given list.


def isSubsetSum(set,n,sum):
    if (sum == 0):
        return True
    if (n==0 and sum!=0):
        return False
    if (set[n-1]>sum):
        return isSubsetSum(set,n-1,sum)
    return isSubsetSum(set,n-1,sum) or isSubsetSum(set,n-1,sum-set[n-1])

set=[5,4,10,20,15,19]
sum=9
n=len(set)
if (isSubsetSum(set,n,sum)==True):
    print("Found a subset with given sum ")
else:
    print("No subset with given sum")
