#ifndef _scorehud_H_
#define _scorehud_H_
#include "cocos2d.h"
USING_NS_CC;

class ScoreHUD
	: public CCLayer
{
public:
	CCLabelTTF* scoreBoard;
	CCLabelTTF* scoreBoard2;
	int score;
	int life;
	virtual bool init();
	LAYER_NODE_FUNC(ScoreHUD);
	static ScoreHUD * sharedHUD();
	static ScoreHUD *  _sharedHUD;
	void updateScore(int kills);
	void updateLife(int pain);
};
#endif