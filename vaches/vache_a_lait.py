from .vache import Vache

class VacheALait(Vache):

    RENDEMENT_LAIT = float(1.1)
    PRODUCTION_LAIT_MAX = float(40.0)

    def __init__(self, petit_nom:str=None, poids:float=None, age:int=None): # type: ignore
        super().__init__(petit_nom=petit_nom,poids=poids,age=age)
        self._lait_disponible = float(0)
        self._lait_total_produit = float(0)
        self._lait_traite = float(0)
    
    def _calculer_lait(self, panse: float) -> float:
        lait_produit = panse * VacheALait.RENDEMENT_LAIT

        if self._lait_disponible + lait_produit >= VacheALait.PRODUCTION_LAIT_MAX :
            lait_produit = VacheALait.PRODUCTION_LAIT_MAX - self._lait_disponible
        
        return lait_produit
       
    def _stocker_lait(self, quantite_lait: float) -> None:
        self._lait_total_produit += quantite_lait
        self._lait_disponible += quantite_lait