fields_to_win = 3

#x = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]]
#y = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 1]]
#z = [[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
f = [[0, 1, 0], [-1, -1, -1], [0, 0, 0], [0, -1, 0], [0, 0, 0]]



def listSum(fields_combination):
    choice_results = 0
    for choice in fields_combination:
        choice_results += choice
    print(choice_results, fields_to_win)
    if choice_results == fields_to_win:
        print("Winner is player 'X' !")
    elif choice_results == -fields_to_win:
        print("Winner is player 'O' !")
    else:
        print("It's a draw!")

temp_res = list()

def define_win_combinations_map(list):
    for comb in list:
        if len(comb) >= 3:
            #print(comb)
            for i, item in enumerate(comb):
                if len(comb[i:i+fields_to_win]) == fields_to_win: #valid win combinations should be chunks with length of defined fields_to_win
                    temp_res.append(comb[i:i+fields_to_win])
    #print(temp_res)            

#define_win_combinations_map(x)
#define_win_combinations_map(y)
#define_win_combinations_map(z)
define_win_combinations_map(f)

print(temp_res)  


for comb in temp_res:
    listSum(comb)
 