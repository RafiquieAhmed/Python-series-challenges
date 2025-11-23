st={1,2,3,4,5,6,7,8,9,10}
print(type(st))

st.add(11)
print(st)
st.remove(5)
print(st)
print(st.clear())
st={1,2,3}
st.update([-1,0,-5])
print(st)
st.discard(1)
print(st)
st.pop()
print(st)
print(st.pop())
print(st)
a={1,2,3}
b={3,4,5}
print(a|b)#union
print(a&b) #intersect
print(a^b)