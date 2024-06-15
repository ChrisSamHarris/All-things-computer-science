### Graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque



def person_is_seller(name):
    # in this example we're going to pretend someone with a name ending in "m" is a mango seller
    return name[-1] == 'm'

def bfs(name):
    # Creates a new queue
    search_queue = deque()
    # adds all of your out-neighbors to the search queue
    search_queue += graph[name]
    searched = set()
    while search_queue:
        # grab the first person off the queue
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                # if the person isnt a mango seller, add all of their neighbors to the search queue
                search_queue += graph[person]
    return False

bfs("you")













