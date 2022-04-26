#pragma once
#include <string>
#include <list>
#include "ModelSingle.h"

using namespace std;

class ModelNonsense : public virtual ModelSingle {
protected:
    char wt_aa = 0;
    virtual void makeModel(string line) = 0;
public:
    ModelNonsense();
    virtual string condensedSNPinfo() = 0;
};

ModelNonsense::ModelNonsense() {}