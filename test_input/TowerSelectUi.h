#ifndef _towerselectui_H_
#define _towerselectui_H_
#include "cocos2d.h"
#include "global.h"
using namespace cocos2d;
class MenuUI :public  CCSprite
{
public:
	MenuUI();
	static void genLeft(CCSprite *p,int x);
	static CCSprite * gen();
};
#endif