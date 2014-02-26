//

//  TutorialLayer.m

//  Cocos2D Tower Defense

// Import the interfaces

#include "TutorialScene.h"
#include "GameHUD.h"
#include "CCSprite.h"
#include "DataModel.h"
#include "MenuUI.h"
#include "towerSelect.h"
// Tutorial implementation

CCScene  *  Tutorial::scene()
{// 'scene' is an autorelease object.
	CCScene * scene=CCScene::node();
	// 'layer' is an autorelease object.
	Tutorial * layer=Tutorial::node();
	// add layer as a child to scene
	scene->addChild(layer,1);
	//layer->gameHUD=new GameHUD();

		// return the scene
	return scene;
}
bool  Tutorial::init()
{
	if (!CCLayer::init() )
	{
		return false;
	}
	//CCSprite * bg=CCSprite::spriteWithFile("Paper.jpg");
	//bg->setAnchorPoint(ccp(0,0));
	//addChild(bg,0);
	MenuUI * menuui=MenuUI::gen();
	this->addChild(menuui,2);
	menuui->setPosition(ccp(410,275));

	TowerSelect * ts=TowerSelect::gen();
	this->addChild(ts,2);
	ts->setPosition(ccp(410,10));

	this->setIsTouchEnabled(true);
	_time=0;lastTimeTargetAdded=0;
	this->_tileMap=CCTMXTiledMap::tiledMapWithTMXFile("mytilemap.tmx");

	this->_tileMap->setAnchorPoint(ccp(0,0));

	this->addChild(_tileMap,0);
	this->addWaypoint();
	this->addWaves();
	// Call game logic about every second
	this->schedule(schedule_selector(Tutorial::update));
	this->schedule(schedule_selector(Tutorial::gameLogic),1.0);
	this->_currentLevel=0;
	//this->setPosition( ccp(-228, -122));
	//this->setPosition(ccp(0,25));

	return true;
}
void Tutorial::addWaves()
{
	DataModel *m=DataModel::getModel();
	Wave *wave=new Wave();
	wave->initWithCreepSpawnRateTotalCreeps(FastRedCreep::creep(),0.3,5);
	wave->autorelease();
	m->_waves->addObject(wave);
	//wave=NULL;
	Wave * wave2=new Wave();wave2->autorelease();
	wave2->initWithCreepSpawnRateTotalCreeps(StrongGreenCreep::creep(),1.0,3);
	m->_waves->addObject(wave2);
}
Wave * Tutorial::getCurrentWave()
{
	DataModel *m=DataModel::getModel();
	Wave *wave=(Wave *) m->_waves->getObjectAtIndex(this->_currentLevel)	;
	return wave;
}
Wave * Tutorial::getNextWave()
{ 
	DataModel *m=DataModel::getModel(); 
	this->_currentLevel++;
	if(this->_currentLevel>1) 
		this->_currentLevel=0;
	Wave * wave=(Wave *)m->_waves->getObjectAtIndex(this->_currentLevel);
	return wave;
}
void Tutorial::addWaypoint()
{ 
	DataModel *m=DataModel::getModel(); 
	CCTMXObjectGroup *objects=this->_tileMap->objectGroupNamed("Objects"); 
	WayPoint *wp=NULL; 
	int wayPointCounter=0;
	char a[20];
	cocos2d::CCStringToStringDictionary * wayPoint;
	while(true)
	{ 
		sprintf(a,"Waypoint%d",wayPointCounter);
		wayPoint=objects->objectNamed(a);
		if (wayPoint==NULL) break;
		CCString * x=wayPoint->objectForKey("x");//.intValue;
		int x1=x->toInt();
		CCString * y=wayPoint->objectForKey("y");//.intValue;
		int y1=y->toInt();
		wp=(WayPoint *)WayPoint::node();
		wp->setPosition(ccp(x1,y1));
		m->_waypoints->addObject(wp);
		wayPointCounter++;
	} 
	//NSAssert (m._waypoints.count>0,@"Waypoint objects missing");
	//DLog (@"Okay, we've got %d waypoints",m._waypoints.count);
	//wp=NULL;
}
CCPoint Tutorial::tileCoordForPosition(CCPoint position)
{ 
	int x=position.x/this->_tileMap->getTileSize().width;
	int y=((this->_tileMap->getMapSize().height*this->_tileMap->getTileSize().height)-position.y)/this->_tileMap->getTileSize().height;
	return ccp(x,y);
}
bool Tutorial::canBuildOnTilePosition(CCPoint pos)
{ 
	CCPoint towerLoc=this->tileCoordForPosition(pos);
	int tileGid=this->_background->tileGIDAt(towerLoc);
	CCStringToStringDictionary * props=this->_tileMap->propertiesForGID(tileGid);
	CCString * type=props->objectForKey("buildable");
	if(type->toInt()==1)
		//if(type->isEqual("1"))
	{
		return true;
	}
	return false;
}
void Tutorial::addTower(CCPoint pos)
{ 
	DataModel *m=DataModel::getModel(); 
	Tower *target=NULL; 
	CCPoint towerLoc=this->tileCoordForPosition(pos);
	int tileGid=this->_background->tileGIDAt(towerLoc);
	CCStringToStringDictionary * props=this->_tileMap->propertiesForGID(tileGid);
	//DLog (@"dict value %@",props);
	CCString * type=props->objectForKey("Buildable");
	//DLog (@"Buildable: %@",type);
	if(type->toInt()==1){
		target=MachineGunTower::tower();
		target->setPosition(ccp((towerLoc.x*20)+16,this->_tileMap->getContentSize().height-(towerLoc.y*20)-16));
		this->addChild(target,1);
		target->setTag(1);
		m->_towers->addObject(target);
	}
	else
	{ 
		//DLog (@"Tile Not Buildable");
	}
}
void Tutorial::addTarget()
{
	DataModel *m=DataModel::getModel(); 
	Wave *wave=getCurrentWave();
	if(wave->_totalCreeps<=0)
	{
		this->getNextWave();
		return ;//[self getNextWave];
	}
	wave->_totalCreeps--;
	Creep * target=NULL;
	target=Creep::creepWithCreep(wave->_creepType);

	WayPoint * waypoint=target->getCurrentWaypoint();
	target->setPosition(waypoint->getPosition());
	waypoint=target->getNextWaypoint();
	this->addChild(target,1);
	float distance=ccpDistance(target->getPosition(),waypoint->getPosition());
	float moveDuration=(distance*target->_moveDuration)/400.0;
	cocos2d::CCFiniteTimeAction * actionMove=CCMoveTo::actionWithDuration(moveDuration,waypoint->getPosition());
	CCAction * actionMoveDone=CCCallFuncN::actionWithTarget(this,callfuncN_selector(Tutorial::FollowPath));
	target->runAction(CCSequence::actions(actionMove,actionMoveDone,NULL));
	// Add to targets array
	target->setTag(1);
	m->_targets->addObject(target);
}
void Tutorial::FollowPath(CCNode * sender)
{ 
	Creep *creep=(Creep *)sender; 
	WayPoint *waypoint=creep->getNextWaypoint(); 
	if(creep->_causedDamage)
	{
		//this->toremove.push_back(creep);
	}
	else
	{
		float distance=ccpDistance(creep->getPosition(),waypoint->getPosition());
		if(distance==0){return ;}
		float moveDuration=(distance*creep->_moveDuration)/400.0;
		CCMoveTo * actionMove=CCMoveTo::actionWithDuration(moveDuration,waypoint->getPosition());
		CCCallFuncN * actionMoveDone=CCCallFuncN::actionWithTarget(creep,callfuncN_selector(Tutorial::FollowPath));

		creep->stopAllActions();
		creep->runAction(CCSequence::actions(actionMove,actionMoveDone,NULL));
	}
}
void Tutorial::gameLogic(ccTime dt)
{
	_time++;
	DataModel *m = DataModel::getModel();
	Wave * wave=this->getCurrentWave();
	if(lastTimeTargetAdded=0|| _time-lastTimeTargetAdded>=wave->_spawnRate)
	{ 
		this->addTarget();
		lastTimeTargetAdded=_time;
	}
}
void Tutorial::update(ccTime dt)
{
	DataModel *m=DataModel::getModel();
	int n=m->_targets->count();
	toremove.clear();
	for(int i=0;i<n;i++)
	{
		Creep * creep=m->_targets->getObjectAtIndex(i);
		if(creep->_causedDamage)
		{

			toremove.push_back(creep);
		}
		else
		{
		}
	}
	for(int i=0;i<toremove.size();i++)
	{
		this->removeChild(toremove[i],true);
		m->_targets->removeObject(toremove[i]);
	}
	
}
CCPoint Tutorial::boundLayerPos(CCPoint newPos)
{ 
	CCSize winSize=CCDirector::sharedDirector()->getWinSize();//.winSize;
	CCPoint retval=newPos;
	retval.x=MIN(retval.x,0);
	retval.x=MAX(retval.x, _tileMap->getContentSize().width+winSize.width);
	retval.y=MIN(0,retval.y);
	retval.y=MAX( _tileMap->getContentSize().height+winSize.height,retval.y);
	//    DLog(@"boundLayerPos %d", retval);
	return retval;
}
void Tutorial::ccTouchesBegan(CCSet *pTouches, CCEvent *pEvent) 
{
	cocos2d::CCLog("tutorial: touch begin");
	if(!pTouches||!pTouches->count())
		return;
	CCTouch* touch = (CCTouch*)(*(pTouches->begin()));
	CCPoint location = touch->locationInView(touch->view());
	CCPoint pointT = CCDirector::sharedDirector()->convertToGL(location);
}
void Tutorial::ccTouchesMoved(CCSet *pTouches, CCEvent *pEvent) 
{
	cocos2d::CCLog("tutorial: touch move");
	if(!pTouches||!pTouches->count())
		return;
	CCTouch* touch = (CCTouch*)(*(pTouches->begin()));
	CCPoint location = touch->locationInView(touch->view());
	CCPoint pointT = CCDirector::sharedDirector()->convertToGL(location);
}
void Tutorial::ccTouchesEnded(CCSet *pTouches, CCEvent *pEvent) {
	cocos2d::CCLog("tutorial: touch end");
	if(!pTouches||!pTouches->count())
		return;
	CCTouch* touch = (CCTouch*)(*(pTouches->begin()));
	CCPoint location = touch->locationInView(touch->view());
	CCPoint pointT = CCDirector::sharedDirector()->convertToGL(location);

}
void Tutorial::ccTouchesCancelled(CCTouch *pTouches, CCEvent *pEvent) 
{


}
//void Tutorial::handlePanFrom()
//{
//	return ;//XXX TODO 
//if(recognizer.state==UIGestureRecognizerStateBegan){ 
//	CCPoint touchLocation=recognizer.locationInView:recognizer.view;
//	touchLocation=CCDirector.sharedDirector.convertToGL:touchLocation;
//	touchLocation=this->convertToNodeSpace:touchLocation;
//}
//elseif(recognizer.state==UIGestureRecognizerStateChanged){ 
//	CCPoint translation=recognizer.translationInView:recognizer.view;
//	translation=ccp((translation.x,- translation.y));
//	CCPoint newPos=ccpAdd((this->position,translation));
//	this->position=this->boundLayerPos:newPos;
//	recognizer.setTranslation:CGPointZeroinView:recognizer.view;
//}
//elseif(recognizer.state==UIGestureRecognizerStateEnded){ 
//	float scrollDuration=0.2;
//	CCPoint velocity=recognizer.velocityInView:recognizer.view;
//	CCPoint newPos=ccpAdd((this->position,ccpMult((ccp((velocity.x,velocity.y*- 1)),scrollDuration))));
//	newPos=this->boundLayerPos:newPos;
//	this->stopAllActions;
//	CCMoveTo * moveTo=CCMoveTo.actionWithDuration:scrollDurationposition:newPos;
//	this->runAction:CCEaseOut.actionWithAction:moveTorate:1;
//}
//}
//void Tutorial::dealloc()
//{ super.dealloc;
//}
