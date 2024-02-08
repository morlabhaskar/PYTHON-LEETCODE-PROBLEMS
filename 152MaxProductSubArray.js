var nums = [2,3,-2,4]

var maxProductArray = function(nums){
    if(nums.length === 0){
        return 0
    }

    let max = nums[0]
    let min = nums[0]
    let res = max

    for(let i = 1 ; i < nums.length ; i++){
        if(nums[i] < 0){
            [min,max] = [max,min]
        }
        max = Math.max(nums[i],max * nums[i])
        min = Math.min(nums[i],min * nums[i])
        res = Math.max(res,max)
    }
    return res
    // console.log(res)

}
