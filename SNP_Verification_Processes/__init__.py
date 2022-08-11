from SNP_Verification_Tools.Gene import Gene
from SNP_Verification_Processes.FrameshiftCheck import FrameshiftCheck
from SNP_Verification_Processes.MappingQueryToReference import MapQueryToReference
from SNP_Verification_Processes.NonsenseCheck import NonsenseCheck
from SNP_Verification_Processes.IntrinsicCheck import IntrinsicCheck
from SNP_Verification_Processes.MisInDelCheck import MisInDelCheck
from SNP_Verification_Processes.nTupleCheck import nTupleCheck
import pysam

def verify(read, gene):
    rRna = gene.rRna()
    gene.addToOutputInfo(0)                                                     #Counts read; other data will be counted in FinalCount method

                                                                                #Checks for frameshifts (if not rRNA), but also for extended indels;
    checkResult = FrameshiftCheck(read, gene, rRna)                             #for S-tagged, also determines if needs suppression
    if not(checkResult):                                                        #If not F-tagged and has frameshifts till the end of query sequence
        FinalCount(gene)
        return None                                
    
    seqOfInterest, mapOfInterest = MapQueryToReference(rRna, read, gene)        #If S-tagged and needs suppression, seq and map of interest, removes index 1602
    
    if not(rRna):                                                               #rRNA stays as nucleotide sequence; nonsense mutations don't matter   
        checkResult = NonsenseCheck(read, gene, mapOfInterest, seqOfInterest)   #Checks for nonsense previously found in literature and for new nonsense
        if not(checkResult):                                                    #If not F-tagged and has new nonsense, can't determine resistance
            FinalCount(gene)
            return None      
    
    IntrinsicCheck(read, gene, mapOfInterest, seqOfInterest)                    #For I-tagged specifically
    MisInDelCheck(read, gene, mapOfInterest, seqOfInterest)                     #Counts all resistance-conferring mutations
    nTupleCheck(read, gene, mapOfInterest, seqOfInterest)                       #Counts all resistance-conferring mutations
    FinalCount(gene)    


