from typing import Dict, List, Callable, Any
import logging

# Configuración básica de logs para ver eventos en consola
logger = logging.getLogger("nexus_core.bus")


class EventBus:
    def __init__(self) -> None:
        # Diccionario que asocia un "nombre_evento" con una lista de funciones callback
        # Ej: {"rider.created": [audit_service.log_event, kpi_service.update_metrics]}
        self._listeners: Dict[str, List[Callable[[Any], None]]] = {}

    def subscribe(self, event_type: str, callback: Callable[[Any], None]) -> None:
        """Registra una función para que se ejecute cuando ocurra un evento específico."""
        if event_type not in self._listeners:
            self._listeners[event_type] = []

        # Evitamos duplicar la suscripción de la misma función
        if callback not in self._listeners[event_type]:
            self._listeners[event_type].append(callback)
            logger.info(f"Servicio suscrito con éxito al evento: '{event_type}'")

    def publish(self, event_type: str, event_data: Any) -> None:
        """Dispara el evento y ejecuta todas las funciones suscritas a él."""
        if event_type not in self._listeners or not self._listeners[event_type]:
            logger.warning(
                f"Evento '{event_type}' publicado, pero nadie lo está escuchando."
            )
            return

        logger.info(
            f"Disparando evento '{event_type}' para {len(self._listeners[event_type])} suscriptores."
        )

        # Ejecuta cada función callback pasándole los datos del evento (los esquemas Pydantic)
        for callback in self._listeners[event_type]:
            try:
                callback(event_data)
            except Exception as e:
                # Evita que el fallo de un servicio rompa el flujo principal del CRUD
                logger.error(
                    f"Error procesando el evento '{event_type}' en el suscriptor {callback.__name__}: {e}"
                )


# Instancia global única (Singleton) para que todo el proyecto comparta el mismo canal
event_bus = EventBus()
