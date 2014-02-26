//

//  PauseHUD.h

//  TowerDefenseTutorial

//

//  Created by Buford Taylor on 7/6/11.

//  Copyright 2011 __MyCompanyName__. All rights reserved.

//
#ifndef _pausehud_H_
#define _pausehud_H_
#include "cocos2d.h"
USING_NS_CC;
class PauseHUD	: public CCLayer
{
public:
	CCSprite * pauseButton;
	CCSprite * towerSelectButton;
	virtual bool init();
	LAYER_NODE_FUNC(PauseHUD);
	bool isPaused;
	bool shouldResumeAnimation;
	static PauseHUD * sharedHUD();
	static PauseHUD *  _sharedHUD;
};
#endif