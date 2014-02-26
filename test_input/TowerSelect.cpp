#include "TowerSelect.h"
TowerSelect * TowerSelect::gen()
{
	TowerSelect * m=new TowerSelect();
	m->autorelease();
	return m;
}
TowerSelect::TowerSelect()
{
	CCSprite * bg=CCSprite::spriteWithFile("uiselect.png");
	bg->setAnchorPoint(ccp(0,0));
	addChild(bg);
	
	CCLabelTTF * about1 = CCLabelTTF::labelWithString("basic","Aria",14);
	about1->setColor(ccc3(255,0,0));
	about1->setPosition(ccp(20,237));
	about1->setAnchorPoint(ccp(0,0));
	addChild(about1);

	CCLabelTTF * lifes = CCLabelTTF::labelWithString("laser","Aria",14);
	lifes->setPosition(ccp(20,237-25));
	lifes->setAnchorPoint(ccp(0,0));
	addChild(lifes);

	CCLabelTTF * mid = CCLabelTTF::labelWithString("mid","Aria",14);
	mid->setPosition(ccp(20,237-25*2));
	mid->setAnchorPoint(ccp(0,0));
	addChild(mid);

	CCLabelTTF * waves = CCLabelTTF::labelWithString("multi","Aria",14);
	waves->setPosition(ccp(20,56));
	waves->setAnchorPoint(ccp(0,0));
	addChild(waves);

	//CCSprite::initWithFile("compressor.png");
	//genLeft(70+12);
	//genLeft(227+12);
}
//void TowerSelect::genLeft(CCSprite *p,int x)
//{
//	for (int i = 0; i < 12; i++)
//	{
//		CCSprite *left=CCSprite::spriteWithFile("compressorBody.png");
//		p->addChild(left);//70 227
//		left->setPosition(ccp(x,34+28 * (i + 1)));
//	}
//}
//
