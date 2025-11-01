digits = {
    ' _ | ||_|': '0',
    '     |  |': '1',
    ' _  _||_ ': '2',
    ' _  _| _|': '3',
    '   |_|  |': '4',
    ' _ |_  _|': '5',
    ' _ |_ |_|': '6',
    ' _   |  |': '7',
    ' _ |_||_|': '8',
    ' _ |_| _|': '9'
}
seg_map = {v: k for k, v in digits.items()}
num_segs = list(digits.keys())
def get_num(s):
    n = len(s[0]) // 3
    res = []
    for i in range(n):
        key = ''
        for j in range(3):
            key += s[j][i * 3:(i + 1) * 3]
        res.append(digits[key])
    return res
def toggle_digit(cur):
    idx = int(cur)
    cur_seg = seg_map[cur]
    mn = None
    for d, s in digits.items():
        if s == cur:
            continue
        diff = sum(1 for a, b in zip(cur_seg, d) if a != b)
        if diff == 1:
            if mn is None or int(s) < int(mn):
                mn = s
    return mn
def find_min_toggles(digits, K):
    n = len(digits)
    result = digits[:]
    used = 0
    for i in range(n):
        mn = toggle_digit(result[i])
        if used < K and mn is not None:
            if int(mn) < int(result[i]):
                result[i] = mn
                used += 1
    return result
def next_permutation(arr):
    arr = arr[:]
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1:
        return arr
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = arr[i+1:][::-1]
    return arr
import sys
inp = []
for _ in range(3):
    inp.append(sys.stdin.readline().rstrip('\n'))
K = int(sys.stdin.readline())
digits_list = get_num(inp)
orig = int(''.join(digits_list))
mod_num = find_min_toggles(digits_list, K)
mod_str = ''.join(mod_num)
nxt = next_permutation(list(mod_str))
while nxt == list(mod_str):
    nxt = next_permutation(nxt)
ans = int(''.join(nxt))
print(abs(orig - ans))
