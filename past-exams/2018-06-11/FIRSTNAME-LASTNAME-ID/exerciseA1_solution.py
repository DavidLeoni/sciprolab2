"""sample_solution.py"""

import pandas as pd
import matplotlib.pyplot as plt



def loadData(filename):
        data = pd.read_csv(filename,
                     sep="\t", index_col = 0, header = 0)
        
        print("The file \"{}\" contains {} SNPs".format(filename, data.shape[0]))
        gc_count = data["GeneticChr"].value_counts()
        
        lgs = [str(x) for x in gc_count.index]
        
        print("\nData has information for the following {} linkage groups:".format(len(gc_count)))
        print("\t {}".format(",".join(lgs)))
        print("\nLG\tSNPcount")
        for el in gc_count.index:
            print("{}\t{}".format(el,gc_count[el]))
        
        pc_count = data["PhysicalChr"].value_counts()
        print("\nData has information for the following {} chromosomes:".format(len(pc_count)))
        chrs =  [str(x) for x in pc_count.index]
        print("\t {}".format(",".join(chrs)))
        print("\nChr\tSNPcount")
        for el in pc_count.index:
            print("{}\t{}".format(el,pc_count[el]))
        
        
        return data

def createMareyPlot(data, chrom):
    chrData = data[data['PhysicalChr'] == chrom][['GeneticChr','GeneticPos','PhysicalPos']]
    
    if(chrData.shape[0] > 0):
        LGcnt = set(chrData['GeneticChr'])
        lgs = list(LGcnt)
        outSTR = chrom + "\t"
        f = plt.figure()
        for i in range(0,len(lgs)):
            tmp = []
            pp = []
            gp = []

            tmp = chrData[chrData["GeneticChr"]==lgs[i]]
            pp = list(tmp["PhysicalPos"])
            gp = list(tmp["GeneticPos"])       

            plt.scatter(pp,gp, label=lgs[i])
            plt.xlabel("Physical pos [bps]")
            plt.ylabel("Genetic pos [cM]")
            plt.title(chrom)
            plt.legend()
            outSTR+="\t"+lgs[i] + ":" + str(len(pp))

        print("MareyPlot for {}".format(chrom))

        plt.show()
    
    else:
            print("No information on {}".format(chrom))
    
dF = loadData("map_info.tsv")
createMareyPlot(dF, "Chr11")
createMareyPlot(dF, "Chr8")
createMareyPlot(dF, "Chr0")
