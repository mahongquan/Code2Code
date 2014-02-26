#ifndef _MYmenuitemsprite_H_
#define _MYmenuitemsprite_H_
#include "cocos2d.h"
using namespace cocos2d;
class MyMenuItemSprite :public CCMenuItemSprite
{
public:
	MyMenuItemSprite(char * fname, CCObject* target, SEL_MenuHandler selector);
	~MyMenuItemSprite();
private:

};
#endif