var ev=require("events");
const { EventEmitter } = require("events");
var evEmitter=new ev.EventEmitter();

var x=function helloworld(){
    console.log("hello world");

}




evEmitter.on(x)
evEmitter.emit("hello")