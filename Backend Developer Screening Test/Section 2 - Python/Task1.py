dataset = [
    {"department": "CS", "score": 85},
    {"department": "IT", "score": 92},
    {"department": "CS", "score": 78},
    {"department": "IT", "score": 88},
    {"department": "EC", "score": 75}
]

def func(val):
    score = {}
    ct = {}
    ans = {}
    
    for it in val:
        dept = it["department"]
        s = it["score"]
        
        score[dept] = score.get(dept, 0) + s
        ct[dept] = ct.get(dept, 0) + 1
    
    for it in score:
        ans[it] = score[it] / ct[it]
    return ans

print(func(dataset))