def FinalCount(gene):
    gene.redefineLastTupleInfo()
    additionalInfo = gene.getLastTupleInfo()
    def nTypeCount(): 
        insertion = False
        deletion  = False
        missense  = False
        nTuple    = False
        resistant = False
        for info in additionalInfo[1:]:
            if 'Mis:' in info:
                if not(missense):
                    gene.addToOutputInfo(2)
                    missense = True
                resistant = True
            elif 'Ins:' in info:
                if not(insertion):
                    gene.addToOutputInfo(3)
                    insertion = True
                resistant = True
            elif 'Del:' in info:
                if not(deletion):
                    gene.addToOutputInfo(4)
                    deletion = True
                resistant = True
            elif 'Nonsense:' in info:
                gene.addToOutputInfo(5)
                resistant = True
            elif 'Mult:' in info:
                if not(nTuple):
                    gene.addToOutputInfo(6)
                    nTuple = True
                resistant = True
            elif 'nonstop' == info:
                gene.addToOutputInfo(7)
                resistant = True
            elif '12+indel:' in info:
                gene.addToOutputInfo(8)
            elif '12+fs:' in info:
                gene.addToOutputInfo(9)
            elif "stop location at position " in info:
                gene.addToOutputInfo(10)
            elif 'FS end' == info:
                gene.addToOutputInfo(11)
        if resistant:
            gene.addToOutputInfo(1)

    def fTypeCount():
        insertion = False
        deletion  = False
        missense  = False
        nTuple    = False
        resistant = False
        for info in additionalInfo[1:]:
            if 'Mis:' in info:
                if not(missense):
                    gene.addToOutputInfo(2)
                    missense = True
                resistant = True
            elif 'Ins:' in info:
                if not(insertion):
                    gene.addToOutputInfo(3)
                    insertion = True
                resistant = True
            elif 'Del:' in info:
                if not(deletion):
                    gene.addToOutputInfo(4)
                    deletion = True
                resistant = True
            elif 'Nonsense:' in info:
                gene.addToOutputInfo(5)
                resistant = True
            elif 'Mult:' in info:
                if not(nTuple):
                    gene.addToOutputInfo(6)
                    nTuple = True
                resistant = True
            elif 'nonstop' == info:
                gene.addToOutputInfo(7)
                resistant = True
            elif '12+indel:' in info:
                gene.addToOutputInfo(8)
            elif '12+fs:' in info:
                gene.addToOutputInfo(9)
            elif "stop location at position " in info:
                gene.addToOutputInfo(10)
                resistant = True
            elif 'FS end' == info:
                gene.addToOutputInfo(11)
                resistant = True
        if resistant:
            gene.addToOutputInfo(1)

    def hTypeCount(): 
        insertion = False
        deletion  = False
        missense  = False
        nTuple    = False
        nonsense  = False
        nonstop   = False
        resistant = False
        for info in additionalInfo[1:]:
            if 'Mis:' in info:
                missense = True
                resistant = True
            elif 'Ins:' in info:
                insertion = True
                resistant = True
            elif 'Del:' in info:
                deletion = True
                resistant = True
            elif 'Nonsense:' in info:
                nonsense = True
                resistant = True
            elif 'Mult:' in info:
                nTuple = True
                resistant = True
            elif 'nonstop' == info:
                nonstop = True
                resistant = True
            elif '12+indel:' in info:
                gene.addToOutputInfo(8)
            elif '12+fs:' in info:
                gene.addToOutputInfo(9)
            elif "stop location at position " in info:
                gene.addToOutputInfo(10)
            elif 'FS end' == info:
                gene.addToOutputInfo(11)
            elif 'Hypersusceptible' in info:
                gene.addToOutputInfo(12)
                resistant = False
        if resistant:
            if missense:
                gene.addToOutputInfo(2)
            elif insertion:
                gene.addToOutputInfo(3)
            elif deletion:
                gene.addToOutputInfo(4)
            elif nonsense:
                gene.addToOutputInfo(5)
            elif nTuple:
                gene.addToOutputInfo(6)
            elif nonstop:
                gene.addToOutputInfo(7)
            gene.addToOutputInfo(1)

    def sTypeCount():
        insertion = False
        deletion  = False
        missense  = False
        nTuple    = False
        resistant = False
        for info in additionalInfo[1:]:
            if 'Mis:' in info:
                if not(missense):
                    gene.addToOutputInfo(2)
                    missense = True
                resistant = True
            elif 'Ins:' in info:
                if not(insertion):
                    gene.addToOutputInfo(3)
                    insertion = True
                resistant = True
            elif 'Del:' in info:
                if not(deletion):
                    gene.addToOutputInfo(4)
                    deletion = True
                resistant = True
            elif 'Nonsense:' in info:
                gene.addToOutputInfo(5)
                resistant = True
            elif 'Mult:' in info:
                if not(nTuple):
                    gene.addToOutputInfo(6)
                    nTuple = True
                resistant = True
            elif 'nonstop' == info:
                gene.addToOutputInfo(7)
                resistant = True
            elif '12+indel:' in info:
                gene.addToOutputInfo(8)
            elif '12+fs:' in info:
                gene.addToOutputInfo(9)
            elif "stop location at position " in info:
                gene.addToOutputInfo(10)
                resistant = False
            elif 'FS end' == info:
                gene.addToOutputInfo(11)
                resistant = False
            elif 'C insert' == info:
                gene.addToOutputInfo(12)
                resistant = True
            elif 'C insert + del/ins' == info:
                gene.addToOutputInfo(13)
                resistant = True
        if resistant:
            gene.addToOutputInfo(1)

    def iTypeCount(): 
        acquired = False
        some     = False
        none     = False
        mutant   = False
        for info in additionalInfo[1:]:
            if 'All' == info:
                gene.addToOutputInfo(1)
                break
            elif 'Some' == info:
                some = True
            elif 'NA' == info:
                none = True
            elif 'Mutant' == info:
                mutant = True
            elif 'Mis:' in info:
                gene.addToOutputInfo(5)
                acquired = True
                break
            elif '12+indel:' in info:
                gene.addToOutputInfo(6)
            elif '12+fs:' in info:
                gene.addToOutputInfo(7)
            elif "stop location at position " in info:
                gene.addToOutputInfo(8)
                resistant = False
            elif 'FS end' == info:
                gene.addToOutputInfo(9)
                resistant = False
        if not(acquired):
            if some:
                gene.addToOutputInfo(2)
            elif none:
                gene.addToOutputInfo(3)
            elif mutant:
                gene.addToOutputInfo(4)

    tag = gene.getGeneTag()
    if tag == 'N':
        nTypeCount()
    elif tag == 'F':
        fTypeCount()
    elif tag == 'H':
        hTypeCount()
    elif tag == 'S':
        sTypeCount()
    else:
        iTypeCount()