"""
st = open("test.txt", "w")
st.write("test write\n")
st.write("test write2")
st.close()
"""

with open("test.txt", "w") as f:
    f.write("Hello!")