def suppress_overdraft_trigger(account_event):
    if account_event.get('type') == 'overdraft':
        return {'defer_fee': True, 'grace_period_days': 5}
    return {'defer_fee': False}
