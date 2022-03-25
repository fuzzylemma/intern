use std::collections::HashMap;

struct Solution { }

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut memo: HashMap<i32,i32> = HashMap::new();
        let mut temp: i32;
        for i in 0..nums.len() {
            temp = target-nums[i]; 
            if memo.contains_key(&temp) {
                return vec![memo[&temp], i as i32]
            }
            memo.insert(nums[i], i as i32);
        }
        return vec![0,0];
    }
}

fn main() {
    println!("{:?}", Solution::two_sum(vec![2,7,11,15], 9));
    println!("{:?}", Solution::two_sum(vec![3,2,4], 6));
    println!("{:?}", Solution::two_sum(vec![3,3], 6));
}
