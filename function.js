//functions


// function login(){
//     console.log('john,loged in succefully');
    
// }
// login();

// function login(userName,password){
//     console.log(`${userName},logged in successfull`);
    
// }
// login('john');
// login('shyam');
// login('tonny');


// function upperCase(str)
// {
// return str.toUpperCase();
// }

// const result=upperCase('javascript');
// console.log(result);


// function calculateArea(width=1,height=1){//default parametrs
//     const area= width * height;
//     return area;
// }
// const area=calculateArea(30,40);
// console.log(area);

//variable scope

// function download(){
    // const fileName='xyz.pdf';
    // console.log(fileName);
    // 
// }
// download();


// declaration
// function login(){

// }

//function Expression
// const login=function(){
// console.log('loged in');

// }
// login();

//Callback function

// function formatText(text){
//     return text.toUpperCase();
// }
// const result=formatText('hello');
// console.log(result);



// function formatText(text,formatCb){
//     return typeof formatCb==='function'? formatCb(text):text;
//     toUpperCase();
// }
// const res=formatText('abcd',function(text){
//     return text.charAt(0).toUpperCase + text.slice(1);
// });
// console.log(res);



//automatic call to function
// (function login(){
//     console.log('login successfully');
    
// })();


//##arrow function
// const login=()=>{
//     console.log('loged in');
    
// };
// login();

const sum=(num1,num2)=>{
    return num1+num2;
}
const result=sum(10,20);
console.log(result);

