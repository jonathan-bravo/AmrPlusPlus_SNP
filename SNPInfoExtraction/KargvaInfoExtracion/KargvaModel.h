#pragma once
#include <string>
#include "../Model.h"
#include "../CARD_database.h"

using namespace std;

class KargvaModel : public virtual Model {
    protected:
        CARD_database* databaseSequences;
        string cardID = "";
        string addContext(int lastLeftIndex, int firstRightIndex, char wt);
    public:
        KargvaModel();
        KargvaModel(string id, CARD_database* dbSeq);
        virtual void addToModel(string line) = 0;
        virtual bool includes(string line) = 0;
        virtual string condensedSNPinfo() = 0;
};
KargvaModel::KargvaModel() {}

KargvaModel::KargvaModel(string id, CARD_database* dbSeq){
    cardID = id;
    databaseSequences = dbSeq;
}

string KargvaModel::addContext(int lastLeftIndex, int firstRightIndex, char wt) {
    string sequence = databaseSequences->getSequence(cardID);
    if (sequence == "none")
        return "__";
    if (wt != '-') {
        if (sequence.at(lastLeftIndex + 1) != wt)
            cout << cardID << "\n";
    }
    string toReturn = "_";
    int firstLeftIndex = lastLeftIndex - 4;
    if (lastLeftIndex < 4)
        firstLeftIndex = 0;
    int leftContextSize = lastLeftIndex - firstLeftIndex + 1;
    if (leftContextSize != 0)
        toReturn += sequence.substr(firstLeftIndex, leftContextSize);
    toReturn += "_";
    int lastRightIndex = firstRightIndex + 4;
    if (lastRightIndex > sequence.size() - 1)
        lastRightIndex = sequence.size() - 1;
    int rightContextSize = lastRightIndex - firstRightIndex + 1;
    if (rightContextSize != 0)
        toReturn += sequence.substr(firstRightIndex, rightContextSize);
    return toReturn;
}