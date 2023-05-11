import ast

tree = ast.parse('def hello_world():\n    print("Hello, World!")')

print(ast.dump(tree, indent=4))
