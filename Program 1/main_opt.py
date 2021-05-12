import sys
## Function to check whether there is a subset equivalent to sum given
def check_subset(votes_list,sum1):
    m=sum1+1
    n=len(votes_list)+1
    count=[]
    mat=[[False for x in range(m)] for x in range(n)]
    mat[0][0]=True

    for j in range(0,m):
        if votes_list[0]==j:
            mat[1][j]=True
  
  
    for i in range(0,n):
        mat[i][0]=True
    subs=[]
    for i in range(2,n):
        for j in range(1,m):
            if votes_list[i-1]>j:
                mat[i][j]=mat[i-1][j]
            elif votes_list[i-1]<=j:
                if mat[i-1][j] or mat[i-1][j-votes_list[i-1]]:
                    mat[i][j]=True
  
    if mat[n-1][sum1-1]==True:
        print("sum is present in vote list")
    else:
        print("sum is not present in vote list")

##Funtion to find the total number of subsets and minimum length subset whose sum equal to the target
def tot_cnt2(votes_list, sum1):
    m = sum1 + 1
    n = len(votes_list) + 1
    total_solutions = [[0 for _ in range(m)] for _ in range(n)]
    minimum_elements = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(0, m):
        total_solutions[0][j] = 0
        minimum_elements[0][j] = 10000

    for i in range(0, n):
        total_solutions[i][0] = 1
        minimum_elements[i][0] = 0

    for i in range(1, n):            ## 1
        for j in range(1, m):        ## 2
            if votes_list[i - 1] > j:   ##3
                total_solutions[i][j] = total_solutions[i - 1][j]
                minimum_elements[i][j] = minimum_elements[i - 1][j]
            elif votes_list[i - 1] == j:   ##4
                total_solutions[i][j] = total_solutions[i - 1][j] + 1
                minimum_elements[i][j] = 1
            elif votes_list[i - 1] < j:   ##4
                total_solutions[i][j] = total_solutions[i - 1][j] + total_solutions[i - 1][j - votes_list[i - 1]]
                minimum_elements[i][j] = min(minimum_elements[i - 1][j], 1 + minimum_elements[i - 1][j - votes_list[i - 1]])
    return total_solutions[n-1][m-1],minimum_elements[n-1][m-1]


##Funtion to find the number of minimum length subset equal to target sum
def subset(target, i, req_sum, arr, size, k):
    if req_sum == target and not k:
        optimal_solutions[i][req_sum][k] = 1
        return 1
    elif req_sum < target and i < size:
        if optimal_solutions[i][req_sum][k] != -1:
            return optimal_solutions[i][req_sum][k]
        optimal_solutions[i][req_sum][k] = subset(target, i + 1, req_sum + arr[i], arr, size, k - 1) + subset(target, i + 1, req_sum, arr, size, k)
        return optimal_solutions[i][req_sum][k]
    return 0

##funtion to find the lexicographic ordered indices of the minimum subset
def lexi(k, size, req_sum):
    k1 = k - 1
    i1 = 1
    tar = 1
    while k1 >= 0:
        x = False
        for i in range(i1, size + 1):
            for j in range(tar, req_sum + 1):
                if optimal_solutions[i][j][k1] == 1:
                    ids.append(i - 1)
                    i1 = i + 1
                    tar = j + 1
                    k1 -= 1
                    x = True
                    break
            if x:
                break


##caller function
def caller_function(states,sum1):
    flag=0
    if isinstance(states,dict):
        arr=list(states.values())
        state_names=list(states.keys())
        flag=1
    else:
        arr=[]
        for i in states:
            if i!=',':
                arr.append(int(i))
        
    print("Number of elements ",len(arr))
    check_subset(arr,sum1)
    total_sol,min_num_ele=tot_cnt2(arr,sum1)
    print("Total number of subsets is ",total_sol)
    print("Minimum number of elements in subsets is",min_num_ele)
    
    subset(sum1, 0, 0, arr, len(arr), min_num_ele)
    print("Number od subsets with minimum number of elements are ",optimal_solutions[0][0][min_num_ele])
    lexi(min_num_ele,len(arr),sum1)
    print("Lexicographically sorted states with their votes are : ")
    
    if flag==0:
        for i in ids:
            print(arr[i])
    else:
        for i in ids:
            print(state_names[i], "   ",arr[i])


# commamd line 
ids = []
optimal_solutions = [[[-1 for _ in range(28)] for _ in range(500)] for _ in range(100)]
helper_text="main_opt.py file/array target_sum"
args=sys.argv[1:]
if len(args)==0:
    print("Please enter the argumenst as specified ",helper_text)
    sys.exit(1)
if len(args)!=2:
    print("Please enter the missing argument ",helper_text)
    sys.exit(1)
if not args[1].isnumeric():
    print("please eneter numeric sum ",helper_text)
    sys.exit(1)
if isinstance(args[0],list):
    caller_function(args[0],int(args[1]))
else:
    states={}
    if not args[0].endswith('.txt'):
        states=args[0]
    else:
        file = open(args[0])
        states_dict = file.read()
        states_dict=states_dict.strip()
        for s in states_dict.split('\n'):
            t=s.split(' ')
            states[t[1]]=int(t[0])
    caller_function(states,int(args[1]))


