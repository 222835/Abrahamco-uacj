from src.data_manager import load_accounts, save_accounts, get_account
# HU 3.2: Función que es llamada por core_logic.py
def is_card_frozen(account):
    """Verifica si la tarjeta está congelada (True/False)."""
    return account.get('virtual_card_status', 'ACTIVA') == 'CONGELADA'

# HU 3.3
def freeze_card(account_id):
    pass

# HU 3.4
def unfreeze_card(account_id):
    pass
