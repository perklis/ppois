from typing import List
from patients.MedicalCard import MedicalCard

class MedicalCardsArchive:
    def __init__(self):
        self._cards: List[MedicalCard] = []

    def _add_card(self, card: MedicalCard):
        self._cards.append(card)

    def get_card_by_name(self, patient_name: str) -> MedicalCard | None:
        for card in self._cards:
            if card.patient.name == patient_name:
                return card
        return None
    
    def _all_cards(self) -> List[MedicalCard]:
        return self._cards
