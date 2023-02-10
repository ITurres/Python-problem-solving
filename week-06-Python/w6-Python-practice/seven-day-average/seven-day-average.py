import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        else:
            print("Please introduce a valid State\.")
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}

    for data in reader:
        state = data["state"]
        cases = int(data["cases"])

        if state not in new_cases:
            new_cases[state] = []
            previous_cases[state] = []

        if len(previous_cases[state]) >= 15:
            previous_cases[state].pop(0)

        previous_cases[state].append(cases)
    # --------------------|       |----------------------
    for stateX in previous_cases:
        # print(f"{stateX} = {previous_cases[stateX]}")
        for i in range(
            len(previous_cases[stateX])
            - 1  # ?prevents index out of range when using [i+1]
        ):
            curr_case = previous_cases[stateX][i]
            next_case = previous_cases[stateX][i + 1]
            # print(f"curr_case = {curr_case} -- next_case = {next_case}")
            if curr_case != next_case:  # jumps equal cases
                current_case = next_case - curr_case
                new_cases[stateX].append(current_case)
    # print("E.G = New York's Cases => ", new_cases["New York"])
    # print(new_cases)
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in new_cases:
        for input_state in states:
            if state == input_state:
                this_week = new_cases[state][7:]
                previous_week = new_cases[state][:7]
                this_week_average = round(sum(this_week) / 7)
                previous_week_average = round(sum(previous_week) / 7)
                diff_of_weeks = previous_week_average - this_week_average
                increase = round(diff_of_weeks / previous_week_average)
                decrease = round(diff_of_weeks / this_week_average)
                # ***<
                if increase > decrease:
                    print(
                        f"{state} had a 7-day average of {this_week_average} and an increase of {increase}%."
                    )
                else:
                    print(
                        f"{state} had a 7-day average of {this_week_average} and a decrease of {decrease}%."
                    )


main()

# ***>
# print(f"this_week = {this_week}")
# print(f"previous_week = {previous_week}")
# print(f"this_week_average = {this_week_average}")
# print(f"previous_week_average = {previous_week_average}")
# print(f"diff_of_weeks = {diff_of_weeks}")
# print(f"increase = {increase}%")
# print(f"decrease = {decrease}%")
