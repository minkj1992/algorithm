import multiprocessing as mp

length = int(input())

def read_api(i):
    value = read_character(i)
    if value == '!':
        return read_api(i)
    if value:
        return value


pool = mp.Pool(min(mp.cpu_count(),9))
results = pool.map(read_api, [i for i in length])
pool.close()

print(results)
