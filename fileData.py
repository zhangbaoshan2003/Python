f1 = open(r'c:\Artifacts\checkOmQAStatus.sh')
cLines = f1.readlines();
print("%d \n %s" %(len(cLines),cLines))
f1.close()

for i in range(0,len(cLines)):
    cLines[i] = str(i)+cLines[i]


f1=open(r"c:\Artifacts\check.sh","w")
f1.writelines(cLines)
f1.close()

f1 = open(r'c:\Artifacts\check.sh')
print(f1.readlines())
f1.close()