//

//  Projectile.h

//  Cocos2D Tower Defense
#ifndef _projectile_H_
#define _projectile_H_
#include "cocos2d.h"
USING_NS_CC;
class Projectile: public CCSprite
{
public:
	static Projectile *  projectile();
};
#endif