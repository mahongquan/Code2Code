#ifndef C_MAIN_SCREEN__
#define C_MAIN_SCREEN__

//#include "BTrisDefines.h"
#include "CBTrisMenu.h"
#include "cocos2d.h"
using namespace cocos2d;
class CMainScreen :public cocos2d::CCLayer, public MenuListener
{
public:
	CMainScreen(void);
	~CMainScreen(void);

	enum eStatus
	{
		emain = 0,
		emode,
		emode0,
	};
		
public:
	void onEnter();
	static void show();

private:
	inline void moveleft(CCLayer* aLayer,CCCallFunc* selector = NULL);
	inline void moveright(CCLayer* aLayer,CCCallFunc* selector = NULL);

public:
	void OnLoadingTimer(cocos2d::ccTime dt);
	void s_main_Action_callback();
	void s_menu_Action_callback();
	void s_menu_Action_quit();
	void OnMenuClick(int aID);
	void s_menu_In_mode_sel();

private:
	cocos2d::CCSprite*		s_BK;
	cocos2d::CCSprite*		s_main;
	cocos2d::CCSprite*		s_menu_menu;

	CImageMenuEx*			s_menu_back;
	eStatus					aStatus;

	CCLayer*				l_main_layer;
	CCLayer*				l_menu_main;
	CImageMenuEx*			s_menu_start;
	CImageMenuEx*			s_menu_setting;
	CImageMenuEx*			s_menu_help;
	CImageMenuEx*			s_menu_ranking;
	CImageMenuEx*			s_menu_exit;

	CCLayer*				l_menu_gamemode;
	CImageMenuEx*			s_menu_mode0;
	CImageMenuEx*			s_menu_mode1;
	CImageMenuEx*			s_menu_mode2;
	CImageMenuEx*			s_menu_mode3;
	
	CCLayer*				l_menu_mode0;
	CImageMenuEx*			s_btn_OK;
};

#endif