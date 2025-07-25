function afunction(value,value1){
    return value**value1;
}

console.log(afunction(9,9))
function raisedPower(number,power){
    let result=1;
    for(let i=0; i<power; i++){
        result *= number;
    }
    return result;
}
console.log(raisedPower(9,9))