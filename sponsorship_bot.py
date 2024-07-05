import requests
import json
import logging

class SponsorshipBot:
    def _init_(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        logging.basicConfig(level=logging.INFO)

    def sponsor_project(self, project_id, amount):
        url = f"{self.base_url}/sponsor"
        data = {
            "project_id": project_id,
            "amount": amount
        }
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()
            logging.info("Sponsorship successful!")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
        return None

    def get_projects(self):
        url = f"{self.base_url}/projects"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
        return None

if __name__== "_main_":
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.pomwebsite.com"
    
    bot = SponsorshipBot(API_KEY, BASE_URL)
    
    # Get a list of projects
    projects = bot.get_projects()
    if projects:
        if isinstance(projects, list):
            for project in projects:
                print(f"Project ID: {project['id']}, Name: {project['name']}, Description: {project['description']}")
        
            # Sponsor the first project in the list with a specified amount
            if projects:
                project_id = projects[0]['id']
                amount = 100  # The amount of cryptocurrency you want to sponsor
                
                result = bot.sponsor_project(project_id, amount)
                if result:
                    print(result)
                else:
                    print("Sponsorship failed.")
        else:
            print("Failed to parse projects data.")
    else:
        print("No projects available or failed to fetch projects.")
