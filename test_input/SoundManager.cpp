﻿package {	import flash.events.Event;	import flash.events.TimerEvent;	import flash.media.Sound;	import flash.media.SoundChannel;	import flash.media.SoundTransform;	import flash.utils.Dictionary;	import flash.utils.Timer;	import Assets.Sounds.*;		public final class SoundManager	{		public static var SoundOn:Boolean = true;		public static var MusicOn:Boolean = true;				private static var Sounds:Dictionary;		private static var Music:SoundChannel;		private static var MusicTimer:Timer;		private static var MusicVolume:SoundTransform;				public static function play(sound:String):void		{			if(SoundOn == false)				return;			Sounds[sound].play(0, 0);		}				public static function startMusic():void		{			if(MusicOn == false)				return;							MusicVolume = new SoundTransform(0, 0);				Music = Sounds["Music"].play(0, int.MAX_VALUE);			if (Music!=null)Music.soundTransform = MusicVolume;						MusicTimer = new Timer(500, 10);			MusicTimer.addEventListener(TimerEvent.TIMER, fadeIn, false, 0, true);			MusicTimer.start();		}				private static function fadeIn(e:TimerEvent):void		{			MusicVolume.volume += 0.05;			if(Music!=null)Music.soundTransform = MusicVolume;		}				public static function stopMusic():void		{			if(Music != null)			{	 			Music.stop();				MusicTimer.stop();				Music = null;			}		}				public static function initialize():void		{			Sounds = new Dictionary();			Sounds["Music"] = new Assets.Sounds.Music();			Sounds["Fire1"] = new Assets.Sounds.Fire1();			Sounds["Fire2"] = new Assets.Sounds.Fire2();			Sounds["Fire3"] = new Assets.Sounds.Fire3();			Sounds["Plane"] = new Assets.Sounds.Plane();			Sounds["Pop1"] = new Assets.Sounds.Pop1();			Sounds["Pop2"] = new Assets.Sounds.Pop2();			Sounds["Pop3"] = new Assets.Sounds.Pop3();			Sounds["Pop4"] = new Assets.Sounds.Pop4();			Sounds["Click1"] = new Assets.Sounds.Click1();			Sounds["Click2"] = new Assets.Sounds.Click2();			Sounds["Click3"] = new Assets.Sounds.Click3();			Sounds["Click4"] = new Assets.Sounds.Click4();		}	}}