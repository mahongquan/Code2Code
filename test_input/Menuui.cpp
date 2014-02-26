#include "MenuUI.h"
MenuUI * MenuUI::gen()
{
	MenuUI * m=new MenuUI();
	m->autorelease();
	return m;
}
MenuUI::MenuUI()
{
	CCSprite * bg=CCSprite::spriteWithFile("ui.png");
	bg->setAnchorPoint(ccp(0,0));
	addChild(bg);
	CCLabelTTF * about1 = CCLabelTTF::labelWithString("money","Aria",14);
	about1->setColor(ccc3(255,0,0));
	about1->setPosition(ccp(20,36+23+23));
	about1->setAnchorPoint(ccp(0,0));
	addChild(about1);
	CCLabelTTF * lifes = CCLabelTTF::labelWithString("lifes","Aria",14);
	lifes->setPosition(ccp(20,36+23));
	lifes->setAnchorPoint(ccp(0,0));
	addChild(lifes);
	CCLabelTTF * waves = CCLabelTTF::labelWithString("waves","Aria",14);
	waves->setPosition(ccp(20,36));
	waves->setAnchorPoint(ccp(0,0));
	addChild(waves);

	//CCSprite::initWithFile("compressor.png");
	//genLeft(70+12);
	//genLeft(227+12);
}
//void MenuUI::genLeft(CCSprite *p,int x)
//{
//	for (int i = 0; i < 12; i++)
//	{
//		CCSprite *left=CCSprite::spriteWithFile("compressorBody.png");
//		p->addChild(left);//70 227
//		left->setPosition(ccp(x,34+28 * (i + 1)));
//	}
//}
//
