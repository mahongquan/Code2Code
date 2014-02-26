#include "Utils.h"
bool IsMatchDisplay(int w, int h, cocos2d::CCSize& size )
{
	return (w==size.width && h==size.height) || (h==size.width && w==size.height);
}

#if (CC_TARGET_PLATFORM == CC_PLATFORM_WIN32)
int ViewAutoScale(cocos2d::CCEGLView* view, 
				  void* title,
				  int width, 
				  int height,
				  int defaultWidth,
				  int defaultHeight)
{
	if(view == NULL)
	{
		return -1;
	}
	view->Create((LPCTSTR)title, defaultWidth, defaultHeight);

	view->setScreenScale(min((float)width/ defaultWidth, (float)height/ defaultHeight));
	view->resize(width, height);
	view->centerWindow();
	return 0;
}

#endif

#if (CC_TARGET_PLATFORM == CC_PLATFORM_ANDROID)
int ViewAutoScale(cocos2d::CCEGLView* view, 
				  void* title,
				  int width, 
				  int height,
				  int defaultWidth,
				  int defaultHeight)
{
	if(view == NULL)
	{
		return -1;
	}
	view->create(defaultWidth, defaultHeight);
	return 0;
}
#endif

#if (CC_TARGET_PLATFORM == CC_PLATFORM_IOS)
int ViewAutoScale(cocos2d::CCEGLView* view, 
				  void* title,
				  int width, 
				  int height,
				  int defaultWidth,
				  int defaultHeight)
{
	return 0;
}
#endif
