import pandas as pd

GameNumberArray=[]
FirstIndex=[]
Total_Values=[]

with open('input.txt','r') as file:
    while True:
        line=file.readline()
        if not line:
            break
        parts=line.split(":")
        if len(parts)==2:
            GameNumberArray.append(parts[0])
            FirstIndex.append(parts[1])

colon_seperate=str(FirstIndex).split(';')

df=pd.DataFrame({
    'Game Number':GameNumberArray
})

df['Values']=colon_seperate[0]


df.to_excel('Game Data.xlsx',index= False)        
            


        
        

