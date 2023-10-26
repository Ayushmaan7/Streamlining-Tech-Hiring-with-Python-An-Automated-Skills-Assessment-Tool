def get_user_input(prompt):
    return input(prompt)

def ask_skill_questions():
    skills = ["AWS", "Docker", "Python", "Kubernetes", "Jenkins", "Terraform","Linux"]
    print("required skills are :", skills)
    user_skills = get_user_input("Enter your skills (comma-separated): ").split(",")
    user_skills = [skill.strip() for skill in user_skills]

    matching_skills = set(skills).intersection(user_skills)
    if len(matching_skills) >= 3:
        print("You pass the skills test!")
        return True, matching_skills
    else:
        print("You did not pass the skills test.")
        return False, matching_skills

def ask_scenario_questions(matching_skills):
    skill_to_question = {
        "AWS": "What is the key service for scalable computing in AWS?",
        "Docker": "What is the main benefit of containerization with Docker?",
        "Python": "What is Python's main use case?",
        "Jenkins": "What is the role of Jenkins?",
        "Terraform": "Why we use terraform ?",
        "Kubernetes": "How kubernetes is different from docker ?",
        "Linux": "What is Linux?"

    }
    
    skill_to_answer= {
        "AWS": "amazon ec2",
        "Docker": "save time",
        "Python": "automation",
        "Jenkins": "ci/cd",
        "Terraform": "infra as code",
        "Kubernetes": " managing container",
        "Linux": "os"

    }
    
    passing_score = 0.6 * len(matching_skills)
    score = 0

    # ...
    for skill in matching_skills:
        question = skill_to_question.get(skill, "No question available for this skill.")
        answer = get_user_input(f"{question} ")
        if answer.lower() == skill_to_answer.get(skill, "No answer available for this skill."):  # Corrected line
            score += 1
# ...


    if score >= passing_score:
        print("You pass the scenario questions!")
        return True
    else:
        print("You did not pass the scenario questions.")
        return False

def ask_experience():
    experience = int(get_user_input("Enter your years of experience: "))
    return experience

def ask_salary_expectation(experience):
    if experience < 2:
        print("Salary Range: $40,000 - $60,000")
    elif experience < 5:
        print("Salary Range: $60,000 - $80,000")
    else:
        print("Salary Range: $80,000 - $100,000")

    salary_expectation = int(get_user_input("Enter your salary expectation: $"))
    return salary_expectation

def main():
    name = get_user_input("Enter your name: ")
    qualification = get_user_input("Enter your qualification: ")

    skills_passed, matching_skills = ask_skill_questions()

    if skills_passed:
        passed_scenario = ask_scenario_questions(matching_skills)
        if passed_scenario:
            experience = ask_experience()
            salary_expectation = ask_salary_expectation(experience)

            company_salary_range = (40000, 100000)
            if company_salary_range[0] <= salary_expectation <= company_salary_range[1]:
                print("Congratulations! You are selected.")
            else:
                print("Sorry, you are not selected.")

if __name__ == "__main__":
    main()
