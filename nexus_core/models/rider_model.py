from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from nexus_core.models.database import Base
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

TIPOS_BICI = ("electric", "standard", "cargo")

class Rider(Base):
    """Repartidor de EcoLogistica."""
    __tablename__ = "riders"
    
    # Columnas solicitadas
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    bike_type = Column(String(20))  # Uno de TIPOS_BICI
    
    # Relación bidireccional con el modelo Entrega
    entregas = relationship('Entrega', back_populates='rider')

    # Método para depuración en consola
    def __repr__(self):
        return f"<Rider(name='{self.name}', bike='{self.bike_type}')>"
    