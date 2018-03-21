import pickle
for i in range(10000):
    name = "data" + str(i) + ".txt"
    f = open(name, 'w')
    pickle.dump(range(10000), f)
    f.close()