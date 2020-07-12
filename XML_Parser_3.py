def build_stack(text):
    dependency_list = []
    for line in text.split("\n"):
        if not line:
            continue

        level = line.count("|")
        name = line.split("-", 1)[1].strip() # the part after the -
        dependency_list.append(name)
        
    return dependency_list


def list_to_set(dependency_list):
    return set(dependency_list)


def compare_dependencies(dependencyInfoSet1,dependencyInfoSet2):
    result= all(elem in dependencyInfoSet1  for elem in dependencyInfoSet2) and all(elem in dependencyInfoSet2  for elem in dependencyInfoSet1)
    if (result):
        print("Both containers can run on each other")
    elif (dependencyInfoSet1.issubset(dependencyInfoSet2)):
        print("Container one can run on container two")
    elif (dependencyInfoSet2.issubset(dependencyInfoSet1)):
        print("Container two can run on container one")
    else :
        print("May contain conflicting dependencies")

#************************************************************************#

service_1_dep = input("Input dependency file one: ")
service_2_dep = input("Input dependency file two: ")

f1 = open(service_1_dep, "r")
data1 = f1.read();

f2 = open(service_2_dep, "r")
data2 = f2.read();

dependencySet_1 = list_to_set(build_stack(data1))
dependencySet_2 = list_to_set(build_stack(data2))

compare_dependencies(dependencySet_1,dependencySet_2)
