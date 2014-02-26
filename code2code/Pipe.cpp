#include "Pipe.h"
#include "global.h"
int pipeHeight = 320;
Pipe::Pipe ()
{
    gap=200;
    down= CCSprite::createWithCCSpriteFrameName("pipe_down.png");
    up = CCSprite::createWithCCSpriteFrameName("pipe_up.png");

    down->setPosition(Point(0,pipeHeight + gap));
    this->addChild(down);
    this->addChild(up);
    this->state=PIPE_NEW;
}
void Pipe::changeGap(int score)
{
    gap=gap-score*10;if(gap<100) gap=100;
    down->setPosition(Point(0,pipeHeight + gap));
    CCLog("score:%d",score);
}