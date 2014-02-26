#ifndef CBTRIS_MENU_H__
#define CBTRIS_MENU_H__
#include "cocos2d.h"
using namespace cocos2d;

class CClickableSprite :public CCSprite,public CCStandardTouchDelegate
{
public:
	void onEnter()
	{
		CCSprite::onEnter();
		CCTouchDispatcher::sharedDispatcher()->addStandardDelegate(this,0);
	}

	void onExit()
	{
		CCTouchDispatcher::sharedDispatcher()->removeDelegate(this);
		CCSprite::onExit();
	}

	bool containsTouchLocation(CCTouch *pTouch)
	{
		CCSize s = getContentSize(); 
		return CCRect::CCRectContainsPoint(CCRectMake(-s.width / 2, -s.height / 2, s.width, s.height),convertTouchToNodeSpaceAR(pTouch));
	}

};

class MenuListener
{
public:
	virtual void OnMenuClick(int aID) = 0;
};

class CImageMenuEx :public CClickableSprite
{
public:
	static CImageMenuEx* spriteWithTexture(CCTexture2D *pTexture)
	{
		CImageMenuEx *pobSprite = new CImageMenuEx();
		pobSprite->initWithTexture(pTexture);
		pobSprite->autorelease();

		return pobSprite;
	}

	static CImageMenuEx* spriteWithTexture(CCTexture2D *pTexture, CCRect rect)
	{
		CImageMenuEx *pobSprite = new CImageMenuEx();
		pobSprite->initWithTexture(pTexture, rect);
		pobSprite->autorelease();

		return pobSprite;
	}


	static CImageMenuEx* spriteWithFile(const char *pszFileName)
	{
		CImageMenuEx *pobSprite = new CImageMenuEx();
		pobSprite->initWithFile(pszFileName);
		pobSprite->autorelease();

		return pobSprite;
	}

	static CImageMenuEx* spriteWithFile(const char *pszFileName, CCRect rect)
	{
		CImageMenuEx *pobSprite = new CImageMenuEx();
		pobSprite->initWithFile(pszFileName, rect);
		pobSprite->autorelease();

		return pobSprite;
	}

	static CImageMenuEx* spriteWithSpriteFrame(CCSpriteFrame *pSpriteFrame)
	{
		CImageMenuEx *pobSprite = new CImageMenuEx();
		pobSprite->initWithSpriteFrame(pSpriteFrame);
		pobSprite->autorelease();

		return pobSprite;
	}

	static CImageMenuEx* spriteWithSpriteFrameName(const char *pszSpriteFrameName)
	{
		CCSpriteFrame *pFrame = CCSpriteFrameCache::sharedSpriteFrameCache()->spriteFrameByName(pszSpriteFrameName);
		return spriteWithSpriteFrame(pFrame);
	}

	CImageMenuEx():pListener(0)
	{

	}

	virtual void OnClick()
	{

		if(pListener)
			pListener->OnMenuClick(iID);
	}

	virtual void ccTouchesBegan(CCSet *pTouches, CCEvent *pEvent) 
	{
		if(!pTouches||!pTouches->count())
			return;
		CCTouch* pTouch = (CCTouch*)(*(pTouches->begin()));
		if(containsTouchLocation(pTouch))
			setScale((1.1f));
	}

	virtual void ccTouchesMoved(CCSet *pTouches, CCEvent *pEvent) 
	{
		if(!pTouches||!pTouches->count())
			return;
		CCTouch* pTouch = (CCTouch*)(*(pTouches->begin()));
		if(containsTouchLocation(pTouch))
		{
			setScale((1.1f));
		}
		else
		{
			setScale((1.0f));
		}
	}

	virtual void ccTouchesEnded(CCSet *pTouches, CCEvent *pEvent) 
	{
		if(!pTouches||!pTouches->count())
			return;
		CCTouch* pTouch = (CCTouch*)(*(pTouches->begin()));
		setScale((1.0));
		if(containsTouchLocation(pTouch))
		{
			OnClick();
		}	
	}

	virtual void ccTouchesCancelled(CCSet *pTouches, CCEvent *pEvent) 
	{
		setScale((1.0));
	}

public:
	void SetID(int aID)
	{
		iID = aID;
	}

	void SetListener(MenuListener* aListenner)
	{
		pListener = aListenner;
	}

private:
	int				iID;
	MenuListener*	pListener;
};
#endif