#include "cocos2d.h"
extern bool IsMatchDisplay(int w, int h, cocos2d::CCSize& size );
#if (CC_TARGET_PLATFORM == CC_PLATFORM_WIN32)
extern int ViewAutoScale(cocos2d::CCEGLView* view, 
				  void* title,
				  int width, 
				  int height,
				  int defaultWidth,
				  int defaultHeight);
#endif

#if (CC_TARGET_PLATFORM == CC_PLATFORM_ANDROID)
int ViewAutoScale(cocos2d::CCEGLView* view, 
				  void* title,
				  int width, 
				  int height,
				  int defaultWidth,
				  int defaultHeight);
#endif

#if (CC_TARGET_PLATFORM == CC_PLATFORM_IOS)
int ViewAutoScale(cocos2d::CCEGLView* view, 
				  void* title,
				  int width, 
				  int height,
				  int defaultWidth,
				  int defaultHeight);
#endif
