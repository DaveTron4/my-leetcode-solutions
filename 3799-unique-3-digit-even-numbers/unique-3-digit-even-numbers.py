class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        hashmap = {}
        index = 0
        for i in digits:
            hashmap[index] = i
            index += 1

        print(hashmap)
        total_unique = len(hashmap)


        if set(digits) <= 2:
            return 1

        final = set()

        for i in range(total_unique):
            for j in range(total_unique):
                for k in range(total_unique):
                    keys = [i, j, k]
                    print(keys)
                    if i != j and j != k and k != i:
                        if hashmap[i] == 0:
                            continue
                        else:
                            num = "".join(str(hashmap[key]) for key in keys)
                            if int(num) % 2 == 0:
                                print(num)
                                final.add(num)
                                
        return len(final)
        