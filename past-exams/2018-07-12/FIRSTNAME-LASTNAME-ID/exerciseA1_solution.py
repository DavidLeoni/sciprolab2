import pandas as pd
from matplotlib import pyplot as plt



def loadData(filename):
        data = pd.read_csv(filename,
                     sep="\t", header = 0)
        
        print("The file \"{}\" contains {} positions".format(filename, data.shape[0]))

        [mean,m,M,std] = [data['Depth'].mean(), data['Depth'].min(), data['Depth'].max(),data['Depth'].std()]
        print("Dept min:{}\nDepth max:{}\nDepth mean: {} (std:{})".format(m,M,mean,std))
        
        grouped = data.groupby("Chromosome")
        grouped_avg = grouped.aggregate(pd.DataFrame.mean)['Depth']
        
        grouped_avg.plot(kind = "bar", title ="Average depth per chr")

        plt.show()
        return data

def classifyRegions(data, avgDepth, stdDepth):
    highThr = avgDepth + 2*stdDepth
    lowThr = avgDepth - 2*stdDepth
    allDepths = data['Depth']
    classes = []
    for el in allDepths:
        if(el > highThr):
            classes.append("High")
        else:
            if(el <lowThr):
                classes.append("Low")
            else:
                classes.append("Normal")
    
    data["Coverage class"] = classes
    
    grouped = data.groupby("Chromosome")
    for i,g in grouped:
        print("{}".format(i))
        cnts = g['Coverage class'].value_counts()
        for name in cnts.index:
            print(" - {} : {} ".format(name, cnts[name]))
    return data

dF = loadData("readDepths.tsv")

newDF = classifyRegions(dF,27.78,5.3)

print(newDF[newDF["Chromosome"] == "Chr13"].head(20010).tail(3))
print(newDF[newDF["Chromosome"] == "Chr13"].head(20000).tail(3))
print(newDF[newDF["Chromosome"] == "Chr13"].head(19000).tail(3))
