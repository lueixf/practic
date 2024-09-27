input_data = open('input.txt','r')
data = input_data.read()
a = 9
c = int(data)
b = a-c
k = str(c) + str(a) + str(b)

output_data = open('output.txt','w')
output_data.write(k)


input_data.close()
output_data.close()