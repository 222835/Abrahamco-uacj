from src.data_manager import load_accounts, save_accounts, get_account
from datetime import datetime

def log_incident(account_id, description, priority="MEDIA"):
    """
    HU 5.2 y 5.4: Añade un nuevo incidente a la lista 'incidents'.
    Debe incluir la fecha, descripción y prioridad.
    """
    # El equipo debe buscar la cuenta y añadir el objeto de incidente (con fecha y prioridad)
    # a la lista 'incidents' de la cuenta.
    pass


def get_incident_history(account_id):
    """HU 5.3: Devuelve la lista de incidentes registrados."""
    # El equipo debe obtener la cuenta y retornar la lista 'incidents'.
    pass

if __name__ == '__main__':
    # Zona de prueba para el equipo 5
    pass
