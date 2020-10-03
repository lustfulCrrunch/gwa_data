import io 
import datetime as dt

files = ['xaa','xab','xac','xad']
allPosts = []
for file in files:
    contents = io.open(file,'r', encoding='utf-16-le') 
    contents = contents.read().split(":;:")
    i = 0
    while i < len(contents)-1:
        title = contents[i].strip()
        auth = contents[i+1]
        url = contents[i+2]
        date = int(contents[i+3])
        i += 4
        allPosts.append([title, auth, url, date])
allPosts = sorted(allPosts, key=lambda x: x[3])
byWeeks = [[] for i in range(433)] #weeks since june 2012
week = 604800 #a week in seconds
firstDay = allPosts[0][3]
nextWeek = firstDay + week
curr = 0

#Iterate over all posts, check their time stamp, and place them in their week index of byWeeks
for p in allPosts:
    if p[3] < nextWeek:
        byWeeks[curr].append(p)
    else:
        nextWeek = nextWeek + week
        curr += 1
    byWeeks[curr].append(p)
    
byWeekGroups = [{0:0, 1:0, 2:0, 3:0, 4:0, 5:0} for i in range(433)]
groups = [['[m4m]','[tm4m]','[m4tm]'], ['[m4a]'], ['[m4f]', '[tm4f]', '[M4TF]'], ['[f4m]', '[tf4m]', '[f4tm]'], ['verification']]


for w in range(len(byWeeks)):
    for p in byWeeks[w]:
        t = p[0].lower() #title
        #For all tag groups
        found = False
        for i in range(len(groups)):
            #For tag in this tag group
            for tag in groups[i]:
                if tag in t: #if tag is in the title
                    found = True
                    byWeekGroups[w][i] += 1
                    if(tag != '[m4a]'):
                        break;
        if(not found):
                byWeekGroups[w][5] += 1
#Print output for google sheets
for w in byWeekGroups:
    for (k,v) in w.items():
        print(str(v) + ":", end = '')
    print()
