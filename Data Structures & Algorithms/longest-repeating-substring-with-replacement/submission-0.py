class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        max_length = 0
                                        
        for right in range(len(s)):
                                                            # Add the current character to our frequency map
            count[s[right]] = count.get(s[right], 0) + 1
                                                                                    
                                                                                                # Keep track of the most frequent character in the current window
            max_freq = max(max_freq, count[s[right]])
                                                                                                                        
                                                                                                                                    # Current window size is (right - left + 1)
                                                                                                                                                # Valid window condition: (window size - max_freq) <= k
            if (right - left + 1) - max_freq > k:
                                                                                                                                                                            # If invalid, shrink the window from the left
                count[s[left]] -= 1
                left += 1
                                                                                                                                                                                                                            
                                                                                                                                                                                                                                        # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
        return max_length
                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                        