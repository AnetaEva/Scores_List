# function first asks how many test scores the user wants to enter
def get_scores():
    number_of_test_scores = int(input('How many test scores do you have?'))
    # create scores as a list
    # scores_list = [0] * number_of_test_scores
    scores_list = []
    for i in range(number_of_test_scores):
        print('Enter Test Score #:', i + 1)
        score = float(input())
        scores_list.append(score)
    return scores_list


# function takes a SCORES_LIST as the PARAMETER
# DROPS the LOWEST score from the list
# and calculates the average score
def calculate_average(scores_list):
    scores_list.remove(min(scores_list))
    total = 0
    for number in scores_list:
        total = total + number
    average = total / len(scores_list)
    # score_list.remove(min(score_list))
    return average


# function displays the average score
def show_results(scores_list, average):
    print('My list after dropping minimum score: ', scores_list)
    print('Average Score is:', average)


def main():
    scores_list = get_scores()
    print('My scores are:', scores_list)

    # if error occurs and "average is not defined"
    # it means to define on left side of equal sign
    average = calculate_average(scores_list)

    show_results(scores_list, average)


main()
