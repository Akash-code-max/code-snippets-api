from flask import Flask, jsonify

app = Flask(__name__)

# Step 1a: Add your code snippets here
snippets = {
    "GP1": "print('Hello from GP1')",
    "GP2": "for i in range(3): print(i)",
    "GP3": "def add(a,b): return a+b\nprint(add(2,3))",
    "GP4": "my_list = [1,2,3,4,5]\nfor n in my_list: print(n*n)",
    "GP5": "import math\nprint('Square root of 16 is', math.sqrt(16))"
}

# Step 1b: Create API endpoint
@app.route("/get_code/<name>")
def get_code(name):
    code = snippets.get(name, "Snippet not found!")
    return jsonify({"code": code})

# Step 1c: Run server for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
