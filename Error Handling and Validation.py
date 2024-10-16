def validate_rule(rule_string):
    # Basic validation for the rule string
    if not re.match(r'^[\w\s<>=!()ANDOR]*$', rule_string):
        raise ValueError("Invalid rule format")

def validate_data(data, expected_attributes):
    for attr in expected_attributes:
        if attr not in data:
            raise ValueError(f"Missing attribute: {attr}")
