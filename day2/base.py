
reports = []
with open("input.txt") as f:
  reports = f.readlines()

countsafe = 0
for report in reports:
  levels = report.split(" ")
  levels = [int(level) for level in levels]
  copy_levels = levels.copy()
  
  if levels[-1] > levels[0]:
    copy_levels.sort()
    
    if copy_levels == levels: 
      safe = True 
      #print("in first check")
      for i in range(len(levels)-1):
        difference = levels[i+1] - levels[i]
        if difference > 3 or difference < 1:
          safe = False
          break
      
      if safe:
        countsafe += 1
  
  if levels[-1] < levels[0]:
    copy_levels.sort(reverse=True)
    if copy_levels == levels:
      safe = True
      #print("in second check")
      for i in range(len(levels)-1):
        difference = abs(levels[i+1] - levels[i])
        if difference > 3 or difference < 1:
          safe = False
          break
      if safe:
        countsafe += 1
        
print(countsafe)

##Part 2

countsafe = 0
for report in reports:
  levels = report.split(" ")
  levels = [int(level) for level in levels]
  
  for i in range(len(levels)):
    levels2 = levels.copy()
    levels2.pop(i)
    copy_levels = levels2.copy()
    
    #print(levels2)
    if levels2[-1] > levels2[0]:
      copy_levels.sort()
      if copy_levels == levels2: 
        safe = True 
        
        #print("in first check")
        for i in range(len(levels2)-1):
          difference = levels2[i+1] - levels2[i]
          if difference > 3 or difference < 1:
            safe = False
            break
        
        if safe:
          countsafe += 1
          break
    
    if levels2[-1] < levels2[0]:
      copy_levels.sort(reverse=True)
      if copy_levels == levels2:
        safe = True
        #print("in second check")
        for i in range(len(levels2)-1):
          difference = abs(levels2[i+1] - levels2[i])
          if difference > 3 or difference < 1:
            safe = False
            break
        if safe:
          countsafe += 1
          break
          
print(countsafe)
      
      
      