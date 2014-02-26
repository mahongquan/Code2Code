#ifndef AboutLayer_H
#define AboutLayer_H
#include "cocos2d.h"
#include "global.h"
using namespace cocos2d;
class AboutLayer :public  CCLayer 
{
public :
	AboutLayer();
	void backCallback(CCObject* pSender);
	static CCLayer* node();
};
#endif