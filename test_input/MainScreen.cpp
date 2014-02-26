#include "MainScreen.h"
//#include "ResConvertor.h"
//#include "ResourceMgr.h"
#include "CCScheduler.h"

CMainScreen::CMainScreen(void)
{
}

CMainScreen::~CMainScreen(void)
{
}


void CMainScreen::onEnter()
{
	CCLayer::onEnter();	
	CCSize aSize = CCSizeMake(480,720);

	aStatus = emain;

	s_BK = CCSprite::spriteWithFile("spash.jpg");
	s_BK->setPosition(ccp(aSize.width/2, aSize.height/2));
	addChild(s_BK,0);
	
	
	{
		l_main_layer = CCLayer::node();
		s_main = CCSprite::spriteWithTexture(CResourceMgr::GetImage(BK_MAIN));
		s_main->setPosition(ccp(aSize.width/2, aSize.height/2));
		s_main->setScale(0.01f);
		s_main->setIsVisible(false);
		l_main_layer->addChild(s_main,0);

		s_menu_back= CImageMenuEx::spriteWithTexture(CResourceMgr::GetImage(BTN_BACK));
		s_menu_back->setPosition(ccp(aSize.width-40,50));
		s_menu_back->setIsVisible(false);
		s_menu_back->SetID(99);
		s_menu_back->SetListener(this);
		l_main_layer->addChild(s_menu_back,1);
	}



}


void CMainScreen::s_main_Action_callback()
{
	moveleft(l_menu_main,CCCallFunc::actionWithTarget(this,callfunc_selector(CMainScreen::s_menu_Action_callback)));
}

void CMainScreen::s_menu_Action_callback()
{
	CCActionInterval* s_menu_menu_fade = CCFadeIn::actionWithDuration(1);
	CCActionInterval* s_main_ease_out = CCScaleTo::actionWithDuration(12.0,(1.05f));
	CCActionInterval* s_main_ease_in = (CCScaleTo::actionWithDuration(12.0,(0.95f)));
	CCFiniteTimeAction* seq1 = CCSequence::actions(
		s_main_ease_out, 
		s_main_ease_in,
		NULL);
	s_menu_menu->setIsVisible(true);
	s_menu_menu->runAction(s_menu_menu_fade);
	s_main->runAction( CCRepeatForever::actionWithAction((CCActionInterval*)seq1));
}


void CMainScreen::s_menu_Action_quit()
{
	CCDirector::sharedDirector()->end();
}

inline void CMainScreen::moveleft(CCLayer* aLayer,CCCallFunc* selector)
{
	CCSize aSize = CCSizeMake(480,720);
	CCActionInterval* s_menu_ease_out = (CCActionInterval*)CCEaseElasticOut::actionWithAction(
		(CCActionInterval*)(CCMoveBy::actionWithDuration(0.5,(ccp( 0 - aSize.width, 0)))), 
		0.8f);
	CCFiniteTimeAction* seq1 = NULL;
	if(selector)
		seq1 =CCSequence::actions(
		s_menu_ease_out, 
		selector,
		NULL);
	else
		seq1 =CCSequence::actions(
		s_menu_ease_out, 
		NULL);
	aLayer->runAction((CCActionInterval*)seq1);
}

inline void CMainScreen::moveright(CCLayer* aLayer,CCCallFunc* selector)
{
	CCSize aSize = CCSizeMake(480,720);
	CCActionInterval* s_menu_ease_out = (CCActionInterval*)CCEaseElasticOut::actionWithAction(
		(CCActionInterval*)(CCMoveBy::actionWithDuration(0.5,(ccp( aSize.width, 0)))), 
		0.8f);

	CCFiniteTimeAction* seq1 = NULL;
	if(selector)
		seq1 =CCSequence::actions(
			s_menu_ease_out, 
			selector,
			NULL);
	else
		seq1 =CCSequence::actions(
		s_menu_ease_out, 
		NULL);
	aLayer->runAction((CCActionInterval*)seq1);
}

void CMainScreen::s_menu_In_mode_sel()
{
	s_menu_back->setIsVisible(true);
	s_menu_back->runAction( CCFadeIn::actionWithDuration(1));
}

void CMainScreen::OnMenuClick(int aID)
{
	switch (aID)
	{
	case 0:
		{
			l_menu_gamemode->setIsVisible(true);
			moveleft(l_menu_main);
			moveleft(l_menu_gamemode,CCCallFunc::actionWithTarget(this,callfunc_selector(CMainScreen::s_menu_In_mode_sel)));
			aStatus = emode;
		}
		break;
	case 1:break;
	case 2:break;
	case 3:break;
	case 4:
		{
			CCActionInterval* aAction = CCEaseIn::actionWithAction(CCScaleTo::actionWithDuration(0.3f,(0.1f)),3);
			CCFiniteTimeAction* seq1 = CCSequence::actions(
				aAction, 
				CCCallFunc::actionWithTarget(this, callfunc_selector(CMainScreen::s_menu_Action_quit)),
				NULL);
			l_main_layer->runAction(seq1);
		}break;
	case 5:
		{
			moveleft(l_menu_gamemode);
			moveleft(l_menu_mode0);
			aStatus = emode0;
		}break;
	case 50:
		{
			Game::show();
		}break;
	case 99:
		{
			if(aStatus == emode)
			{
				s_menu_back->setIsVisible(false);
				moveright(l_menu_main);
				moveright(l_menu_gamemode);
				aStatus = emain;
			}
			else if(aStatus == emode0)
			{
				moveright(l_menu_mode0);
				moveright(l_menu_gamemode);
				aStatus = emode;
			}
		}
		break;
	}
}