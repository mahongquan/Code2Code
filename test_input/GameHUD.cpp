//

//  GameHUD.m

//  Cocos2D Tower Defense

#include "GameHUD.h"
#include "DataModel.h"
GameHUD::GameHUD():CCNode()

{
		//this->setIsTouchEnabled(true);
		CCSize winSize=CCDirector::sharedDirector()->getWinSize();
		//CCTexture2D.setDefaultAlphaPixelFormat:kCCTeture2DPixelFormat_RGB565;
		background=CCSprite::spriteWithFile("hud.png");
		background->setAnchorPoint(ccp(0,0));
		this->addChild(background);
		//CCTexture2D.setDefaultAlphaPixelFormat:kCCTexture2DPixelFormat_Default;
		movableSprites=new CCMutableArray<CCSprite *>();
		//CCArray * images=CCArray::array();
		std::vector<char *> images;
		images.push_back("MachineGunTurret.png");
		images.push_back("MachineGunTurret.png");
		images.push_back("MachineGunTurret.png");
		images.push_back("MachineGunTurret.png");
		//,"MachineGunTurret.png","MachineGunTurret.png","MachineGunTurret.png",NULL);

		for( int i=0;i<images.size();++i){ 
			CCSprite *sprite=CCSprite::spriteWithFile(images[i]); 
			float offsetFraction=((float)(i+1))/(images.size()+1);
			sprite->setPosition(ccp(winSize.width*offsetFraction,35));
			this->addChild(sprite);
			movableSprites->addObject(sprite);
		} 
		//CCTouchDispatcher.sharedDispatcher.addTargetedDelegate:selfpriority:0swallowsTouches:true;
		

}
bool GameHUD::ccTouchBegan(CCTouch* touch, CCEvent* event)
{ 
	cocos2d::CCLog("touch begin");
	//CCPoint touchLocation=this->convertTouchToNodeSpace(touch);
	CCSprite * newSprite=NULL;
	//for( CCSprite* sprite in movableSprites)
	{
		//if(CCRectContainsPoint((sprite.boundingBox,touchLocation)))
		{ 
			DataModel *m=DataModel::getModel();
			//m->_gestureRecognizer.enabled=false;
			selSpriteRange=CCSprite::spriteWithFile("Range.png");
			selSpriteRange->setScale(4);
			this->addChild(selSpriteRange,- 1);
			//selSpriteRange->setPosition(sprite->getposition;
			//newSprite=CCSprite::spriteWithTexture(sprite.texture);
			//sprite;
			//newSprite.position=sprite.position;
			//selSprite=newSprite;
			//this->addChild:newSprite;
			//break;
		}
	}
	return true;
}
void GameHUD::ccTouchMoved(CCTouch* touch, CCEvent* event) 
{ 
	cocos2d::CCLog("touch move");
	//CCPoint touchLocation=this->convertTouchToNodeSpace(touch);
	//CCPoint oldTouchLocation=touch.previousLocationInView:touch.view;
	//oldTouchLocation=CCDirector.sharedDirector.convertToGL:oldTouchLocation;
	//oldTouchLocation=this->convertToNodeSpace:oldTouchLocation;
	//CCPoint translation=ccpSub((touchLocation,oldTouchLocation));
	//if(selSprite){ CCPoint newPos=ccpAdd((selSprite.position,translation));
	//selSprite.position=newPos;
	//selSpriteRange.position=newPos;
	//DataModel * m=DataModel.getModel;
	//CCPoint touchLocationInGameLayer=m._gameLayer.convertTouchToNodeSpace:touch;
	//bool isBuildable=m._gameLayer.canBuildOnTilePosition:touchLocationInGameLayer;
	//if(isBuildable){selSprite.opacity=200;
	//}else{selSprite.opacity=50;
	//}
	//return true;
	//}
}
void  GameHUD::ccTouchEnded(CCTouch* touch, CCEvent* event) 
{ 
	cocos2d::CCLog("touch end");
	//	CCPoint touchLocation=this->convertTouchToNodeSpace:touch;
	//DataModel * m=DataModel.getModel;
	//if(selSprite){ CCRect backgroundRect=CGRectMake((background.position.x,background.position.y,background.contentSize.width,background.contentSize.height));
	//if(! CGRectContainsPoint((backgroundRect,touchLocation))){ CCPoint touchLocationInGameLayer=m._gameLayer.convertTouchToNodeSpace:touch;
	//m._gameLayer.addTower:touchLocationInGameLayer;
	//} this->removeChild:selSpritecleanup:true;
	//selSprite=NULL;
	//this->removeChild:selSpriteRangecleanup:true;
	//selSpriteRange=NULL;
	//}m._gestureRecognizer.enabled=true;
}
//void GameHUD::registerWithTouchDispatcher()
//{ 
//	//CCTouchDispatcher.sharedDispatcher.addTargetedDelegate:selfpriority:0swallowsTouches:true;
//}
//void GameHUD::dealloc()
//{ 
//	movableSprites.release;
//	movableSprites=NULL;
//}
void GameHUD::onEnter()
{
	
    CCTouchDispatcher::sharedDispatcher()->addTargetedDelegate(this, -100, true);
	CCNode::onEnter();
	
}

void GameHUD::onExit()
{
	CCTouchDispatcher::sharedDispatcher()->removeDelegate(this);
	CCNode::onExit();
}	
void GameHUD::touchDelegateRetain()
{
	this->retain();
}
//void GameHUD::registerWithTouchDispatcher() {
//	CCTouchDispatcher::sharedDispatcher()->addTargetedDelegate(this,-100, true);
//}
void GameHUD::touchDelegateRelease()
{
	this->release();
}