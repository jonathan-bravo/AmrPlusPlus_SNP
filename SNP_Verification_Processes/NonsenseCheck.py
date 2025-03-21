from SNP_Verification_Tools.Gene import Gene
from SNP_Verification_Tools.SNP import SNP
from SNP_Verification_Tools.InDel import InDel

def NonsenseCheck(read, gene, mapOfInterest, seqOfInterest):
    stopLocation = seqOfInterest.find('*') 
    #if nonsense mutations
    if (stopLocation != -1) & ((stopLocation < len(seqOfInterest)-1) | (read.reference_end < gene.ntSeqLength())): 
        return verifyNonsense(read, gene, stopLocation, mapOfInterest)
    return True

def verifyNonsense(read, gene, stopLocation, mapOfInterest):

    def findNonsenseLocation():
        values = list(mapOfInterest.values())
        referenceStopLocation = -1
        i = 0
        lastQueryIndex = values[0][0]-1
        for queryTuple in values:
            for queryIndex in queryTuple:
                if queryIndex == '-':
                    continue
                if stopLocation == queryIndex:
                    referenceStopLocation = list(mapOfInterest.keys())[i]
                    break
                elif stopLocation < queryIndex:
                    referenceStopLocation = list(mapOfInterest.keys())[i-1] + stopLocation - lastQueryIndex
                    break
                lastQueryIndex = queryIndex
            if referenceStopLocation != -1:
                break
            i+=1
        if referenceStopLocation == -1:
            referenceStopLocation = list(mapOfInterest.keys())[i-1] + stopLocation - lastQueryIndex
        gene.addDetails(read, "Newly found nonsense: " + str(referenceStopLocation+1))

    SNPInfo = gene.condensedNonInfo()
    if (len(SNPInfo) == 0) and (gene.getGeneTag() != 'F'):
        findNonsenseLocation()
        return False
    else:
        for snp in SNPInfo:
            stopLocTemp = mapOfInterest.get(snp[1]-1,False)
            if stopLocTemp != False:
                if stopLocTemp[0] == stopLocation:
                    gene.addDetails(read, snp)
                    return True
        
        findNonsenseLocation()
        return (gene.getGeneTag() == 'F')