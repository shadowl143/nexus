from sqlalchemy import Column, Integer, ForeignKey, Float
from nexus_core.models.database import Base
from sqlalchemy.orm import relationship


class Entrega(Base):
    """Entrega realizada por un Rider."""

    __tablename__ = "entregas"

    # Columnas solicitadas
    id = Column(Integer, primary_key=True)
    rider_id = Column(Integer, ForeignKey("riders.id"), nullable=False)
    distancia_km = Column(Float, nullable=False)
    co2_ahorrado_kg = Column(Float, default=0.0)

    # Relación bidireccional con el modelo Rider
    rider = relationship("Rider", back_populates="entregas")

    # Método opcional útil para depuración (__repr__)
    def __repr__(self) -> str:
        return (
            f"<Entrega(id={self.id}, rider_id={self.rider_id}, km={self.distancia_km})>"
        )
