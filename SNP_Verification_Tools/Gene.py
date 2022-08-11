from . import SNP
from . import InDel
from . import dnaTranslate
class Gene:
    def __init__(this, name, sequence, infoString):
        this.name = name[:name.find('|')]
        this.fullName = name + "|RequiresSNPConfirmation"
        this.sequence = sequence.upper()
        if "Nuc" in infoString:
            this.translated = None
        else:
            this.translated = dnaTranslate(this.sequence, name)

        this.listOfHyperSNPs = []
        this.listOfMisSNPs = []
        this.listOfNonsenseSNPs = []
        this.listOfMultSNPs = []
        this.frameshiftInfo = None
        this.isThereANonstop = (False, None)
        this.listOfDel = []
        this.listOfIns = []
        this.listOfMusts = None
        this.geneTag = 'N'
        this.outputInfo = dict()
        this.additionalInfo = list()

        infoList = infoString.split('|')
        for info in infoList:
            if "Nonstop" in info:
                if info[:4] == "Mult":
                    snpToAdd = SNP.SNP_Mis(this.translated, info[9:info.find(";")], this.name)
                    if (snpToAdd.isValid()):
                        this.isThereANonstop = (True, snpToAdd)
                else:
                    this.isThereANonstop = (True, None)
            elif info[:4] == "Mult":
                snpToAdd = SNP.SNP_Mult(this.translated, info[5:], this.name)
                if(snpToAdd.isValid()):
                    this.listOfMultSNPs.append(snpToAdd)
            elif info[:3] == "Mis":
                snpToAdd = SNP.SNP_Mis(this.translated, info[4:], this.name)
                if(snpToAdd.isValid()):
                    this.listOfMisSNPs.append(snpToAdd)
            elif info[:3] == "Del":
                indelToAdd = InDel.Deletion(this.translated, info[4:], this.name)
                if(indelToAdd.isValid()):
                    this.listOfDel.append(indelToAdd)
            elif info[:3] == "Ins":
                indelToAdd = InDel.Insertion(this.translated, info[4:], this.name)
                if(indelToAdd.isValid()):
                    this.listOfIns.append(indelToAdd)
            elif info[:5] == "Hyper":
                snpToAdd = SNP.SNP_Mult(this.translated, info[6:], this.name)
                if(snpToAdd.isValid()):
                    this.listOfHyperSNPs.append(snpToAdd)
                this.geneTag = 'H'
            elif info[:3] == "FS-":
                this.frameshiftInfo = info[3:]
                this.geneTag = 'S' if this.name == "MEG_6094" else 'F'
            elif info[:7] == "NucMult":
                snpToAdd = SNP.SNP_Mult(this.sequence, info[8:], this.name)
                if(snpToAdd.isValid()):
                    this.listOfMultSNPs.append(snpToAdd)
            elif info[:6] == "NucDel":
                indelToAdd = InDel.Deletion(this.sequence, info[7:], this.name, True)
                if(indelToAdd.isValid()):
                    this.listOfDel.append(indelToAdd)
            elif info[:3] == "Nuc":
                snpToAdd = SNP.SNP_Mis(this.sequence, info[4:], this.name, True)
                if(snpToAdd.isValid()):
                    this.listOfMisSNPs.append(snpToAdd)
            elif info[:4] == "Must":
                this.listOfMusts = SNP.MustList(info[5:], this.name)
                this.geneTag = 'I'
            else: #temp[:3] == "Nonsense" 
                snpToAdd = SNP.SNP_Non(this.translated, info[9:], this.name)
                if(snpToAdd.isValid()):
                    this.listOfNonsenseSNPs.append(snpToAdd)
        if (this.geneTag == 'N') or (this.geneTag == 'F'):
            for i in range(0,12):
                this.outputInfo.update({i,0})
        elif (this.geneTag == 'I'):
            for i in range(0,10):
                this.outputInfo.update({i,0})
        elif (this.geneTag == 'S'):
            for i in range(0,14):
                this.outputInfo.update({i,0})
        else:
            for i in range(0,13):
                this.outputInfo.update({i,0})

    def getOutputInfo(this):
        return this.outputInfo
    def clearOutputInfo(this):
        for key in this.outputInfo:
            this.outputInfo[key] = 0
    def getGeneTag(this):
        return this.geneTag
    def addToOutputInfo(this, index):
        this.outputInfo[index] += 1
    def addDetails(this, read, info):
        if read is this.additionalInfo[-1][0]:
            temp = list(this.additionalInfo[-1])
            temp.append(info)
            this.additionalInfo[-1] = tuple(temp)
        else:
            this.additionalInfo.append((read, info))
    def getLastTupleInfo(this):
        return this.additionalInfo[-1]
    def redefineLastTupleInfo(this):
        toRedefine = this.additionalInfo.pop()
        toRedefine = list(toRedefine)
        toRedefine[0] == toRedefine[0].query_name
        for i in range(1,len(toRedefine)):
            if type(toRedefine[i]) == tuple:
                toRedefine[i] = toRedefine[i][-1]
            elif toRedefine[i] == "hypersusceptible":
                toRedefine[i] = "Hypersusceptible: " + toRedefine[i][-1][5:]
        this.additionalInfo.append(toRedefine)
    def mustSuppressFrameshift(this):
        if this.geneTag != 'S':
            return False
        elif 'C insert' not in this.additionalInfo:
            return False
        return True

    def aaSequence(this):
        return this.translated
    def ntSequence(this):
        return this.sequence

    def condensedMultInfo(this):
        condensedInfoList = []
        for snp in this.listOfMultSNPs :
            condensedInfoList.append(snp.condensedInfo())
        return condensedInfoList
    def condensedHyperInfo(this):
        return this.listOfHyperSNPs[0].condensedInfo()
    def condensedMisInDelInfo(this):
        condensedInfoList = []
        for snp in this.listOfMisSNPs :
            condensedInfoList.append(snp.condensedInfo())
        for snp in this.listOfIns:
            condensedInfoList.append(snp.condensedInfo())
        for snp in this.listOfDel :
            condensedInfoList.append(snp.condensedInfo())
        return condensedInfoList
    def condensedNonInfo(this):
        condensedInfoList = []
        for snp in this.listOfNonsenseSNPs :
            condensedInfoList.append(snp.condensedInfo())
        return condensedInfoList
    def getNonstopInfo(this):
        return this.isThereANonstop
    def getFrameshiftInfo(this):
        return this.frameshiftInfo
    def getFirstMustBetweenParams(this, begin, end):
        if this.listOfMusts == None:
            return None
        return this.listOfMusts.getFirstMustBetweenParams(begin, end)

    def getName(this):
        return this.name
    def getFullName(this):
        return this.fullName
    def ntSeqLength(this):
        return len(this.sequence)
    def aaOrNu(this):
        return this.listOfMusts.returnAaOrNu()
    def rRna(this):
        return (("16S" in this.fullName) or ("23S" in this.fullName)) and (this.name != "MEG_6144") 