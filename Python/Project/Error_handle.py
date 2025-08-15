# 1
file=open("youtube.txt","w")
try:
    file.write("Hii Mayur")
finally:
    file.close()

# 2
with open("youtube.txt","w") as file:
    file.write("Hii Rudra")

###### Both 1 and 2 are same ######