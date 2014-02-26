//

//  TutorialLayer.h

//  Cocos2D Tower Defense

// When you import this file, you import all the cocos2d classes
#ifndef _tutorialscene_H_
#define _tutorialscene_H_
#include "cocos2d.h"
#include "Creep.h"
#include "Projectile.h"
#include "Tower.h"
#include "WayPoint.h"
#include "Wave.h"
#include "GameHUD.h"
// Tutorial Layer
USING_NS_CC;
class Tutorial	: public CCLayer
{
public:
	int _time;
	int lastTimeTargetAdded;
	CCTMXTiledMap *_tileMap;
	CCTMXLayer *_background;
	int _currentLevel;
	GameHUD * gameHUD;
	static CCScene *  scene();
	void addWaves();
	void addWaypoint();
	void addTower(CCPoint pos);
	bool canBuildOnTilePosition(CCPoint pos);
	virtual bool init();
	LAYER_NODE_FUNC(Tutorial);
	Wave * getCurrentWave();
	Wave * getNextWave();
	void addTarget();
	void FollowPath(CCNode * sender);
	void gameLogic(ccTime dt);
	void update(ccTime dt);
	CCPoint boundLayerPos(CCPoint newPos);
	virtual void ccTouchesBegan(CCSet *pTouch, CCEvent *pEvent) ;
	 void ccTouchesMoved(CCSet *pTouches, CCEvent *pEvent) ;
	 	void ccTouchesEnded(CCSet *pTouches, CCEvent *pEvent) ;
		virtual void ccTouchesCancelled(CCTouch *pTouch, CCEvent *pEvent);

		CCPoint tileCoordForPosition(CCPoint position);
		std::vector<Creep *>  toremove;
};
#endif