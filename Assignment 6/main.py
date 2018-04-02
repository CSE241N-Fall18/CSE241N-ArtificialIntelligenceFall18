from Graph import *
import pickle


graphfile = open('graphdata.pkl', 'rb')
g = pickle.load(graphfile)
bfs_list = list(g.bfs_paths(0,8))
dfs_list = list(g.dfs_paths(0 ,8))
print (len(bfs_list))
print(g.bfs_paths(0,8))
print(g.dfs_paths(0,8))
bfs_pickle = open('bfs_result.pkl', 'wb')
pickle.dump(bfs_list, bfs_pickle)

dfs_pickle = open('dfs_result.pkl', 'wb')
pickle.dump(dfs_list, dfs_pickle)

