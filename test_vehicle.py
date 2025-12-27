def test_vehicle_information():
    expected_output=(
        "vehicle_id:v101/n"
        "vehicle name:bullete/n"
        "vehicle price:200000/n"
        "year of purchase:2006/n"
    )
    assert vehicle_information("v101","bullete",200000,2006)==expected_output

