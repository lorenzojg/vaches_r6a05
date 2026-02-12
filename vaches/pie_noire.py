from vaches.vache_a_lait import VacheALait
from vaches.nourriture.TypeNourriture import TypeNourriture
from vaches.exception import InvalidVacheException

class PieNoire(VacheALait):
    COEFFICIENT_NUTRITIONNEL = {TypeNourriture.FOIN : float(0.8), TypeNourriture.MARGUERITE : float(0.5), TypeNourriture.HERBE : float(1.0), TypeNourriture.PAILLE : float(0.2), TypeNourriture.CEREALES : float(1.2)}

    def __init__(self, petit_nom:str=None, poids:float=None, age:int=None, nb_taches_blanches:int=None, nb_taches_noires:int=None): # type: ignore
        super().__init__(petit_nom=petit_nom,poids=poids,age=age)
        if nb_taches_blanches is None or nb_taches_noires is None or type(nb_taches_blanches) is not int or type(nb_taches_noires) is not int:
            raise InvalidVacheException("Le nombre de tâches blanches et noires doit être spécifié pour une vache Pie Noire.")
        elif nb_taches_blanches <= 0 or nb_taches_noires <= 0:
            raise InvalidVacheException("Le nombre de tâches blanches et noires doit être un entier strictement positif.")
        elif nb_taches_blanches + nb_taches_noires == 0:
            raise InvalidVacheException("Une vache Pie Noire doit avoir au moins une tâche blanche ou noire.")
        else :
            self._nb_taches_noires = nb_taches_noires
            self._nb_taches_blanches = nb_taches_blanches
            self._ration : dict[TypeNourriture,float] = {}

    def __str__(self) -> str:
        return super().__str__() + "\nNombre de tâches blanches : " + str(self._nb_taches_blanches) + "\nNombre de tâches noires : " + str(self._nb_taches_noires)

    def brouter(self, quantite: float = None, nourriture: TypeNourriture = None): # type: ignore
        if nourriture is not None and quantite is not None and quantite > 0 :
            if self._ration.get(nourriture) is None :
                self._ration[nourriture] = quantite
            else :
                self._ration[nourriture] += quantite
        elif nourriture is None and quantite is not None :
            super().brouter(quantite)
    
    def _calculer_lait(self, panse: float = None) -> float: # type: ignore
        lait_produit = float()

        if panse is not None and self._ration == {} :
            return super()._calculer_lait(panse)
        else :
            somme = float()
            for nourriture, qte in self._ration.items() :
                somme += qte * PieNoire.COEFFICIENT_NUTRITIONNEL[nourriture]
            lait_produit = somme * PieNoire.RENDEMENT_LAIT
        return lait_produit
    
    def _post_rumination(self, panse_avant: float = None, lait: float = None) -> None: # type: ignore
        self._ration = {}
        return super()._post_rumination(panse_avant, lait)
    
    def _valider_rumination_possible(self):
        if self._ration == {} and self._panse <= 0.0 :
            raise InvalidVacheException

    @property
    def nb_taches_blanches(self):
        return self._nb_taches_blanches
    
    @property
    def nb_taches_noires(self):
        return self._nb_taches_noires
    
    @property
    def ration(self) -> dict[TypeNourriture,float]:
        return self._ration.copy()