import json

# Input JSON array
data = [{"name":"Alice","age":72},{"name":"Bob","age":28},{"name":"Charlie","age":32},{"name":"David","age":15},{"name":"Emma","age":85},{"name":"Frank","age":43},{"name":"Grace","age":70},{"name":"Henry","age":7},{"name":"Ivy","age":25},{"name":"Jack","age":39},{"name":"Karen","age":2},{"name":"Liam","age":66},{"name":"Mary","age":2},{"name":"Nora","age":72},{"name":"Oscar","age":14},{"name":"Paul","age":83}]

sorted_data = sorted(data, key=lambda x: (x["age"], x["name"]))

# Convert to JSON string without spaces or newlines
result = json.dumps(sorted_data, separators=(',', ':'))
print(result)