//

//  DataModel.m

//  Cocos2D Tower Defense

#include "DataModel.h"
#include "Projectile.h"
#include "Tower.h"
#include "Wave.h"
#include "WayPoint.h"
#include "Creep.h"

DataModel* DataModel::_sharedContext=NULL;

DataModel* DataModel::getModel()
{
	if(_sharedContext==NULL){
		_sharedContext=new DataModel();
	}
	return _sharedContext;
}
//void DataModel::encodeWithCoder(NSCoder * coder)
//{}
//DataModel *  DataModel::initWithCoder(NSCoder * coder)
//{return self;}
DataModel::DataModel()
{
	_projectiles=new CCMutableArray<Projectile *>();
	_towers=new CCMutableArray<Tower*>();
	_targets=new CCMutableArray<Creep *>();
	_waypoints=new CCMutableArray<WayPoint *>();
	_waves=new CCMutableArray<Wave *>();

}
DataModel::~DataModel()
{
	this->_gameLayer=NULL;
	this->_gameHUDLayer=NULL;
	//unused
	this->_towerSelectHUDLayer=NULL;
	this->_pauseHUDLayer=NULL;
	//this->_gestureRecognizer=NULL;
	this->_scoreHUDLayer=NULL;
	_projectiles->release();
	_projectiles=NULL;
	_towers->release();
	_towers=NULL;
	_targets->release();
	_targets=NULL;
	_waypoints->release();
	_waypoints=NULL;
	_waves->release();
	_waves=NULL;
}
