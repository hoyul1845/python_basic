# 집합 (set)
# 중복 안됌, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할수있는 개발자)
print(java & python)
print(java.intersection(python))


print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))



python.add("김태호")
print(python)


java.remove("김태호")
print(java)