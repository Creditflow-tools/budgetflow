def adjust_projection(model_input):
    model_input['income_growth_rate'] = 0.015  # More realistic baseline
    model_input['inflation_rate'] = 0.035
    return model_input
