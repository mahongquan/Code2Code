//

//  Creep.m

//  Cocos2D Tower Defense

#include "DataModel.h"
#include "Creep.h"
//Creep *  Creep::copyWithZone(NSZone * zone)
//{ Creep *copy=[[[self class] allocWithZone:zone] initWithCreep:self];return copy;}
Creep * Creep::creepWithCreep(Creep * copyFrom)
{
	Creep *c=new Creep();
	//c->initWithFile("Enemy1.png");
	c->initWithTexture(copyFrom->getTexture());
	c->autorelease();
	//this->autorelease();
	c->_curHp=copyFrom->_curHp;
	c->_moveDuration=copyFrom->_moveDuration;
	c->_curWaypoint=(copyFrom->_curWaypoint);
	c->_inflictedDamage=(copyFrom->_inflictedDamage);
	c->_causedDamage=(copyFrom->_causedDamage);
	c->schedule(schedule_selector(Creep::creepLogic),0.2);
	//this->retain;
	return c;
}
WayPoint * Creep::getCurrentWaypoint()
{ 
	DataModel *m=DataModel::getModel(); 
	WayPoint *waypoint=(WayPoint *) m->_waypoints->getObjectAtIndex(_curWaypoint);
	return waypoint;
}
WayPoint * Creep::getNextWaypoint()
{ 
	DataModel *m=DataModel::getModel(); 
	int lastWaypoint=m->_waypoints->count();
	this->_curWaypoint++;
	if(this->_curWaypoint>=lastWaypoint){ 
		this->_causedDamage=true;
		this->_curWaypoint=0;
	} 
	CCMutableArray<WayPoint*> * a=m->_waypoints;
	WayPoint * waypoint=(WayPoint *)m->_waypoints->getObjectAtIndex(_curWaypoint);
	return waypoint;
}
void Creep::creepLogic(float dt)
{ 
	DataModel *m=DataModel::getModel();// Rotate creep to face next waypoint
	WayPoint * waypoint=this->getCurrentWaypoint();
	CCPoint waypointVector=ccpSub(waypoint->getPosition(),this->getPosition());
	CGFloat waypointAngle=ccpToAngle(waypointVector);
	CGFloat cocosAngle=CC_RADIANS_TO_DEGREES((- 1*waypointAngle));
	float rotateSpeed=0.5/M_PI;
	// 1/2 second to roate 180 degrees
	float rotateDuration=fabs((waypointAngle*rotateSpeed));
	this->runAction(CCSequence::actions(CCRotateTo::actionWithDuration(rotateDuration,cocosAngle),NULL));
}
FastRedCreep *  FastRedCreep::creep()
{ 
	FastRedCreep *creep=new FastRedCreep();
	creep->initWithFile("Enemy1.png");
	creep->autorelease();
	creep->_curHp=1;
	creep->_moveDuration=(1);
	creep->_curWaypoint=(0);
	creep->_inflictedDamage=(2);
	creep->_causedDamage=(false);
	creep->schedule(schedule_selector(Creep::creepLogic),0.2);
	return creep;

}
StrongGreenCreep *  StrongGreenCreep::creep()
{ 
	//StrongGreenCreep *creep=NULL;if((creep=super.alloc.initWithFile:@"Enemy2.png".autorelease))
	StrongGreenCreep *creep=new StrongGreenCreep();
	creep->initWithFile("Enemy2.png");
	creep->autorelease();
	creep->_curHp=1;
	creep->_moveDuration=(9);
	creep->_curWaypoint=(0);
	creep->_inflictedDamage=(1);
	creep->_causedDamage=(false);
	creep->schedule(schedule_selector(Creep::creepLogic),0.2);
	return creep;
}
