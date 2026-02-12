from vaches.exception import InvalidVacheException
from vaches.nourriture.TypeNourriture import TypeNourriture

class Vache :

    AGE_MAX = int(25)
    POIDS_MAX = float(1000.0)
    PANSE_MAX = float(50.0)
    POIDS_MIN_PANSE = float(2.0)
    RENDEMENT_RUMINATION = float(0.25)
    NEXT_ID = int(1)

    def __init__(self, petit_nom:str=None, poids:float=None, age:int=None): # type: ignore
        if petit_nom == None or petit_nom == "" :
            raise InvalidVacheException("Le petit nom de la vache ne peut pas être vide ou None.")
        else :
            is_correct_name = False
            petit_nom_length = len(petit_nom)
            for i in range(petit_nom_length):
                if petit_nom[i] != " " and petit_nom[i]!="\n" and petit_nom[i]!="\t":
                    is_correct_name = True
            
            if not is_correct_name :
                raise InvalidVacheException("Le petit nom de la vache doit contenir au moins un caractère autre que les espaces, les tabulations ou les sauts de ligne.")

        if age < 0 or age > Vache.AGE_MAX :
            raise InvalidVacheException("Age de la vache doit être compris entre 0 et " + str(Vache.AGE_MAX) + " ans.")
        elif poids < 0 :
            raise InvalidVacheException("Poids de la vache doit être positif.")
    
        self._id = Vache.NEXT_ID
        Vache.NEXT_ID += 1
        self._petit_nom = petit_nom
        self._poids = poids
        self._age = age
        self._panse = float(0)
        return
    
    def __str__(self) -> str:
        return "Vache " + str(self._id) + " : " + self._petit_nom + "\nPoids : " + str(self._poids) + " kg\nAge : " + str(self._age) + " ans\nPanse : " + str(self._panse) + " litres"
    
    def brouter(self, quantite:float=None, nourriture:TypeNourriture=None): # type: ignore
        if quantite is None :
            raise InvalidVacheException
        elif quantite <= 0 :
            raise InvalidVacheException
        elif nourriture is not None :
            raise InvalidVacheException
        else :
            if quantite + self._panse <= Vache.PANSE_MAX :
                self._panse += quantite
            else :
                raise InvalidVacheException
    

    def _valider_rumination_possible(self):
        if self._panse <= 0.0 :
            raise InvalidVacheException("Impossible de ruminer : la panse est vide.")

    def ruminer(self):
        self._valider_rumination_possible()
        panse_avant = self._panse
        gain = Vache.RENDEMENT_RUMINATION * panse_avant
        self._poids += gain
        self._panse = 0.0

        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)
        self._post_rumination(panse_avant,lait)


    # Hooks 
    def _calculer_lait(self,panse:float = None) -> float : # type: ignore
        return 0.0

    def _stocker_lait(self,quantite_lait:float) -> None :
        pass

    def _post_rumination(self,panse_avant:float=None,lait:float=None) -> None : # type: ignore
        pass
    #---

    def vieillir(self):
        if self._age < Vache.AGE_MAX :
            self._age += 1
        else :
            raise InvalidVacheException("Impossible de vieillir : la vache a déjà atteint l'âge maximum de " + str(Vache.AGE_MAX) + " ans.")

    @property
    def getId(self) -> int :
        return self._id
    
    @property
    def getPetitNom(self) -> str :
        return self._petit_nom
    
    @property
    def getPoids(self) -> float :
        return self._poids
    
    @property
    def getAge(self) -> int :
        return self._age

    @property
    def getPanse(self) -> float :
        return self._panse