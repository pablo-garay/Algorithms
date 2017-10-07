def compute_result(phrase="bloomberg"):
    result = []
    length = len(phrase)

    count_out = 0
    prev = None

    for i in xrange(length):
        # print result
        if phrase[i] == "b":
            count_out = 0
            count_in = 1

            if prev is not None:  # careful: prev could be 0; gotta check specifically for None
                left = (prev + i) / 2
            else:  # prev is None
                left = -1
            prev = i

            for j in xrange(i - 1, left, -1):
                result[j] = count_in
                count_in += 1

        result.append(count_out)
        count_out += 1

    print result


compute_result(phrase="bloomberg")
compute_result(phrase="loomberg")
compute_result(phrase="loomerg")
compute_result(phrase="bloombergbloomberg")
compute_result(phrase="bloombergloomberg")
compute_result(phrase="bloombergbbloomberg")
compute_result(phrase="bloombergbbbloomberg")
