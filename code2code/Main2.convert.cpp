package 
{
   import flash.media.*;

   public class winJingle extends Sound
   {
		var test1:int;
		var test2:Number=0.5;
		static var s1:int=3.14;
		public function Main2()		
        {
			if (stage)				
                init();
			else				
                addEventListener(Event.ADDED_TO_STAGE, init);
			return;
		}
		static function testSF():void
        {
			s1=123.0; //expression
		}// end function
		private function init(e:Event = null):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);//expression
			//var csd = new CuanSongDai();
			// entry point
			//addChild(new CuanSongDai());
			var ma=1;
			var the:MyCuanSongDai2= new MyCuanSongDai2();// (new SceneMain());
			addChild(the);//expression
			the.x = 100;//expression
			the.startRotate();//expression
            var t=the.x
		}

    }
}