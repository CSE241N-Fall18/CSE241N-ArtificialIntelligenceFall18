from Graph import *
import pickle


graphfile = open('graphdata.pkl', 'rb')
g = pickle.load(graphfile)
#print(g.graph)
bfs_list = list(g.bfs_paths(1, 8))
dfs_list = list(g.dfs_paths(1, 11))
#print(dfs_list)
#print(bfs_list)
print (len(dfs_list))
bfs_pickle = open('bfs_result.pkl', 'wb')
pickle.dump(bfs_list, bfs_pickle)

dfs_pickle = open('dfs_result.pkl', 'wb')
pickle.dump(dfs_list, dfs_pickle)

