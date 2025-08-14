records = {
    "data": [
        {"id": 1, "name": "Alice", "score": 91},
        {"id": 2, "name": "Bob", "score": 85},
        {"id": 3, "name": "Charlie", "score": 88}
    ]
}

def get_top_students(val, limit):
    ans = []
    for it in val.get("data", []):
        if it["score"] > limit:
            ans.append(it["name"])
    return ans

print(get_top_students(records, 87))