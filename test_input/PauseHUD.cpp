//

//  PauseHUD.m

//  TowerDefenseTutorial

//

//  Created by Buford Taylor on 7/6/11.

//  Copyright 2011 __MyCompanyName__. All rights reserved.

//

#include "PauseHUD.h"
//#include "DataModel.h"
PauseHUD * PauseHUD::_sharedHUD=NULL;
PauseHUD * PauseHUD::sharedHUD()
{
	if(_sharedHUD==NULL)
		_sharedHUD=new PauseHUD();// to avoid compiler warning
	return _sharedHUD;
}
//PauseHUD *  PauseHUD::alloc()
//{@synchronized(PauseHUD.class){ NSAssert (_sharedHUD==NULL,@"Attempted to allocate a second instance of a singleton.");
//_sharedHUD=super.alloc;
//return _sharedHUD;}// to avoid compiler warning
//return NULL;}
bool PauseHUD::init()
{
	if (!CCLayer::init() )
	{
		return false;
	}
	//isPaused=false;
	//shouldResumeAnimation=true;
	// CCTexture2D.setDefaultAlphaPixelFormat:kCCTexture2DPixelFormat_RGB565;
	pauseButton=CCSprite::spriteWithFile("pause-red.png");
	//pauseButton->setScale=0.10f;
	// pauseButton->setPosition(ccp(20,300));
	 this->addChild(pauseButton);
	//towerSelectButton=CCSprite.spriteWithFile:@"pause-red.png";
	//towerSelectButton.scale=0.10f;
	// towerSelectButton.setPosition:ccp((50,300));
	// this->addChild:towerSelectButton;
	// CCTexture2D.setDefaultAlphaPixelFormat:kCCTexture2DPixelFormat_Default;
	// CCTouchDispatcher.sharedDispatcher.addTargetedDelegate:selfpriority:0swallowsTouches:false;
	return true;
}
//void PauseHUD::ccTouchEndedwithEvent(UITouch * touch,UIEvent * event)
//{ CCPoint touchLocation=this->convertTouchToNodeSpace:touch;
//if(CGRectContainsPoint((pauseButton.boundingBox,touchLocation))){if(isPaused){ CCTexture2D *texture2D=[[CCTexture2D alloc]initWithImage:[UIImage imageNamed:@"pause-red.png"]]; pauseButton.setTexture:texture2D;
//isPaused=false;
//shouldResumeAnimation=true;
//}else{ CCTexture2D *texture2D=[[CCTexture2D alloc]initWithImage:[UIImage imageNamed:@"play-green.png"]]; pauseButton.setTexture:texture2D;
//isPaused=true;
//}}if(CGRectContainsPoint((towerSelectButton.boundingBox,touchLocation))){ DataModel *m=[DataModel getModel]; m._towerSelectHUDLayer.toggleTSHUDwithSpeed:2;
//}}
//bool PauseHUD::ccTouchBeganwithEvent(UITouch * touch,UIEvent * event)
//{return true;}
//void PauseHUD::registerWithTouchDispatcher()
//{ CCTouchDispatcher.sharedDispatcher.addTargetedDelegate:selfpriority:0swallowsTouches:true;
//}
//void PauseHUD::dealloc()
//{ pauseButton.release;
// super.dealloc;
//}
