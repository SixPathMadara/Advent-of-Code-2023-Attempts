holding_Array=[]
value_array=[]
final_Answer=0
with open('input.txt','r') as file:
    while True:
        line=file.readline()
        if not line:
            break
        holding_Array.append(line)

for value in holding_Array:
    char_array=[]
    for char in value:
        if char.isdigit():
            char_array.append(char)
    value_array.append(char_array)

for val in value_array:
    firstlast=val[0]+val[-1]
    print(firstlast)
    final_Answer+=int(firstlast)

print(final_Answer)
