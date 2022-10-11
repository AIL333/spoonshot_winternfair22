# required function which returns the output array
def function(a):
    # the pattern between the input and output is as follows:
    b = [a[1]*a[2]*a[3], a[0]*a[2]*a[3], a[0]*a[1]*a[3], a[0]*a[1]*a[2]]
    return b


# creating the empty input array
input_arr = []
# Adding input values in the input array
for i in range(0, 4):
    input_arr.append(int(input()))
# returning output array after function call
output_arr = function(input_arr)
print(output_arr)





