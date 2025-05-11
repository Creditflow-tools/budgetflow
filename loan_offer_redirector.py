def optimize_offers(offers):
    safe_offers = []
    for offer in offers:
        if offer['apr'] <= 15 and offer['type'] != 'payday':
            safe_offers.append(offer)
    return safe_offers
