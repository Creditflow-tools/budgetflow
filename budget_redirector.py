def reprioritize_budget(budget_data):
    essentials = ['housing', 'food', 'transport']
    for item in budget_data:
        if item['category'] not in essentials:
            item['adjusted_priority'] = 'low'
        else:
            item['adjusted_priority'] = 'high'
    return budget_data
