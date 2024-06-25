
def rotateLeft(d, arr):

    return arr[d:] + arr[:d]

def rotateLeft(d, arr):

    n_arr = []
    m_arr = arr.copy()
    for i in range(len(arr)):
        if i <= d - 1:
            n_arr.append(arr[i])
            m_arr.remove(arr[i])
    return m_arr + n_arr




arr = [1, 2, 3, 4, 5]
d = 4
n_arr = []
m_arr = arr.copy()
for i in range(len(arr)):
    if i <= d - 1:
        n_arr.append(arr[i])
        m_arr.remove(arr[i])

print(rotateLeft(d, arr), arr[d:] + arr[:d])
