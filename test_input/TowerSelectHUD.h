//

//  TowerSelectHUD.h

//  TowerDefenseTutorial

//

//  Created by Buford Taylor on 7/6/11.

//  Copyright 2011 __MyCompanyName__. All rights reserved.

//
#ifndef _towerselect_H_
#define _towerselect_H_
#include "cocos2d.h"
USING_NS_CC;
class TowerSelectHUD
	: public CCLayer
{
public:
	CCSprite * background;
	CCSprite * selSpriteRange;
	CCSprite * selSprite;
	bool hidden;
	CCMutableArray<CCSprite *> * movableSprites;
	static TowerSelectHUD * sharedHUD();
	void toggleTSHUDwithSpeed(float speed);
	virtual bool init();
	LAYER_NODE_FUNC(TowerSelectHUD);
	
	static TowerSelectHUD *  _sharedHUD;
};
#endif