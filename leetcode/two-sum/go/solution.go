package main

import ( 
    "fmt"
)

func twoSum(nums []int, target int) []int {
    var memo = make(map[int]int) 
    for i, ele := range nums {
        val, exists := memo[target-ele]
        if exists {
            return []int{val,i}
        }
        memo[ele] = i
    }
    return []int{0,0}
}

func main() {
    fmt.Println(twoSum([]int{2,7,11,15}, 9))
    fmt.Println(twoSum([]int{3,2,4}, 6))
    fmt.Println(twoSum([]int{3,3}, 6))
}
