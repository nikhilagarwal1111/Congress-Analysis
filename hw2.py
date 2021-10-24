import json
import matplotlib.pyplot as plt
import numpy as np


renddate2023=0
renddate2025=0
renddate2027=0
denddate2023=0
denddate2025=0
denddate2027=0
file= 'senators.json'
with open(file) as f:
    text = f.read()
    senators=json.loads(text) 
for senator in senators['objects']:  
    for key in senator:
        if key =='party':
            if senator['party']=='Republican':
                if senator['enddate']=='2023-01-03':
                    renddate2023+=1
                elif senator['enddate']=='2025-01-03':
                    renddate2025+=1
                elif senator['enddate']=='2027-01-03':
                    renddate2027+=1
            if senator['party']=='Democrat':
                if senator['enddate']=='2023-01-03':
                    denddate2023+=1
                elif senator['enddate']=='2025-01-03':
                    denddate2025+=1
                elif senator['enddate']=='2027-01-03':
                    denddate2027+=1
#rend_dates={'2023':renddate2023,'2025':renddate2025,'2027':renddate2027}
#dend_dates={'2023':denddate2023,'2025':denddate2025,'2027':denddate2027}

labels = ['2023', '2025', '2027']
r_end = [renddate2023, renddate2025, renddate2027]
d_end = [denddate2023, denddate2025, denddate2027]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, r_end, width, label='Republicans')
rects2 = ax.bar(x + width/2, d_end, width, label='Democrats')
ax.set_ylabel('Number of Senators')
ax.set_title('Bar Chart showing how many Senators are up for re-election in the next three General Elections')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)



rthirties=0
rfourties=0
rfifties=0
rsixties=0
rseventies=0
reighties=0
rnineties=0
dthirties=0
dfourties=0
dfifties=0
dsixties=0
dseventies=0
deighties=0
dnineties=0
file= 'representatives.json'
with open(file) as f:
    text = f.read()
    represenatives=json.loads(text)
for representative in represenatives['objects']:
    for key in representative:
        if key =='party':
            if representative['party']=='Republican':
                if '193' in representative['person']['birthday']:
                    rthirties+=1
                if '194' in representative['person']['birthday']:
                    rfourties+=1
                if '195' in representative['person']['birthday']:
                    rfifties+=1
                if '196' in representative['person']['birthday']:
                    rsixties+=1
                if '197' in representative['person']['birthday']:
                    rseventies+=1
                if '198' in representative['person']['birthday']:
                    reighties+=1
                if '199' in representative['person']['birthday']:
                    rnineties+=1
            if representative['party']=='Democrat':
                if '193' in representative['person']['birthday']:
                    dthirties+=1
                if '194' in representative['person']['birthday']:
                    dfourties+=1
                if '195' in representative['person']['birthday']:
                    dfifties+=1
                if '196' in representative['person']['birthday']:
                    dsixties+=1
                if '197' in representative['person']['birthday']:
                    dseventies+=1
                if '198' in representative['person']['birthday']:
                    deighties+=1
                if '199' in representative['person']['birthday']:
                    dnineties+=1


rbirthdecades={'30s':rthirties,'40s':rfourties,'50s':rfifties,'60s':rsixties,'70s':rseventies,'80s':reighties,'90s':rnineties}
dbirthdecades={'30s':dthirties,'40s':dfourties,'50s':dfifties,'60s':dsixties,'70s':dseventies,'80s':deighties,'90s':dnineties}                     
xs = sorted(rbirthdecades.keys()) 
ys= [rbirthdecades[x] for x in xs]
fig, ax = plt.subplots()
plt.plot(xs,ys,label='Republicans')
x1 = sorted(dbirthdecades.keys())
y1= [dbirthdecades[x] for x in x1] 
plt.plot(x1,y1,label='Democrats')
plt.title('Line plot of the number of representatives born in each decade from both parties')
plt.xlabel('Decade')
plt.ylabel('Number of Representative')
leg = plt.legend(loc='upper right')
plt.show()




           
            
           


            

  
    
