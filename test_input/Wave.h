//

//  Wave.h

//  Cocos2D Tower Defense

#include "cocos2d.h"
#include "Creep.h"
USING_NS_CC;
class Wave: public CCNode
{
public:
	float _spawnRate;
	int _totalCreeps;
	Creep * _creepType;
	//float spawnRate();
	//void setspawnRate(float value);
	//int totalCreeps();
	//void settotalCreeps(int value);
	//Creep *  creepType();
	//void setcreepType(Creep *  value);
	Wave *  initWithCreepSpawnRateTotalCreeps(Creep * creep,float spawnrate,int totalcreeps);
};
