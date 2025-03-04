from app import app



def test_verify_header(dash_duo):
    dash_duo.start_server(app)
    assert (dash_duo.find_element("h1")).text == "Pink-Morsels Sales Dashboard"

def test_verify_graph(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#pink-morsel-sales-over-time") is not None

def test_verify_radiobutton(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("input[type='radio']") is not None