if __name__ == '__main__':
    scores_raw = input(f"Enter up to 10 integers from -100 to 100 separated by commas: ")
    scores = [int(x) for x in scores_raw.split(" ")]
    max1 = max(scores)
    max2 = -101
    for i in range(len(scores)):
        if scores[i] > max2 and scores[i] != max1:
            max2 = scores[i]
    print(f"The runner-up score is: {max2}")
