from src.data_manager import load_accounts, save_accounts, get_account
# Importar core_logic si es necesario

def create_new_account(owner_name, initial_deposit):
    """HU 1.1 y 1.2: Crea la estructura base para una nueva cuenta con validaciones."""
    # Lógica de validación aquí...

    accounts = load_accounts()
    new_id = "C" + str(len(accounts) + 100)
    new_account = {
        "id": new_id,
        "owner": owner_name,
        "balance": initial_deposit,
        "is_active": True,
        "virtual_card_status": "ACTIVA",
        "transactions": [],
        "incidents": [],
        "savings_goal": {"target": 0.00, "current": 0.00}
    }
    accounts.append(new_account)
    save_accounts(accounts)
    return new_id

# HU 1.3
def toggle_account_status(account_id):
    pass

# HU 1.4
def check_status(account_id):
    pass
