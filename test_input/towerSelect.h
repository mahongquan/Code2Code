#ifndef _towerselect_H_
#define _towerselect_H_
#include "cocos2d.h"
#include "global.h"
using namespace cocos2d;
class TowerSelect :public  CCNode
{
public:
	TowerSelect();
	//static void genLeft(CCSprite *p,int x);
	static TowerSelect * gen();
};
#endif