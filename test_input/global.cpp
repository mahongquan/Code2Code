#include "global.h"
//#include <iconv\iconv.h>
int global_level=0;
bool global_sound=true;
bool global_difficult=false;
bool global_win=true;
//! convert from wstring to UTF8 using self-coding-converting

//bool IConvConvert(const char *from_charset, const char *to_charset, const char *inbuf, int inlen, char *outbuf, int outlen) 
//
//{
//
//	iconv_t cd = iconv_open(to_charset, from_charset);
//
//	if (cd == 0) return false;
//
//	const char **pin = &inbuf;
//
//	char **pout = &outbuf;
//
//	memset(outbuf,0,outlen);
//
//	size_t ret = iconv(cd,pin,(size_t *)&inlen,pout,(size_t *)&outlen);
//
//	iconv_close(cd);
//
//	return ret == (size_t)(-1) ? false : true;
//
//}
//
//std::string WStrToUTF8(Lconst std::string& str)
//
//{
//
//	const char* textIn = str.c_str();
//
//	char textOut[556];
//
//	bool ret = IConvConvert("gb2312", "utf-8", textIn, strlen(textIn),textOut, 556);
//
//	return ret ? string(textOut) : string();
//
//}