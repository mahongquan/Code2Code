//

//  Projectile.m

//  Cocos2D Tower Defense

#include "Projectile.h"
Projectile *  Projectile::projectile()
{
	Projectile * s=new Projectile();
	s->initWithFile("Projectile.png");
	s->autorelease();
	return s;
}

