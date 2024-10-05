# Skill Assessment Script

This Python script assesses a candidate's skills, experience, and salary expectations. It asks the user about their skills, scenario-based questions, years of experience, and desired salary range.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Functionality](#functionality)
- [How It Works](#how-it-works)
- [Conclusion](#conclusion)

## Prerequisites

- Python 3.x installed on your machine.

## Usage

1. Run the script using Python:
   ```bash
   python skill_assessment.py
   ```

2. Follow the prompts to enter your name, qualification, skills, experience, and salary expectations.

## Functionality

The script includes the following key functions:

- **get_user_input(prompt)**: Prompts the user for input.
- **ask_skill_questions()**: Checks if the user has at least 3 matching skills from a predefined list.
- **ask_scenario_questions(matching_skills)**: Asks scenario-based questions related to the matching skills and assesses the answers.
- **ask_experience()**: Prompts the user to enter their years of experience.
- **ask_salary_expectation(experience)**: Suggests a salary range based on experience and prompts the user for their salary expectation.

## How It Works

1. **User Input**: The script starts by asking the user for their name and qualification.
2. **Skills Assessment**: It checks the user's skills against a predefined list.
3. **Scenario Questions**: If the user passes the skills test, they are asked scenario-based questions related to their matching skills.
4. **Experience and Salary**: The user is then prompted for their years of experience and salary expectations.
5. **Final Decision**: The script checks if the user's salary expectation falls within a predefined company salary range and displays the final result.

### Example of Execution

Here’s how the interaction may look:

```plaintext
Enter your name: John Doe
Enter your qualification: Bachelor in Computer Science
required skills are : ['AWS', 'Docker', 'Python', 'Kubernetes', 'Jenkins', 'Terraform', 'Linux']
Enter your skills (comma-separated): AWS, Docker, Python
What is the key service for scalable computing in AWS? amazon ec2
What is the main benefit of containerization with Docker? save time
What is Python's main use case? automation
Enter your years of experience: 3
Salary Range: $60,000 - $80,000
Enter your salary expectation: $70,000
Congratulations! You are selected.
```

## Conclusion

This script serves as a basic skill assessment tool for evaluating candidates based on their skills, experience, and salary expectations. You can modify the skills, questions, and salary ranges as per your requirements.
