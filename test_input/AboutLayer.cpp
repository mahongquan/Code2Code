#include "AboutLayer.h"
#include "SysMenu.h"
AboutLayer::AboutLayer():CCLayer()
{
	CCSize winSize = CCSizeMake(320,480);
	//winSize();
	int t=1;
	std::string text = "弹射泡泡龙，通过发射泡泡击落相同颜色的泡泡，采用物理引擎提高画面的真实性，发射碰撞效果非常给力。游戏分简单和困难两种模式，简单模式下发射的泡泡的颜色只从冻结的泡泡的颜色中随机选，困难模式下下发射的泡泡的颜色从全部8种颜色中随机选。";

	CCLabelTTF * about1 = CCLabelTTF::labelWithString(text.c_str(),CCSizeMake(winSize.width*0.85f ,480),CCTextAlignmentLeft,"Aria",14);
	
	about1->setPosition(ccp(160,300));
	addChild(about1);

	std::string text2 = "软件作者：马红权\n 邮箱：mahongquan@sina.com \nQQ：370182851 \n新浪微博：weibo.com/mahongquan";
	CCLabelTTF *author = CCLabelTTF::labelWithString(text2.c_str(),CCSizeMake(winSize.width * 0.85f ,150),CCTextAlignmentLeft,"Aria",14);
	author->setPosition(ccp(winSize.width/2,160));
	addChild(author);

	std::string text3 = "返回";
	CCLabelTTF *label= CCLabelTTF::labelWithString(text3.c_str(), "Aria", 14);
	CCMenuItem* back = CCMenuItemLabel::itemWithLabel(label, this, menu_selector(AboutLayer::backCallback));
	CCMenu *menu = CCMenu::menuWithItem(back);
	menu->setPosition(ccp(winSize.width/2,50));
	addChild(menu);
}

void AboutLayer::backCallback(CCObject* pSender) {
	CCScene *scene = CCScene::node();
	scene->addChild(SysMenu::node());
	CCDirector::sharedDirector()->replaceScene(CCTransitionFade::transitionWithDuration(1.2, scene));
}

CCLayer* AboutLayer::node() {
	CCLayer* sg = new AboutLayer();
	return sg;
}
