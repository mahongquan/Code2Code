//

//  ScoreHUD.m

//  TowerDefenseTutorial

//

//  Created by Buford Taylor on 7/6/11.

//  Copyright 2011 __MyCompanyName__. All rights reserved.

//

#include "ScoreHUD.h"
ScoreHUD * ScoreHUD::_sharedHUD=NULL;
ScoreHUD * ScoreHUD::sharedHUD()
{
	if(_sharedHUD==NULL)
		_sharedHUD=new ScoreHUD();// to avoid compiler warning
	return _sharedHUD;
}
//ScoreHUD *  ScoreHUD::alloc()
//{@synchronized(ScoreHUD.class){ NSAssert (_sharedHUD==NULL,@"Attempted to allocate a second instance of a singleton.");
//_sharedHUD=super.alloc;
//return _sharedHUD;}// to avoid compiler warning
//return NULL;}
bool ScoreHUD::init()
{
	if (!CCLayer::init() )
	{
		return false;
	}
	//if((self=super.init)){ 
	//		CCTexture2DPixelFormat currentFormat=CCTexture2D.defaultAlphaPixelFormat;
	// CCTexture2D.setDefaultAlphaPixelFormat:kCCTexture2DPixelFormat_RGBA4444;
	//        scoreBoard = [[CCLabelAtlas labelWithString:@"00" charMapFile:@"fps_images.png" itemWidth:16 itemHeight:24 startCharMap:'.'] retain];
	//        [scoreBoard setPosition:ccp(325, 280)];
	scoreBoard2=CCLabelTTF::labelWithString("Kills 0","Arial",16);
	scoreBoard2->setPosition(ccp(445,310));
	this->addChild(scoreBoard2);
	//scoreBoard=CCLabelTTF.labelWithString:@"Life 10"fontName:@"Arial"fontSize:16;
	// scoreBoard.setPosition:ccp((445,290));
	// this->addChild:scoreBoard;
	// CCTexture2D.setDefaultAlphaPixelFormat:currentFormat;
	score=0;
	life=10;
	return true;
}
void ScoreHUD::updateScore(int kills)
{
	score+=kills;
	//scoreBoard2.setString:NSString.stringWithFormat:@"Kills %d",score;
}
void ScoreHUD::updateLife(int pain)
{life-=pain;
//scoreBoard.setString:NSString.stringWithFormat:@"Life %d",life;
}
//void ScoreHUD::dealloc()
//{ 
//	scoreBoard2.release;
// scoreBoard.release;
// super.dealloc;
//}
