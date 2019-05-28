import astor
from requests.auth import HTTPDigestAuth
import astpretty
import ast


# astpretty.pprint(ast.parse('if x == y: y += 4').body[0])
test = ast.parse('if x == y: y += 4')

print(ast.dump(test))
dir()
