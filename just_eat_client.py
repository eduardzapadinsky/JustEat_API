"""
This Python script provides a client for interacting with the Just Eat API to retrieve restaurant information by postal
code in the UK.
"""

import argparse

import requests


class JustEatAPIError(Exception):
    """
    Custom exception for errors related to the Just Eat API.
    """
    pass


class InvalidPostalCodeError(Exception):
    """
    Custom exception for invalid postal codes or no restaurants found.
    """
    pass


class JustEatClient:
    """
    A client for interacting with the Just Eat API to retrieve restaurant information by postal code.
    """

    BASE_URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"

    def by_post_code(self, code):
        """
        Retrieve a list of restaurants by postal code.
        """

        url = self.BASE_URL + code
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/117.0.0.0 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            restaurants_list = []

            if not data.get("Restaurants"):
                raise InvalidPostalCodeError("Postal code is wrong or no restaurants found.")

            for restaurant_data in data.get("Restaurants", []):
                restaurant_info = {
                    "Name": restaurant_data.get("Name"),
                    "Rating": restaurant_data.get("Rating", {}).get("Average"),
                    "Cuisines": [cuisine.get("Name") for cuisine in restaurant_data.get("Cuisines", [])]
                }
                restaurants_list.append(restaurant_info)

            return restaurants_list

        except requests.exceptions.RequestException as request_e:
            raise JustEatAPIError(f"Request failed: {request_e}")
        except ValueError as value_e:
            raise JustEatAPIError(f"Failed to parse JSON response: {value_e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve restaurant information by postal code.")
    parser.add_argument("postcode", type=str, help="Postal code for restaurant search")
    args = parser.parse_args()

    client = JustEatClient()
    postcode = args.postcode
    try:
        restaurants = client.by_post_code(postcode)
        print(restaurants)
    except JustEatAPIError as error:
        print(f"An error occurred: {error}")
    except InvalidPostalCodeError as e:
        print(f"Invalid postal code error: {e}")
