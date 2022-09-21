#pragma once
#include <string>
#include <list>
#include "Model.h"

using namespace std;

class ModelInDel : public virtual Model {
protected:
	list<int> pos;
	virtual void makeModel(string line) = 0;
	virtual ~ModelInDel();
public:
	ModelInDel();
	virtual string condensedInfo() = 0;
};

ModelInDel::ModelInDel() {}
ModelInDel::~ModelInDel() {}