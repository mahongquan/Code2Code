//
//  bubble3210AppDelegate.cpp
//  bubble3210
//
//  Created by ma hongquan on 12-5-19.
//  Copyright __MyCompanyName__ 2012年. All rights reserved.
//
#include "AppDelegate.h"
#include "SimpleAudioEngine.h"
#include "cocos2d.h"
//#include "Box2dTest.h"

#include "SysMenu.h"
USING_NS_CC;
using namespace CocosDenshion;
AppDelegate::AppDelegate()
{

}

AppDelegate::~AppDelegate()
{
	SimpleAudioEngine::end();
}

bool AppDelegate::initInstance()
{
    bool bRet = false;
    do 
    {
#if (CC_TARGET_PLATFORM == CC_PLATFORM_WIN32)

        // Initialize OpenGLView instance, that release by CCDirector when application terminate.
        // The HelloWorld is designed as HVGA.
        CCEGLView * pMainWnd = new CCEGLView();
        CC_BREAK_IF(! pMainWnd
            || ! pMainWnd->Create(TEXT("cocos2d: Hello World"),600,400));

#endif  // CC_PLATFORM_WIN32
        
#if (CC_TARGET_PLATFORM == CC_PLATFORM_IOS)
        // OpenGLView is initialized in AppDelegate.mm on ios platform, nothing need to do here.
#endif  // CC_PLATFORM_IOS

#if (CC_TARGET_PLATFORM == CC_PLATFORM_ANDROID)        
        // OpenGLView is initialized in HelloWorld/android/jni/helloworld/main.cpp
		// the default setting is to create a fullscreen view
		// if you want to use auto-scale, please enable view->create(320,480) in main.cpp
#endif  // CC_PLATFORM_ANDROID
        
#if (CC_TARGET_PLATFORM == CC_PLATFORM_WOPHONE)

        // Initialize OpenGLView instance, that release by CCDirector when application terminate.
        // The HelloWorld is designed as HVGA.
        CCEGLView* pMainWnd = new CCEGLView(this);
        CC_BREAK_IF(! pMainWnd || ! pMainWnd->Create(320,480, WM_WINDOW_ROTATE_MODE_CW));

#ifndef _TRANZDA_VM_  
        // on wophone emulator, we copy resources files to Work7/TG3/APP/ folder instead of zip file
        cocos2d::CCFileUtils::setResource("HelloWorld.zip");
#endif

#endif  // CC_PLATFORM_WOPHONE

#if (CC_TARGET_PLATFORM == CC_PLATFORM_AIRPLAY)
		// MaxAksenov said it's NOT a very elegant solution. I agree, haha
		CCDirector::sharedDirector()->setDeviceOrientation(kCCDeviceOrientationLandscapeLeft);
#endif
      // CCDirector::sharedDirector()->setDeviceOrientation(kCCDeviceOrientationPortrait); 
        bRet = true;
    } while (0);
    return bRet;
}

bool AppDelegate::applicationDidFinishLaunching()
{
	// initialize director
	CCDirector *pDirector = CCDirector::sharedDirector();
    pDirector->setOpenGLView(&CCEGLView::sharedOpenGLView());

    // enable High Resource Mode(2x, such as iphone4) and maintains low resource on other devices.
    // pDirector->enableRetinaDisplay(true);

	// sets landscape mode
	//pDirector->setDeviceOrientation(kCCDeviceOrientationPortrait);
	//SimpleAudioEngine::sharedEngine()->preloadBackgroundMusic( CCFileUtils::fullPathFromRelativePath("sdk_bgm_06.mp3") );
	//SimpleAudioEngine::sharedEngine()->preloadEffect( CCFileUtils::fullPathFromRelativePath("stick.mp3") );
	//SimpleAudioEngine::sharedEngine()->preloadBackgroundMusic( CCFileUtils::fullPathFromRelativePath("newroot_solo.mp3") );
	//SimpleAudioEngine::sharedEngine()->preloadEffect( CCFileUtils::fullPathFromRelativePath("noh.pm3") );
	//SimpleAudioEngine::sharedEngine()->preloadEffect( CCFileUtils::fullPathFromRelativePath("applause.mp3") );
	//SimpleAudioEngine::sharedEngine()->preloadEffect( CCFileUtils::fullPathFromRelativePath("destroy_group.mp3") );
	//SimpleAudioEngine::sharedEngine()->preloadEffect( CCFileUtils::fullPathFromRelativePath("launch.mp3") );
	//float vb,ve;
	//if(global_sound)
	//{
	//vb= SimpleAudioEngine::sharedEngine()->getBackgroundMusicVolume();
	//ve= SimpleAudioEngine::sharedEngine()->getEffectsVolume();
	//SimpleAudioEngine::sharedEngine()->setBackgroundMusicVolume(1.7);
	//SimpleAudioEngine::sharedEngine()->setEffectsVolume(1.7);
	//vb= SimpleAudioEngine::sharedEngine()->getBackgroundMusicVolume();
	//ve= SimpleAudioEngine::sharedEngine()->getEffectsVolume();
	//}
	/*global_level=CCUserDefault::sharedUserDefault()->getIntegerForKey(ID_LEVEL, 0);
	global_difficult=CCUserDefault::sharedUserDefault()->getBoolForKey(ID_DIFF, false);
	global_sound=CCUserDefault::sharedUserDefault()->getBoolForKey(ID_SOUND, true);*/
	// turn on display FPS
	//pDirector->setDisplayFPS(true);

	// set FPS. the default value is 1.0/60 if you don't call this
	pDirector->setAnimationInterval(1.0 / 30);

	// create a scene. it's an autorelease object
	CCScene *pScene = SysMenu::scene();//HelloWorld::scene();

	// run
	pDirector->runWithScene(pScene);

	return true;
}

// This function will be called when the app is inactive. When comes a phone call,it's be invoked too
void AppDelegate::applicationDidEnterBackground()
{
    CCDirector::sharedDirector()->pause();
    SimpleAudioEngine::sharedEngine()->pauseBackgroundMusic();
	SimpleAudioEngine::sharedEngine()->pauseAllEffects();
}

// this function will be called when the app is active again
void AppDelegate::applicationWillEnterForeground()
{
    CCDirector::sharedDirector()->resume();
    SimpleAudioEngine::sharedEngine()->resumeBackgroundMusic();
	SimpleAudioEngine::sharedEngine()->resumeAllEffects();
}
