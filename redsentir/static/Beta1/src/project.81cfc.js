require=function e(t,n,o){function i(s,r){if(!n[s]){if(!t[s]){var a="function"==typeof require&&require;if(!r&&a)return a(s,!0);if(c)return c(s,!0);var u=new Error("Cannot find module '"+s+"'");throw u.code="MODULE_NOT_FOUND",u}var p=n[s]={exports:{}};t[s][0].call(p.exports,function(e){var n=t[s][1][e];return i(n||e)},p,p.exports,e,t,n,o)}return n[s].exports}for(var c="function"==typeof require&&require,s=0;s<o.length;s++)i(o[s]);return i}({Dragoncito:[function(e,t,n){"use strict";cc._RF.push(t,"8fa34jmdHlHO6DVgow00HQN","Dragoncito"),cc.runtime||cc.Class({extends:cc.Component,editor:{requireComponent:dragonBones.ArmatureDisplay},properties:{touchHandler:{default:null,type:cc.Node},_armature:null,_armatureDisplay:null},onLoad:function(){this._armatureDisplay=this.getComponent(dragonBones.ArmatureDisplay),this._armature=this._armatureDisplay.armature(),this._armatureDisplay.addEventListener(dragonBones.EventObject.FADE_OUT_COMPLETE,this._animationEventHandler,this),this._armatureDisplay.addEventListener(dragonBones.EventObject.COMPLETE,this._animationEventHandler,this),this.touchHandler&&this.mouseEvento()},acelerar:function(){var e=(new Date).getTime();(function t(){var n=(new Date).getTime();dragonBones.WorldClock.clock.advanceTime(.001*(n-e)),e=n,requestAnimationFrame(t)})()},mouseEvento:function(){var e=this;this.touchHandler.on(cc.Node.EventType.TOUCH_START,function(t){e.scheduleOnce(function(){this.node.destroy()},2)},this)},_animationEventHandler:function(e){e.type===dragonBones.EventObject.COMPLETE&&this.node.destroy()}}),cc._RF.pop()},{}],Juego2:[function(e,t,n){"use strict";cc._RF.push(t,"bb3f6ARu3ZOi5wUitkzGP2E","Juego2"),Object.defineProperty(n,"__esModule",{value:!0});var o=cc._decorator,i=o.ccclass,c=o.property,s=function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.keys=new Map,t.Letrero=null,t.Espermas=[null],t.Fondo=null,t.Capaesperma=null,t.delta=0,t.puntaje=0,t}return __extends(t,e),t.prototype.onKeyDown=function(e){switch(this.keys.set(e.keyCode,!0),e.keyCode){case cc.KEY.right:this.keys.has(cc.KEY.shift)?this.Letrero.string="izq y Der":this.Letrero.string="Der"}console.log(this.keys.size)},t.prototype.onKeyUp=function(e){this.keys.delete(e.keyCode)},t.prototype.onLoad=function(){cc.systemEvent.on(cc.SystemEvent.EventType.KEY_DOWN,this.onKeyDown,this),cc.systemEvent.on(cc.SystemEvent.EventType.KEY_UP,this.onKeyUp,this),this.Capaesperma.node.setContentSize(this.node.width,this.node.height),this.node.on("Esper_Captura",function(){this.sumarPuntos(1)},this),this.node.on("GameOver",function(){cc.director.loadScene("GameOver")},this)},t.prototype.start=function(){},t.prototype.sumarPuntos=function(e){this.puntaje+=e,this.Letrero.string="Puntos:"+String(this.puntaje)},t.prototype.update=function(e){this.creadorespermas(e)},t.prototype.creadorespermas=function(e){if(this.delta+=e,!(this.delta<1)){this.delta=0;var t=this.Capaesperma.node,n=(t.getContentSize(),Math.ceil((this.Espermas.length-1)*cc.random0To1())),o=cc.instantiate(this.Espermas[n]);o.setPosition(this.posicionespermas());var i=cc.v2(-600,400),c=cc.moveBy(8,i),s=cc.sequence(c,cc.removeSelf(!0));o.runAction(s),t.addChild(o),o.getComponent(cc.Animation).play("Gome_Anim")}},t.prototype.posicionespermas=function(){var e=this.Capaesperma.node.getContentSize(),t=Math.ceil(e.width*cc.random0To1())+200;return cc.p(t,0)},__decorate([c(cc.Label)],t.prototype,"Letrero",void 0),__decorate([c(cc.Prefab)],t.prototype,"Espermas",void 0),__decorate([c(cc.Node)],t.prototype,"Fondo",void 0),__decorate([c(cc.Layout)],t.prototype,"Capaesperma",void 0),t=__decorate([i],t)}(cc.Component);n.default=s,cc._RF.pop()},{}],Viejo:[function(e,t,n){"use strict";cc._RF.push(t,"94ec4egUzJDj4lOVaq3dDWp","Viejo"),cc.Class({extends:cc.Component,properties:{},onLoad:function(){this.getComponent(cc.Animation).play("Gome_Anim")},start:function(){this.node.on("touchend",function(){this.node.dispatchEvent(new cc.Event.EventCustom("Esper_Captura",!0)),this.getComponent(cc.Animation).play("Explosion"),this.scheduleOnce(function(){this.node.removeFromParent()},2)},this)},update:function(e){this.node.x<270&&this.node.y>320&&this.node.x>0&&this.node.y<600&&this.node.dispatchEvent(new cc.Event.EventCustom("GameOver",!0))}}),cc._RF.pop()},{}],boton:[function(e,t,n){"use strict";cc._RF.push(t,"feb47KBQhVO2KX3oUbJXVQb","boton"),cc.Class({extends:cc.Component,properties:{},start:function(){this.node.on("touchend",function(){cc.director.loadScene("JUEGO_INTER")})}}),cc._RF.pop()},{}],musicafondo:[function(e,t,n){"use strict";cc._RF.push(t,"0583cLzql9BHYq0xF844Va+","musicafondo"),cc.Class({extends:cc.Component,properties:{jumpAudio:{default:null,url:cc.AudioClip}},onLoad:function(){var e=this.current=cc.audioEngine.playEffect(this.jumpAudio,!1,1);cc.repeatForever(e)},start:function(){var e=this.current=cc.audioEngine.playEffect(this.jumpAudio,!1,1);cc.repeatForever(e)}}),cc._RF.pop()},{}],posiciona:[function(e,t,n){"use strict";cc._RF.push(t,"496a7gIKmpDE6NOefFR592z","posiciona"),cc.Class({extends:cc.Component,properties:{Posit:{default:null,type:cc.Label}},start:function(){this.Posit.string="y"+String(this.node.y)+" x"+String(this.node.x)}}),cc._RF.pop()},{}],sonido:[function(e,t,n){"use strict";cc._RF.push(t,"a5e9c/f7KFL6ZZuWGstl3sy","sonido"),cc.Class({extends:cc.Component,properties:{jumpAudio:{default:null,url:cc.AudioClip}},start:function(){this.node.on("touchend",function(){cc.audioEngine.playEffect(this.jumpAudio,!1)},this)}}),cc._RF.pop()},{}]},{},["Dragoncito","Juego2","Viejo","boton","musicafondo","posiciona","sonido"]);