//

//  GameHUD.h

//  Cocos2D Tower Defense
#ifndef _gamehud_H_
#define _gamehud_H_
#include "cocos2d.h"
USING_NS_CC;
class GameHUD	: public CCNode, public CCTargetedTouchDelegate
{
public:
	CCSprite * background;
	CCSprite * selSpriteRange;
	CCSprite * selSprite;
	CCMutableArray<CCSprite *> * movableSprites;
	GameHUD();
	bool ccTouchBegan(CCTouch* touch, CCEvent* pevent);
	void ccTouchMoved(CCTouch* touch, CCEvent* pevent); 
	void ccTouchEnded(CCTouch* touch, CCEvent* pevent);

	virtual void onEnter();
	virtual void onExit();
	virtual void touchDelegateRetain();
	virtual void touchDelegateRelease();
	//void registerWithTouchDispatcher();
};
#endif