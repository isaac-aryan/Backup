var handlr=require("fs");
//var x=handlr.readFileSync("file.txt");

//console.log(x.toString());
handlr.readFile("file.txt",function myFunc(error,data){
    if(error){
    console.log(error);
    }
    else{
        console.log(data.toString());
    }
});

console.log("This is the last line in the code.");