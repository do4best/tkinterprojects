function searchit(arr,value){
    for(let i=0; i<arr.length; i++){
        if(arr[i] === value){
            return arr[i];
        }

    }
            return false;
}

let array = [1,2,3,4,5,6]
console.log(searchit(array,5))
function binarySearch(arr,value){
    let lowend = 0,highend=arr.length-1;
    while(lowend <= highend){
        let midRange = Math.floor((lowend + highend)/2)
        if(arr[midRange] === value){
            return midRange;
        }else if(value > arr[midRange]){
            lowend = midRange;
        }else{
            highend = midRange
        }
      
    }
      return -1;

}
console.log(binarySearch(array,5))