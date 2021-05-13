import sys
from graph import Graph
from PriorityQueue import MinHeap

## The main function to compute the Total budget, time for the path from source to dest

def Dijkstras(input_graph,size):
    paths={}
    successor={}
    for i in range(0,size):
        paths[i]=[]

    for i in range(0,size):
        successor[i] =[]

    priorityqueue=MinHeap(2*size)
    source=Graph(0,0,0)
    priorityqueue.insert([source.cost,source.time,source.vertex])
    while(priorityqueue.size > 0):
        pair=priorityqueue.remove()
        dominant = 0

        for element in paths[pair[2]]:
            if element[0] <= pair[0] and element[1] <= pair[1]:
                dominant = 1
                
        ## Select the path and add it to the curve only if it is not dominated by another path for that vertex
        if dominant==0:    
            paths[pair[2]].append(pair)
        neighbors=input_graph[pair[2]]
        for i in range(0,len(neighbors)):
           
            if neighbors[i] == 0:
                continue
            else:
                
                graph=Graph(i,neighbors[i][0],neighbors[i][1])
                graph.cost = graph.cost + pair[0]
                graph.time = graph.time + pair[1]
                dominant = 0
                for element in priorityqueue.Heap:
                    if element[2] == i:
                        if element[0] <= graph.cost and element[1] <= graph.time:
                            dominant=1
                            break


                for element in paths[i]:
                        if element[0] <= graph.cost and element[1] <= graph.time:
                            dominant=1
                            break

                ## Add only that vertex with the updated cost and time to reach it if it is not dominated by another vertex in the priority queue
                if dominant == 0:
                   
                    priorityqueue.insert([graph.cost,graph.time,graph.vertex])
                    successor[pair[2]].append([graph.cost,graph.time,graph.vertex])
               
        
    return paths,successor


## Function to print the trade-off curves from source to dest
def print_curve(curves,source,dest,budget):
    p=curves[dest]
    print("The tradeoff curve is ")
    print(dest,":",end = " ")
    for i in p:
        print(i , end= " ")
    print()
    for i in range(0,len(p)):
        if p[i][0]>budget:
            if i == 0:
                print("No such path exists from source ",source," to destination ",dest)
                exit()

            return p[i-1]
            break
    return p[i]

## Function to print the optimal paths from source to dest
def print_source_dest_paths(paths,budget,time):
    print("The optimal path from source ", paths[-1] ," to detination ",paths[0], " has cost ",budget, " time ",time)
    for i in paths[::-1]:
        if i==paths[0]:
            break
        print(i," -> ",end = " ")
    print(i,end=" ")


## Function to backtrack and find the path from source to dest of an optimal path [path within budget]

def find_path(element,successor,input_graph,path_dir,source):
    
    if element[2] == source:
        path_dir.append(source)
        return path_dir
    for key,val in successor.items():
        if element in val:
            element[0]=element[0]-input_graph[key][element[2]][0]
            element[1]=element[1]-input_graph[key][element[2]][1]
            path_dir.append(element[2])
            element[2] = key
            break
    find_path(element,successor,input_graph,path_dir,source)
    return path_dir

def find_successor(successor,input_graph,optimal_path,source):
    
    budget = optimal_path[0]
    time = optimal_path[1]
    path_dir=[]
    path_dir=find_path(optimal_path,successor,input_graph,path_dir,source)
    
    print_source_dest_paths(path_dir,budget,time)

## Function to preprocess the input 
def pre_processing(file,source,dest,budget):
    source=int(source)
    dest=int(dest)
    budget=int(budget)
    file=open(file,'r')
    lines=file.readlines()
    G=[]
    maximum1=0
    maximum2=0
    for i in lines:
        
        index=i.strip().split(' ')
        
        if maximum1<int(index[0]):
            maximum1=int(index[0])
        if maximum2<int(index[1]):
            maximum2=int(index[1])
        G.append(index)
    maximum=max(maximum1,maximum2)
    size=maximum+1
    input_graph = [ [0] * size for _ in range(size)]
    for i in G:
        index=[]
        for j in i:
            index.append(int(j))
        input_graph[index[0]][index[1]] = (index[2],index[3])
    curves,successor=Dijkstras(input_graph,size)
    optimal_path=print_curve(curves,source,dest,budget)
  
    find_successor(successor,input_graph,optimal_path,source)
  

if __name__ == "__main__":
    helper_text="python cpath.py file source dest budget"
    args = sys.argv
    if len(args) < 5:
        print("Please enter the command line argumenst as specified ",helper_text)
        sys.exit(1)
    
    pre_processing(args[1],args[2],int(args[3]),int(args[4]))
