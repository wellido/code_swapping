import astor
from requests.auth import HTTPDigestAuth
import astpretty
import ast

code = """
while i < l:
    cd = td[i][2] + ss[pi[i + 1]]
    if cd < ss[i]:
        ss[i + 1] = ss[i]
        f = f + [[0, i]]
    else:
        ss[i + 1] = cd
        f = f + [[1, pi[i + 1]]]
    i += 1

"""
# astpretty.pprint(ast.parse('if x == y: y += 4').body[0])
test = ast.parse(code)
# astpretty.pprint(test)
tt = ast.dump(test)
print(tt)
# dir()
