from pprint import pprint

def build_stack(text):
    stack = []
    for line in text.split("\n"):
        if not line:
            continue

        level = line.count("|")
        name = line.split("-", 1)[1].strip() # the part after the -
        stack = stack[:level] + [name] # update the stack: everything up to level-1 and name
        yield stack[:level], name # this is a generator

#for bottom_stack, name in build_stack(data):
    #print (bottom_stack + [name])

def create_tree(text):
    tree = {}
    for stack, name in build_stack(text):
        temp = tree
        for n in stack: # find or create...
            temp = temp.setdefault(n, {}) # ...the most inner dict
        temp[name] = {}
    return tree


def format(tree):
    L = []
    for name, subtree in tree.items():
        group, artifact, packaging, version, scope = name.split(":")
        d = {"artifact":artifact} # you can add group, ...
        v = {"version":version} 
        if subtree: # children are present
            d["children"] = format(subtree)
        L.append(d)
        L.append(v)
    return L

#***************************************************************************#

f = open("dependency_tree.txt", "r")
data = f.read();
pprint(format(create_tree(data)))
