print("")
print("Function to find the length of the List")
List = [4,8,6,3,10,77,43,2]
print("The list is :" +str(List))
def countListLength(List):

 """Function to Compute the Lenght of the List"""
 listCount = 0
for i in List :
  listCount= listCount+1
  return listCount
print("Length of the given List is : " +str(countListLength(List)))
