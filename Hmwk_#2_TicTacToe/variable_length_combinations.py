fields_to_win = 3

x = [[17, 75, 71, 27, 37], [15, 53, 45, 25, 55], [1, 4, 7, 10, 9], [2, 5, 8, 11, 1], [3, 6, 9, 12, 1]]
y = [[17, 15, 1, 2, 3], [75, 53, 4, 5, 6], [71, 45, 7, 8, 9], [27, 25, 10, 11, 12], [37, 55, 9, 1, 1]]
z = [[71, 53, 1], [27, 45, 4, 2], [37, 25, 7, 5, 3], [55, 10, 8, 6], [9, 11, 9]]
f = [[71, 25, 9], [75, 45, 10, 1], [17, 53, 7, 11, 1], [15, 4, 8, 12], [1, 5, 9]]


res = [ list() for elements in range(20)]
temp_res = []

for comb in x:
    if len(comb) >= 3:
        #print(comb)
        for i, item in enumerate(comb):
            if len(comb[i:i+fields_to_win]) == fields_to_win: #valid win combinations should be chunks with length of defined fields_to_win
                print(i, item, comb[i:i+fields_to_win])
                temp_res.append(comb[i:i+fields_to_win])
print(temp_res)            
            #while len(temp_res) <= 3:
                #temp_res[i].append(item[i:i+(fields_to_win-1)]) #valid win combinations should be chunks with length of defined fields_to_win
                #print(i, item)