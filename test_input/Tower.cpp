//

//  Creep.m

//  Cocos2D Tower Defense

#include "Tower.h"
#include "Creep.h"
#include "DataModel.h"
#include "Projectile.h"

Creep * Tower::getClosestTarget()
{
	Creep *closestCreep=NULL; double maxDistant=99999;
	DataModel * m=DataModel::getModel();
	for(int i=0;i<m->_targets->count();i++)
		//for( CCSprite* target in m->_targets)
	{
		Creep *creep=(Creep *)m->_targets->getObjectAtIndex(i); 
		double curDistance=ccpDistance(this->getPosition(),creep->getPosition());
		if(curDistance<maxDistant){
			closestCreep=creep;
			maxDistant=curDistance;
		}
	}
	if(maxDistant<this->_range)
		return closestCreep;
	return NULL;
}
MachineGunTower *  MachineGunTower::tower()
{ 
	MachineGunTower *tower=new MachineGunTower();
	if(tower!=NULL)
	{tower->initWithFile("MachineGunTurret.png");
	tower->autorelease();
	tower->_range=100;
	tower->setScale(0.5f);
	tower->_target=NULL;
	tower->_speed=0.2;
	tower->schedule(schedule_selector(MachineGunTower::towerLogic),tower->_speed);
	}
	return tower;
}
bool  MachineGunTower::init()
{
	//if((self=super.init)){
	//	//[[CCTouchDispatcher sharedDispatcher] addTargetedDelegate:self priority:0 swallowsTouches:true];
	//}
	//return self;
	return true;
}
void MachineGunTower::toggleTowerAnimation()
{ 
	this->schedule(schedule_selector(MachineGunTower::towerLogic),this->_speed);
}
void MachineGunTower::setClosestTarget(Creep * closestTarget)
{ 
	this->_target=closestTarget;
}
void MachineGunTower::towerLogic(ccTime dt)
{ 
	this->_target=this->getClosestTarget();
	if(this->_target!=NULL)
	{//rotate the tower to face the nearest creep
		CCPoint shootVector=ccpSub(this->_target->getPosition(),this->getPosition());
		CGFloat shootAngle=ccpToAngle((shootVector));
		CGFloat cocosAngle=CC_RADIANS_TO_DEGREES((- 1*shootAngle));
		float rotateSpeed=0.2/M_PI;
		// 1/2 second to roate 180 degrees
		float rotateDuration=fabs((shootAngle*rotateSpeed));
		this->runAction(
			CCSequence::actions(
			CCRotateTo::actionWithDuration(rotateDuration,cocosAngle),
			CCCallFunc::actionWithTarget(this,callfunc_selector(MachineGunTower::finishFiring))			,NULL
			)
			);
	}
}
void MachineGunTower::creepMoveFinished(CCNode * sender)
{ 
	DataModel *m=DataModel::getModel(); 
	CCSprite *sprite=(CCSprite *)sender; 
	this->getParent()->removeChild(sprite,true);
	m->_projectiles->removeObject((Projectile *)sprite);
}
void MachineGunTower::finishFiring()
{ 
	DataModel *m=DataModel::getModel(); 
	this->_nextProjectile=Projectile::projectile();
	this->_nextProjectile->setPosition(this->getPosition());
	this->getParent()->addChild(this->_nextProjectile,1);
	m->_projectiles->addObject(this->_nextProjectile);
	ccTime delta=0.1;
	//determines  projectile speed
	CCPoint shootVector=ccpSub(this->_target->getPosition(),this->getPosition());
	CCPoint normalizedShootVector=ccpNormalize((shootVector));
	CCPoint overshotVector=ccpMult(normalizedShootVector,320);
	CCPoint offscreenPoint=ccpAdd(this->getPosition(),overshotVector);
	this->_nextProjectile->runAction(
		CCSequence::actions(
			CCMoveTo::actionWithDuration(delta,offscreenPoint),
			CCCallFuncN::actionWithTarget(this,callfuncN_selector(MachineGunTower::creepMoveFinished)),
			NULL
		)
	);
	this->_nextProjectile->setTag(2);
	this->_nextProjectile=NULL;
}
