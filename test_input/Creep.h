//

//  Creep.h

//  Cocos2D Tower Defense
#ifndef _creep_H_
#define _creep_H_
#include "cocos2d.h"
//#include "DataModel.h"
#include "WayPoint.h"
USING_NS_CC;
class Creep: public CCSprite
{
public:
	int _curHp;
	int _moveDuration;
	int _inflictedDamage;
	int _curWaypoint;
	bool _causedDamage;
	static Creep * creepWithCreep(Creep * copyFrom);
	WayPoint * getCurrentWaypoint();
	WayPoint * getNextWaypoint();
	void creepLogic(float dt);
};
class FastRedCreep	: public Creep
{
public:
	static FastRedCreep *  creep();
};
class StrongGreenCreep	: public Creep
{
public:
	static StrongGreenCreep *  creep();
};
#endif