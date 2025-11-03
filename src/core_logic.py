import json
from datetime import datetime
from src.data_manager import load_accounts, save_accounts, get_account
# Importar módulos necesarios
from src.modules import mod_cards # Necesario para la HU 3.2

# HU 2.1, 2.2, 2.4: SOLO MODIFICADO POR EQUIPO 2
def update_balance(account_id, amount, description):
    """
    Realiza una transacción, implementando la lógica de balance y seguridad.
    *** SOLO EL EQUIPO 2 DEBE MODIFICAR ESTA FUNCIÓN PARA SUS HISTORIAS DE USUARIO. ***
    """
    accounts = load_accounts()

    # 1. Obtener la cuenta y realizar verificaciones
    account = get_account(account_id)
    if not account or not account.get('is_active', False):
        return False, "Cuenta no encontrada o inactiva."

    # HU 3.2 (Implementación de mod_cards.py): Bloqueo si la tarjeta está congelada.
    if mod_cards.is_card_frozen(account): # Llama a la lógica del Equipo 3
         return False, "Error: Tarjeta virtual congelada. No se permite la transacción."

    # >>> START: Zona de trabajo principal del EQUIPO 2 (Límites, Comisiones, etc.)
    # HU 2.1: Límite Diario. HU 2.4: Comisión por Retiro.
    # >>> END: Zona de trabajo principal del EQUIPO 2

    new_balance = account['balance'] + amount

    # HU 6.4 (Implementación de mod_savings.py): Bloqueo por balance mínimo después del retiro.
    # if not mod_savings.check_minimum_balance(new_balance): ...

    if new_balance < 0:
        # HU 2.2: Registro de error por fondos insuficientes
        return False, "Fondos insuficientes para la transacción."

    # 2. Actualizar y guardar
    for acc in accounts:
        if acc['id'] == account_id:
            acc['balance'] = new_balance
            acc['transactions'].append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "amount": amount,
                "description": description,
                "category": "Sin Asignar" # Campo por defecto, puede ser usado por Equipo 4
            })
            save_accounts(accounts)
            # HU 4.4: Alerta de Sobregiro.
            return True, "Transacción exitosa. Nuevo balance: {}".format(new_balance)

    return False, "Error desconocido al actualizar."
