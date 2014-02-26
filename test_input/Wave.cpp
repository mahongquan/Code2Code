//

//  Wave.m

//  Cocos2D Tower Defense

#include "Wave.h"
//Wave *  Wave::init()
//{
//	if((self=super.init)){}return self;
//}
Wave *  Wave::initWithCreepSpawnRateTotalCreeps(Creep * creep,float spawnrate,int totalcreeps)
{ 
	//NSAssert (creep!=NULL,@"Invalid creep for wave.");
	//if((self=this->init))
	//CCNode::init();
	{
	_creepType=creep;
	_spawnRate=spawnrate;
	_totalCreeps=totalcreeps;
	}
	return this;
}
