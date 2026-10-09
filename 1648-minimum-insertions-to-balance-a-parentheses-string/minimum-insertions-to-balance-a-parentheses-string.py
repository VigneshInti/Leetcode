class Solution:
    def minInsertions(self, s: str) -> int:
        # Track the number of insertions needed
        insertions_needed = 0
        # Track the number of unmatched left parentheses
        unmatched_left_parens = 0
      
        # Index for traversing the string
        index = 0
        string_length = len(s)
      
        while index < string_length:
            if s[index] == '(':
                # Found a left parenthesis, increment unmatched count
                unmatched_left_parens += 1
            else:
                # Found a right parenthesis, check if there's another one following
                if index < string_length - 1 and s[index + 1] == ')':
                    # Found two consecutive right parentheses, move index forward
                    index += 1
                else:
                    # Only one right parenthesis, need to insert another one
                    insertions_needed += 1
              
                # Now we have a pair of right parentheses (either found or inserted)
                if unmatched_left_parens == 0:
                    # No left parenthesis to match with, need to insert one
                    insertions_needed += 1
                else:
                    # Match with an existing left parenthesis
                    unmatched_left_parens -= 1
          
            # Move to the next character
            index += 1
      
        # After traversing, if there are still unmatched left parentheses,
        # each needs two right parentheses inserted (hence multiply by 2)
        insertions_needed += unmatched_left_parens * 2
      
        return insertions_needed
