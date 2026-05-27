# Given a stream of integers and window size n, calculate the moving average of all the integers of the sliding window.

# Implement the Solution class:

#    MovingAverage(int size) Initializes the object with the size of the window size, which is n.
#    double next(int x) Calculates and returns the moving average of the last n values of the integer stream.


# Example 1:

#     Input: ["MovingAverage", "next", "next", "next"], [[2], [1], [10], [3]]
#     Expected Output: [null, 1.0, 5.5, 6.5]
#     Justification: The moving average of the last 2 numbers. Initially, it's 1. Then (1+10)/2 = 5.5, and (10+3)/2 = 6.5.


# Example 2:

#     Input: ["MovingAverage", "next", "next"], [[4], [5], [15]]
#     Expected Output: [null, 5.0, 10.0]
#     Justification: First, the average is 5. Then, (5+15)/2 = 10 as we consider the last 4 numbers, but only two numbers are in the stream.


# Example 3:

#     Input: ["MovingAverage", "next", "next", "next", "next"], [[3], [7], [4], [8], [5]]
#     Expected Output: [null, 7.0, 5.5, 6.33, 5.67]
#     Justification: Moving average calculations are (7), (7+4)/2, (7+4+8)/3, and (4+8+5)/3.




from collections import deque

class MovingAverageFromData:
    def __init__(self, size):
        self.size = size  # Size of the moving window
        self.queue = deque()  # Double-ended queue to store elements
        self.sum = 0  # Sum of the elements in the current window

    def next(self, val):
        self.queue.append(val)  # Add new value to the queue
        self.sum += val  # Add new value to the sum

        # If the queue size exceeds the window size, remove the oldest element
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()  # Subtract the oldest value from the sum

        # Return the average of the elements in the current window
        return self.sum / min(len(self.queue), self.size)

# Main function to test the algorithm with example inputs
if __name__ == "__main__":
    operations = ["MovingAverage", "next", "next", "next", "next"]
    values = [3, 7, 4, 8, 5]

    obj = None
    for op, val in zip(operations, values):
        if op == "MovingAverage":
            obj = Solution(val)
            print("null")
        elif op == "next":
            # Print the moving average after each next operation
            print(obj.next(val))



