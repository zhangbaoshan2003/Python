f= open(r"D:\Blowing in the wind.txt",'w')
f.writelines("How many roads must a man walk down\n")
f.writelines("Before they call him a man\n")
f.seek(0,0)
f.writelines("Blowin’ in the wind\n")
f.close()
f= open(r"D:\Blowing in the wind.txt");
content = f.readlines();
print(content)
f.close()