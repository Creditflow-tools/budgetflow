from credit_score_filter import filter_score_factors
from loan_offer_redirector import optimize_offers

def test_credit_filter():
    input_data = {'medical_debt': 2000, 'zip_code_bias': 50}
    result = filter_score_factors(input_data)
    assert result['medical_debt'] == 0
    assert result['zip_code_bias'] == 0

def test_offer_filter():
    offers = [{'apr': 12, 'type': 'personal'}, {'apr': 300, 'type': 'payday'}]
    safe = optimize_offers(offers)
    assert len(safe) == 1
