def filter_score_factors(score_data):
    # Suppress penalties from known biased categories
    if 'medical_debt' in score_data:
        score_data['medical_debt'] = 0
    if 'zip_code_bias' in score_data:
        score_data['zip_code_bias'] = 0
    return score_data
