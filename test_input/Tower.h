//

//  Creep.h

//  Cocos2D Tower Defense
#ifndef _tower_H_
#define _tower_H_
#include "cocos2d.h"
//#include "Creep.h"
//#include "SimpleAudioEngine.h"
//#include "Projectile.h"
//#include "DataModel.h"
USING_NS_CC;
class Projectile;
class Creep;
class Tower	: public CCSprite
{
public:
	int _range;
	float _speed;
	Creep * _target;
	CCSprite * selSpriteRange;
	CCMutableArray<Projectile *> *_projectiles;
	Projectile *_nextProjectile;
	Creep * getClosestTarget();
};
class MachineGunTower	: public Tower
{
public:
	static MachineGunTower *  tower();
	void setClosestTarget(Creep * closestTarget);
	void towerLogic(ccTime dt);
	void creepMoveFinished(CCNode *sender);
	void finishFiring();
	void toggleTowerAnimation();
	bool init();
};
#endif