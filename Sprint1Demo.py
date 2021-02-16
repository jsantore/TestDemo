import secrets
import requests
from typing import Sequence, Dict


def get_data():
    all_data = []
    response = requests.get(
        f'https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.state,school.name,2018.student.size,'
        f'2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line&api_key={secrets.api_key}')
    first_page = response.json()
    if response.status_code != 200:
        print(f"error getting data!: key = {secrets.api_key} error: {response.raw}")  # get rid of this after debugging
        return []

    total_results = first_page['metadata']['total']
    page = 0
    per_page = first_page['metadata']['per_page']
    all_data.extend(first_page['results'])
    while (page + 1) * per_page < total_results:
        page += 1
        response = requests.get(
            f'https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.state,school.name,2018.student.size,'
            f'2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line&api_key={secrets.api_key}&page={page}')
        if response.status_code != 200:  # if we didn't get good data keep going
            continue
        current_page = response.json()
        all_data.extend(current_page['results'])

    return all_data


def save_data(file_name: str, all_data: Sequence[Dict[str, str]]):
    with open(file_name, 'w') as outfile:
        for item in all_data:
            print(item, file=outfile)



def main():
    demo_data = get_data()
    save_data("Sprint1Output.txt", demo_data)


if __name__ == '__main__':
    main()
