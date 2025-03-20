class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        # Initialize max time and its corresponding button index
        max_time = events[0][1]
        max_time_ind = events[0][0]
        
        n = len(events)
        
        # Iterate through the events
        for i in range(1, n):
            # Calculate the time difference between current and previous event
            temp_time = events[i][1] - events[i-1][1]
            
            # Update max_time and max_time_ind if necessary
            if temp_time > max_time:
                max_time = temp_time
                max_time_ind = events[i][0]
            elif temp_time == max_time:
                # If times are equal, choose the button with the smaller index
                max_time_ind = min(events[i][0], max_time_ind)

        # Return the button index with the longest time
        return max_time_ind