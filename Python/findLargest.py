class Main:

    def findLargest(nums):
        biggest = nums[0]
        for x in nums:
            if x > biggest:
                biggest = x
        
        print(f"{biggest} is the largest number in the list")

    def main():
        numbers = (1, 2, 3, 4, 5)
        Main.findLargest(numbers)

if __name__ == "__main__":
    Main.main()