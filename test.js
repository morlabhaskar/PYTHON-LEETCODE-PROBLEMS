const check = (a) => (b) => (c) => (d) => a + b + (c*d);
const result = check(1)(2)(3)(4)
console.log(result)  //1+2+12=15