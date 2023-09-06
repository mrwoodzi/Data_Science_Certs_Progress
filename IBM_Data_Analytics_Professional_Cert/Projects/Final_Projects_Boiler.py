def unique_skills():
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
    # Make an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python list of dictionaries
        key_skills = response.json()
        unique_skills = set()
        # Iterate through the job listings and add each location to the set
        for job in key_skills:
            location = job.get("Location")
            if location:
                unique_skills.add(location)
        return list(unique_skills)
    else:
        print("Failed to fetch data from the URL.")
        return []

def get_number_of_jobs_all_L(skills_function):
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
    # Make an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python list of dictionaries
        key_skills = response.json()
        skill__counts = {}
        
        # Get the list of unique locations using the provided location_function
        unique_skills = skills_function

        # Iterate through the job listings and count occurrences of each location
        for skill in unique_skills:
            skill_counts[skill] = 0
            for job in key_skills:
                key_skill = job.get("Key Skills")
                if key_skill and key_skill.lower() == skill.lower():
                    skill__counts[skill] += 1
        
        return unique_skills
    else:
        print("Failed to fetch data from the URL.")
        return {}

# Usage example
unique_skills = unique_skills()
skill_counts = get_number_of_jobs_all_L(unique_skills)
print(unique_skills)