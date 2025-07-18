function intersection(seta,setb){
    let aset = new Set()
    for(let ele of setb){
        if(seta.has(ele)){
            aset.add(ele)
        }
    }
    return aset;
}
let seta = new Set([1,2,3,4])
let setb = new Set([1,3])
console.log(intersection(seta,setb))