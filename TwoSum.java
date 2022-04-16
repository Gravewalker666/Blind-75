import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numToIndex = new HashMap<>();
        int[] output = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (numToIndex.containsKey(difference)) {
                output[0] = i;
                output[1] = numToIndex.get(difference);
                break;
            } else {
                numToIndex.put(nums[i], i);
            }
        }
        return output;
    }
}
