#include "SysMenu.h"
#include "AboutLayer.h"
//#include "SettingsLayer.h"
#include "SimpleAudioEngine.h"
#include "MyButton.h"
#include "MyMenuItemSprite.h"
#include "TutorialScene.h"

using namespace cocos2d;
SysMenu::SysMenu():CCLayer() {
	this->setIsKeypadEnabled(true);
	winSize = CCSizeMake(600,400);
	cocos2d::CCSprite* sp1 = CCSprite::spriteWithFile("Paper.jpg");
	sp1->setPosition(ccp(winSize.width/2,winSize.height/2));
	this->addChild(sp1,-1);

	cocos2d::CCSprite* sp2 = CCSprite::spriteWithFile("Monsters.png");
	this->addChild(sp2, 0);
	sp2->setAnchorPoint(cocos2d::CCPointZero);
	sp2->setPosition(ccp(10,10));

	cocos2d::CCSprite* sp3 = CCSprite::spriteWithFile("title.png");
	this->addChild(sp3, 0);
	sp3->setAnchorPoint(cocos2d::CCPointZero);
	sp3->setPosition(ccp(350,300));
	sp3->setScale(1.5f);

	/*MyButton * b1=new MyButton("begin");
	b1->setAnchorPoint(cocos2d::CCPointZero);
	addChild(b1);
	b1->setPosition(ccp(385,250));
	MyButton * b2=new MyButton("more");
	b2->setAnchorPoint(cocos2d::CCPointZero);
	addChild(b2);
	b2->setPosition(ccp(385,200));*/

	CCSprite* newGameNormal = CCSprite::spriteWithFile("Button.png",
		CCRectMake(0, 0, 140, 25));
	CCSprite *newGameSelected = CCSprite::spriteWithFile("Button.png",
		CCRectMake(0, 25, 140, 25));
	CCSprite *newGameDis = CCSprite::spriteWithFile("Button.png",
		CCRectMake(0, 25, 140, 25));
	CCLabelTTF * about1 = CCLabelTTF::labelWithString("Start Game",CCSizeMake(100,25),CCTextAlignmentCenter,"Aria",20);
	about1->setColor(ccc3(0,0,0));
	CCMenuItemSprite* newGame = CCMenuItemSprite::itemFromNormalSprite(newGameNormal,
		newGameSelected, newGameDis, this, menu_selector(SysMenu::functionNewGame));
	//about1->setAnchorPoint(cocos2d::CCPointZero);
	about1->setPosition(ccp(70,12.5));
	newGame->addChild(about1);
	CCSprite* newGameNormal2 = CCSprite::spriteWithFile("Button2.png",
		CCRectMake(0, 0, 140, 25));
	CCSprite *newGameSelected2 = CCSprite::spriteWithFile("Button2.png",
		CCRectMake(0, 25, 140, 25));
	CCSprite *newGameDis2 = CCSprite::spriteWithFile("Button2.png",
		CCRectMake(0, 25, 140, 25));
	CCLabelTTF * about = CCLabelTTF::labelWithString("About",CCSizeMake(100,25),CCTextAlignmentCenter,"Aria",20);
	CCMenuItemSprite* aboutM = CCMenuItemSprite::itemFromNormalSprite(newGameNormal2,
		newGameSelected2, newGameDis2, this, menu_selector(SysMenu::onAbout));
	//about->setAnchorPoint(cocos2d::CCPointZero);
	about->setPosition(ccp(70,12.5));
	about->setColor(ccc3(0,0,0));
	aboutM->addChild(about);
	//MyMenuItemSprite * newGame=new MyMenuItemSprite("test",this,menu_selector(SysMenu::functionNewGame));
	/*CCMenuItemSprite *about = CCMenuItemSprite::itemFromNormalSprite(newGameNormal,
		newGameSelected, newGameNormal, this, menu_selector(SysMenu::onAbout));*/

	CCMenu *menu = CCMenu::menuWithItems(newGame,aboutM,NULL);
	menu->alignItemsVertically();
	this->addChild(menu, 1, 2);
	menu->setPosition(ccp(480,250 ));
}


void SysMenu::functionNewGame(CCObject* pSender) {
	//onButtonEffect();
	onNewGame();
}
//
void SysMenu::onNewGame() {
	CCScene *scene = Tutorial::scene();
	CCDirector::sharedDirector()->replaceScene(CCTransitionFade::transitionWithDuration(1.2f, scene));
}
//void SysMenu::onButtonEffect(){
//	if (global_sound) {
//		//var s = cc.AudioManager.sharedEngine().playEffect(s_buttonEffect);
//		CocosDenshion::SimpleAudioEngine::sharedEngine()->playEffect(s_buttonEffect);
//	}
//}


void SysMenu::onAbout(CCObject* pSender) {
	//this.onButtonEffect();
	CCScene* scene = CCScene::node();
	scene->addChild(AboutLayer::node());
	CCDirector::sharedDirector()->replaceScene(CCTransitionFade::transitionWithDuration(1.2,
	scene));
}
//

CCLayer* SysMenu::node() {
	SysMenu *sg = new SysMenu();
	//if(sg->init())
	//sg->setIsKeypadEnabled(true);
		return sg;
	//else
	//	return NULL;
}

CCScene *SysMenu::scene() {
	CCScene* scene = CCScene::node();
	CCLayer* layer = SysMenu::node();
	scene->addChild(layer);
	return scene;
}
void SysMenu::keyBackClicked(){


    CCLog("Android- KeyBackClicked!");
    CCDirector::sharedDirector()->end();
    #if (CC_TARGET_PLATFORM == CC_PLATFORM_IOS)
	exit(0);
    #endif
}
void SysMenu::keyMenuClicked(){
    CCLog("Android- keyMenuClicked!");
}
