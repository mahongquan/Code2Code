#ifndef _GLOBAL_H_
#define _GLOBAL_H_
#include "cocos2d.h"
using namespace cocos2d;
#define MAXLINES 14
#define MOVEDOWN 28
#define ROT_SPEED 2
#define R 16
#define  D  (16*1.732)
#define  DEG_TO_RAD  0.0174532925
#define  BUBBLE_SPEED  8
#define PLAY 0
#define WIN  1
#define FAIL 2
#define ID_LEVEL "level"
#define ID_DIFF "diff"
#define ID_SOUND "sound"
#define bitmapcompressorheight 51
extern int global_level;
extern bool global_sound;
extern bool global_difficult;
extern bool global_win;
//bool IConvConvert(const char *from_charset, const char *to_charset, const char *inbuf, int inlen, char *outbuf, int outlen) ;
//std::string IConvConvert_GBKToUTF8(const std::string& str);
#if (CC_TARGET_PLATFORM == CC_PLATFORM_WIN32)
inline void WStrToUTF8(std::string& dest, const std::string& src){

	dest.clear();

	for (size_t i = 0; i < src.size(); i++){

		wchar_t w = src[i];

		if (w <= 0x7f)

			dest.push_back((char)w);

		else if (w <= 0x7ff){

			dest.push_back(0xc0 | ((w >> 6)& 0x1f));

			dest.push_back(0x80| (w & 0x3f));

		}

		else if (w <= 0xffff){

			dest.push_back(0xe0 | ((w >> 12)& 0x0f));

			dest.push_back(0x80| ((w >> 6) & 0x3f));

			dest.push_back(0x80| (w & 0x3f));

		}

		else if (sizeof(wchar_t) > 2 && w <= 0x10ffff){

			dest.push_back(0xf0 | ((w >> 18)& 0x07)); // wchar_t 4-bytes situation

			dest.push_back(0x80| ((w >> 12) & 0x3f));

			dest.push_back(0x80| ((w >> 6) & 0x3f));

			dest.push_back(0x80| (w & 0x3f));

		}

		else

			dest.push_back('?');

	}

}

//! simple warpper

inline std::string WStrToUTF8(const std::string& str){

	std::string result;

	WStrToUTF8(result, str);

	return result;

}
#endif
#if (CC_TARGET_PLATFORM == CC_PLATFORM_ANDROID)        
inline std::string WStrToUTF8(const std::string & str){

	return str;

}
#endif  // CC_PLATFORM_ANDROID
#define RANGETOP 445
#endif