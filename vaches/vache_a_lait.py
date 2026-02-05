from .vache import Vache
from .exception import InvalidVacheException

class VacheALait(Vache):

    RENDEMENT_LAIT = float(1.1)
    PRODUCTION_LAIT_MAX = float(40.0)

    def __init__(self, petit_nom:str=None, poids:float=None, age:int=None): # type: ignore
        super().__init__(petit_nom=petit_nom,poids=poids,age=age)
        self._lait_disponible = float(0)
        self._lait_total_produit = float(0)
        self._lait_total_traite = float(0)
    
    def __str__(self) -> str:
        return super().__str__() + "\nLait disponible :" + str(self._lait_disponible) + " L\nLait total produit : " + str(self._lait_total_produit) + " litres\nLait total traité : " + str(self._lait_traite) + " litres"
    
    def _calculer_lait(self, panse: float) -> float:
        lait_produit = panse * VacheALait.RENDEMENT_LAIT

        if self._lait_disponible + lait_produit >= VacheALait.PRODUCTION_LAIT_MAX :
            lait_produit = VacheALait.PRODUCTION_LAIT_MAX - self._lait_disponible
        
        return lait_produit
       
    def _stocker_lait(self, quantite_lait: float) -> None:
        self._lait_total_produit += quantite_lait
        self._lait_disponible += quantite_lait

    def traire(self, litres: float) -> float:
        if litres > self._lait_disponible:
            raise InvalidVacheException("La vache ne dispose pas de suffisamment de lait pour être trait.")
        elif litres <= 0:
            raise InvalidVacheException("La quantité de lait à traire doit être strictement positive.")
        
        self._lait_disponible -= litres
        self._lait_total_traite += litres

        return litres

    @property
    def getLaitDisponible(self):
        return self._lait_disponible
    
    @property
    def getLaitTotalProduit(self):
        return self._lait_total_produit
    
    @property
    def getLaitTotaltraite(self):
        return self._lait_total_traite