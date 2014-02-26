#ifndef _menuui_H_
#define _menuui_H_
#include "cocos2d.h"
#include "global.h"
using namespace cocos2d;
class MenuUI :public  CCNode
{
public:
	MenuUI();
	//static void genLeft(CCSprite *p,int x);
	static MenuUI * gen();
};
#endif