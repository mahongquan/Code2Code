//

//  DataModel.h

//  Cocos2D Tower Defense
#ifndef _datamodel_H_
#define _datamodel_H_
#include "cocos2d.h"
//#include "Projectile.h"
//#include "Tower.h"
//#include "Wave.h"
//#include "WayPoint.h"

USING_NS_CC;
class Tower;
class Projectile;
class Wave;
class WayPoint;
class Creep;
class DataModel	: public CCObject
{
public:
	~DataModel();
	CCLayer *_gameLayer;
	CCNode *_gameHUDLayer;
	CCLayer* _towerSelectHUDLayer;
	CCLayer* _pauseHUDLayer;
	CCLayer* _scoreHUDLayer;
	CCMutableArray<Projectile*> *_projectiles;
	CCMutableArray<Tower*> *_towers;
	CCMutableArray<Creep *> *_targets;
	CCMutableArray<WayPoint*> *_waypoints;
	CCMutableArray<Wave *> *_waves;
	//UIPanGestureRecognizer *_gestureRecognizer;
	//CCLayer *  _gameLayer();
	//void set_gameLayer(CCLayer *  value);
	//CCLayer *  _gameHUDLayer();
	//void set_gameHUDLayer(CCLayer *  value);
	//CCLayer *  _towerSelectHUDLayer();
	//void set_towerSelectHUDLayer(CCLayer *  value);
	//CCLayer *  _pauseHUDLayer();
	//void set_pauseHUDLayer(CCLayer *  value);
	//CCLayer *  _scoreHUDLayer();
	//void set_scoreHUDLayer(CCLayer *  value);
	//CCMutableArray<Projectile*> *  _projectiles();
	//void set_projectiles(CCMutableArray<Projectile*> *  value);
	//CCMutableArray<Tower*> *  _towers();
	//void set_towers(CCMutableArray<Tower*> *  value);
	//CCMutableArray<Creep *> *  _targets();
	//void set_targets(CCMutableArray<Creep*> *  value);
	//CCMutableArray<WayPoint *> *  _waypoints();
	//void set_waypoints(CCMutableArray<WayPoint*> *  value);
	//CCMutableArray<Wave*> *  _waves();
	//void set_waves(CCMutableArray<Wave*> *  value);
	//UIPanGestureRecognizer *  _gestureRecognizer();
	//void set_gestureRecognizer(UIPanGestureRecognizer *  value);
	static DataModel* getModel();
	static DataModel* _sharedContext;
	DataModel();
};
#endif