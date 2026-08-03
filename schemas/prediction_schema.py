def validate_prediction_request(data):

    if "month" not in data:

        raise ValueError(
            "month is required"
        )


    if not isinstance(
        data["month"], int
    ):

        raise ValueError(
            "month must be integer"
        )


    return data