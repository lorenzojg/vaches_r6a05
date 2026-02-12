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
        return super().__str__() + "\nLait disponible : " + str(self._lait_disponible) + " L\nLait total produit : " + str(self._lait_total_produit) + " L\nLait total trait : " + str(self._lait_total_traite) + " L"
    
    def _calculer_lait(self, panse: float = None) -> float: # type: ignore
        if panse is not None :
            lait_produit = panse * VacheALait.RENDEMENT_LAIT
        else :
            raise InvalidVacheException
        return lait_produit

    def _stocker_lait(self, quantite_lait: float) -> None:
        if quantite_lait + self._lait_disponible > VacheALait.PRODUCTION_LAIT_MAX :
             raise InvalidVacheException("Impossible de stocker le lait : la capacité maximale de production de lait a été atteinte.")
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