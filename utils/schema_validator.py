def validate_data_schema(data):
    required_keys = ["branch.name", "address", "contact_numbers"]
    for item in data:
        for key in required_keys:
            if key not in item:
                raise ValueError(f"Missing required key: {key}")
