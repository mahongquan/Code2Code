#ifndef _SYSMENU_H_
#define _SYSMENU_H_
#include "cocos2d.h"
using namespace cocos2d;
class SysMenu :public  CCLayer {//miss public
public:
	SysMenu();
	//virtual bool init();

	void functionNewGame(CCObject* pSender);
	void onNewGame();
	//void onSettings(CCObject* pSender);
	void onAbout(CCObject* pSender);
	//void update(float dt);
	static CCLayer* node();
	static CCScene* scene();
	//void onButtonEffect();
	//void removeIt();
	CCSize winSize;
	virtual void keyBackClicked();//
	virtual void keyMenuClicked();//Android
	//virtual void onEnter();
	//virtual void onExit();
};
#endif