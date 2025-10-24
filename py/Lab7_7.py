lines = ['one', 'two', 'three']
with open('Lab7.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')