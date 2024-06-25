Pattern="*"
start = 0
end= 6
peak = 3

for i in range(1, end +1):
 print(Pattern * (start+ i))

for i in range (1,end + 1):
 if i>0:
  print(Pattern * (end-i))
else: print(Pattern * i)
print(i)