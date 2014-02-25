import Queue
def bfs(graph,root,whatToFind):
    queue = Queue.Queue()
    queue.put(root)#put the first element in the queue, so we can explore it latter on
    while queue:#while there are elements in the queue
        curr = queue.get()
        print curr
        if whatToFind == curr:
            print 'found!'
            return#we have found what we are looking for
        if curr in graph:#if the current node has adjacent nodes
            [queue.put(adjacent) for adjacent in graph[curr]]#add next nodes into queue

def dfs(graph,root,whatToFind):
    stack = []
    stack.append(root)#put the first element in the stack, so we can explore it latter on
    while stack:#while there are elements in the stack
        curr = stack.pop()
        print curr
        if whatToFind == curr:
            print 'found!'
            return#we have found what we are looking for
        if curr in graph:#if the current node has adjacent nodes
            [stack.append(adjacent) for adjacent in graph[curr]]#add next nodes into queue            
            

graph = {
            "human" : ["chicken","pig","shark"],
            "shark" : ["nemo","batfish"],
            "batfish" : ["tuna"],

            "pig" : ["apple","mush"],
            "chicken" : ["grass","grains"]
        }

print '===BFS==='
bfs(graph,"human","batfish")

print '===DFS==='
dfs(graph,"human","batfish")
