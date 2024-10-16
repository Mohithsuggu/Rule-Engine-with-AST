def main():
    # Sample rules
    rules = [
        "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
        "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    ]
    
    # Validate and combine rules
    combined_rule = combine_rules(rules)
    
    # Sample user data
    user_data = {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
    }

    # Evaluate combined rule
    is_eligible = evaluate_rule(combined_rule, user_data)
    print("User is eligible:", is_eligible)

if __name__ == "__main__":
    main()
