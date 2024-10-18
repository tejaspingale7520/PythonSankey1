//arays and loops

//const lang=['javascript','python','c'];
//console.log(lang.length);
//document.writeln(lang.length);
//console.log(lang[2]);

// lang.push('c++');
// lang.unshift('java');
// //lang.pop();
// lang.shift();
// console.log(lang);



//loops

// for(let i = 0; i <= 4; i++){
//     console.log('*')

// }

// for (let index = 0; index <= 4; index++) {
   // console.log("*");
    // document.writeln('*');  
    // 
// }

// const actors=[
//     {
//         name:'actor1',
//         payment:1000
//     },
//     {
//         name:'actor2',
//         payment:100
//     },
//     {
//         name:'actor3',
//         payment:2000
//     }];
     
    // normal foe loop
    // for(let i =0;i <actors.length;i++){
    //     actors[i].payment-=10;    
    // }

    //for each loop
    // actors.forEach(actor => {
    //     actor.payment-=10;
        
    // });


//console.log(actors);

//filter

// const students=[
//     {
//         name:'std1',
//         marks:50

//     },
//     {
//         name:'std2',
//         marks:45

//     },
//     {
//         name:'std3',
//         marks:35

//     }
// ];
// const failed=students.filter((student)=>{
//     if(student.marks < 40){
//         return true;
//     }
//     else 
//     false;
    
// });

//simplified way

//const failed=students.filter(student=> student.marks < 40);
//console.log(failed);
// const passed=students.filter(student=>student.marks > 40);
// console.log(passed);


//map method

// const user=[
//     {
//         fname:'john',
//         lname:'doe'

//     },
//     {
//         fname:'sam',
//         lname:'jorge'

//     },
//     {
//         fname:'andrew',
//         lname:'fernandis'

//     }
    
// ];
// const finalUser=user.map((users)=>{
//     return {
//         //fullname: users.fname +" "+ users.lname
//         fullname:`${users.fname} ${users.lname}`
//     };
// });
// console.log(finalUser);

//Reduce method

const movies=[
    {
        name:'ravan',
        budegt:1000
    },
    {
        name:'ravan2',
        budegt:1500
    },
    {
        name:'ravan3',
        budegt:2000
    }
];

// normally used foreach
// let total=0;
// movies.forEach(movie=>{
// total+=movie.budegt;
// });
// console.log(total);

//using reduce
// const total1=movies.reduce((acc,movie)=>{
//     acc+=movie.budegt;
//     return acc;
// },0);
// console.log(total1);

//indexof

// const admin=[1,2,5];
// const user=
//     {
//         name:'abc',
//         id:2
//     }
// ;

// //const isAdmin=admin.indexOf(user.id) > -1;
// //console.log(isAdmin);

// //indexof or includes
// console.log(admin.includes(user.id));

// by find method

// const users=[
//     {name:'abc',
//         id:1
//     },
//     {name:'pqr',
//         id:2
//     },
//     {name:'xyz',
//         id:3
//     }
// ];

// const myUser=users.find((user)=>{
//     // if(user.id===2){
//     //     return true;
//     // }
//     // else false;
//     return user.name==='abc';
// });
// console.log(myUser);

//sort method

// const names=['john','jane','shyam','ram','sameer','mansi'];
// names.sort();
// console.log(names);

//splice method 
// const names=['john','jane','shyam','ram','sameer','mansi'];
// names.splice(2,2);

// console.log(names);
