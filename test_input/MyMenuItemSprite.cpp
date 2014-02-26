#include "MyMenuItemSprite.h"
MyMenuItemSprite::~MyMenuItemSprite()
{
}
MyMenuItemSprite::MyMenuItemSprite(char * fname, CCObject* target, SEL_MenuHandler selector)
{
	CCSprite* newGameNormal = CCSprite::spriteWithFile("Button.png",
		CCRectMake(0, 0, 140, 25));
	CCSprite *newGameSelected = CCSprite::spriteWithFile("Button.png",
		CCRectMake(0, 25, 140, 25));
	CCSprite *newGameDis = CCSprite::spriteWithFile("Button.png",
		CCRectMake(0, 25, 140, 25));
	CCMenuItemSprite::itemFromNormalSprite(newGameNormal,
		newGameSelected, newGameDis, target,selector);
}

